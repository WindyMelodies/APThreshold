"""Class for estimating spike threshold using waveform-curvature based method"""
import logging
from utils.condition_check import data_source_check, data_exists_check, spike_check
from utils.tools import get_decimal_digits, get_voltage_from_AP_data, get_voltage_from_data, \
    get_timestamp_from_data, get_max_num
import copy
import numpy as np
import unicodeit
from PySide6.QtWidgets import QMessageBox


class MethodBasedOnCurvature:
    """Estimate spike threshold using waveform-curvature based method"""

    def __init__(self, main_window, option, k_th, voltage_option):
        self.voltage_option = voltage_option
        self.data_operation_module = None
        self.main_window = main_window
        self.option = option
        self.figure_set = None
        self.figure_set_origin = None
        self.dt = None
        self.k_th = k_th
        self.SpikeThresholds = []
        self.AP = self.main_window.AP
        # Check whether the conditions for quantifying spike threshold are met
        self.condition = self.identify_run_condition()
        # Measure spike threshold of all extracted single action potentials (APs)
        if self.condition:
            self.extract_AP_data()
            if int(option) == 0:
                self.method_1()
            elif int(option) == 1:
                self.method_2()
            elif int(option) == 2:
                self.method_3()
            elif int(option) == 3:
                self.method_4()
            elif int(option) == 4:
                self.method_5()

            ISI = self.calculate_ISI()
            self.calculate_superposition_APs()
            self.get_data(ISI)
            # Initialize the default plot settings
            self.get_figure_set_origin()

    def identify_run_condition(self):
        """
        Identifies if the conditions for estimating spike threshold are met

        Conditions for calculating spike threshold:
        1. Spike data exist in 'Action Potential' page
        2. Single APs are extracted through 'AP' button
        3. Spike exists in voltage trace
        4. For the waveform curvature-based method: K_th must be greater than 0
        """
        if data_exists_check(main_window=self.main_window):
            if self.main_window.doubleSpinBox_kth_curvature.value() > 0:
                self.pre_info()
                if self.spike:
                    return True
                else:
                    msg_box = QMessageBox(QMessageBox.Information, 'Message', 'No spike!')
                    msg_box.exec()
                    return False
            else:
                msg_box = QMessageBox(QMessageBox.Information, 'Message', 'K_th can not be zero!')
                msg_box.exec()
                return False

        else:
            msg_box = QMessageBox(QMessageBox.Information, 'Message', 'No action potential！')
            msg_box.exec()
            return False

    def pre_info(self):
        """Prepare necessary parameters and data for subsequent spike threshold dynamics quantification"""
        self.data_source, self.voltage_option, self.data, self.dt = data_source_check(
            self.main_window)
        logging.info(f'data_source: {self.data_source}')
        logging.info(f'voltage_option: {self.voltage_option}')
        self.voltage = get_voltage_from_data(data=self.data, data_source=self.data_source,
                                             voltage_option=self.voltage_option)
        self.timestamp = get_timestamp_from_data(data=self.data)
        self.spike, self.spike_count, self.spike_flag = spike_check(self.voltage)

    def extract_AP_data(self):
        """
        Extracts single AP data based on the current spike data source (simulation data or experimental recordings)

        Notes:
            The data source is determined by the position of panel in the 'Action Potential'. When extracting single APs,
            the panel of 'Action potential' page should be in corresponding position of spike data.
        """
        if self.main_window.toolBox_aquire_ap.currentIndex() == 0:
            if self.main_window.Model:
                self.data_operation_module = self.main_window.Model
                self.AP_data(dt=self.main_window.Model.dt, AP=self.AP, data=self.data_operation_module.data,
                             timestamp=self.data_operation_module.t)
        else:
            if self.main_window.widget_physiological_data.data:
                timestamp = self.main_window.widget_physiological_data.data['timestamp']['timestamp']
                self.AP_data(dt=self.main_window.widget_physiological_data.dt, AP=self.AP,
                             data=self.main_window.widget_physiological_data.data, timestamp=timestamp)

    @staticmethod
    def AP_data(dt, AP: dict, data, timestamp):
        """Extract data of all single APs"""
        decimal_digits = get_decimal_digits(dt)
        AP_temporary = copy.deepcopy(AP)
        for i in AP_temporary:
            AP[i]['features'] = {}
            if 'start' in AP[i]:
                start = round(AP[i]['start'], decimal_digits)
                stop = round(AP[i]['stop'], decimal_digits)
                index1 = list(timestamp).index(start)
                index2 = list(timestamp).index(stop)
                for j in data:
                    AP[i][j] = {}
                    for k in data[j]:
                        if k == 'label':
                            AP[i][j][k] = data[j][k]
                        else:
                            AP[i][j][k] = data[j][k][index1:index2 + 1]

    def method_1(self):
        """First derivative method for estimating spike threshold"""
        data_source, _, _, _ = data_source_check(self.main_window)
        for i in self.AP:
            if data_source == 'simulation':
                index, SpikeThreshold, t_Vth = self.temporal_derivative_method(
                    dVdt=self.AP[i]['derivative voltage'][unicodeit.replace(
                        'd{}/dt'.format(self.voltage_option))], voltage=self.AP[i]['voltage'][self.voltage_option],
                    k_th=self.k_th, timestamp=self.AP[i]['timestamp']['timestamp'])
            else:
                data = self.AP[i]
                index, SpikeThreshold, t_Vth = self.temporal_derivative_method(
                    dVdt=data['voltage'][unicodeit.replace('dV/dt')], voltage=data['voltage']['voltage'],
                    k_th=self.k_th, timestamp=data['timestamp']['timestamp'])
            logging.info(
                'First derivative method: index: {}, spike threshold: {}, spike time: {}'.format(index, SpikeThreshold,
                                                                                                 t_Vth))
            self.AP[i]['index'] = index
            self.AP[i]['features']['Vth'] = SpikeThreshold
            self.AP[i]['timestamp']['timestamp_Vth'] = t_Vth

    def method_2(self):
        """Second derivative method for estimating spike threshold"""
        data_source, _, _, _ = data_source_check(self.main_window)
        for i in self.AP:
            if data_source == 'simulation':
                index, SpikeThreshold, t_Vth = self.temporal_derivative_method(
                    dVdt=self.AP[i]['derivative voltage'][unicodeit.replace(
                        'd^2{}/dt^2'.format(self.voltage_option))], voltage=self.AP[i]['voltage'][self.voltage_option],
                    k_th=self.k_th, timestamp=self.AP[i]['timestamp']['timestamp'])
            if data_source == 'txt' or data_source == 'mat' or data_source == 'bin' or data_source == 'dat':
                data = self.AP[i]
                index, SpikeThreshold, t_Vth = self.temporal_derivative_method(
                    dVdt=data['voltage'][unicodeit.replace('d^2V/dt^2')], voltage=data['voltage']['voltage'],
                    k_th=self.k_th, timestamp=data['timestamp']['timestamp'])
            self.AP[i]['index'] = index
            self.AP[i]['features']['Vth'] = SpikeThreshold
            self.AP[i]['timestamp']['timestamp_Vth'] = t_Vth

    def method_3(self):
        """Third derivative method for estimating spike threshold"""
        data_source, _, _, _ = data_source_check(self.main_window)

        for i in self.AP:
            if data_source == 'simulation':
                index, SpikeThreshold, t_Vth = self.temporal_derivative_method(
                    dVdt=self.AP[i]['derivative voltage'][unicodeit.replace(
                        'd^3{}/dt^3'.format(self.voltage_option))], voltage=self.AP[i]['voltage'][self.voltage_option],
                    k_th=self.k_th, timestamp=self.AP[i]['timestamp']['timestamp'])
            if data_source == 'txt' or data_source == 'mat' or data_source == 'bin' or data_source == 'dat':
                data = self.AP[i]
                index, SpikeThreshold, t_Vth = self.temporal_derivative_method(
                    dVdt=data['voltage'][unicodeit.replace('d^3V/dt^3')], voltage=data['voltage']['voltage'],
                    k_th=self.k_th, timestamp=data['timestamp']['timestamp'])
            self.AP[i]['index'] = index
            self.AP[i]['features']['Vth'] = SpikeThreshold
            self.AP[i]['timestamp']['timestamp_Vth'] = t_Vth

    @staticmethod
    def temporal_derivative_method(dVdt, voltage, k_th, timestamp):
        """
        Parameters
        ----------
        dVdt : array
            The time derivative of membrane voltage for a single AP.
        voltage : array
        k_th : float
            A key parameter for spike threshold quantification
        timestamp : array
        Returns
        -------
        index：int
            The index of the spike threshold in the action potential voltage sequence.
        SpikeThreshold：float
        t_Vth：float
            The time corresponding to spike threshold
        """
        SpikeThresholdIndex = None
        for j in dVdt:
            if j == None:
                pass
            else:
                if j >= k_th:
                    SpikeThresholdIndex = np.where(dVdt == j)[0][0]
                    break

        index = SpikeThresholdIndex
        SpikeThreshold = voltage[index]
        t_Vth = timestamp[index]
        logging.info(f'index: {index}, SpikeThreshold: {SpikeThreshold}, t_Vth: {t_Vth}')
        return index, SpikeThreshold, t_Vth

    def method_4(self):
        """Maximal slope method for estimating spike threshold"""
        data_source, _, _, _ = data_source_check(self.main_window)
        for i in self.AP:
            if data_source == 'simulation':
                index, SpikeThreshold, t_Vth = self.maximum_slope_method_based_on_phase_space(
                    voltage=self.AP[i]['voltage'][self.voltage_option],
                    dVdt_1=self.AP[i]['derivative voltage'][unicodeit.replace(
                        'd{}/dt'.format(self.voltage_option))],
                    dVdt_2=self.AP[i]['derivative voltage'][unicodeit.replace(
                        'd^2{}/dt^2'.format(self.voltage_option))], timestamp=self.AP[i]['timestamp']['timestamp'],
                    dt=self.dt)
            if data_source == 'txt' or data_source == 'mat' or data_source == 'bin' or data_source == 'dat':
                data = self.AP[i]
                index, SpikeThreshold, t_Vth = self.maximum_slope_method_based_on_phase_space(
                    voltage=data['voltage']['voltage'], dVdt_1=data['voltage'][unicodeit.replace('dV/dt')],
                    dVdt_2=data['voltage'][unicodeit.replace('d^2V/dt^2')], timestamp=data['timestamp']['timestamp'],
                    dt=self.dt)
            self.AP[i]['index'] = index
            self.AP[i]['features']['Vth'] = SpikeThreshold
            self.AP[i]['timestamp']['timestamp_Vth'] = t_Vth

    def method_5(self):
        """Maximal slope method for estimating spike threshold"""
        data_source, _, _, _ = data_source_check(self.main_window)
        for i in self.AP:
            if data_source == 'simulation':
                index, SpikeThreshold, t_Vth = self.maximum_second_derivative_method_based_on_phase_space(
                    voltage=self.AP[i]['voltage'][self.voltage_option],
                    dVdt_1=self.AP[i]['derivative voltage'][unicodeit.replace(
                        'd{}/dt'.format(self.voltage_option))],
                    dVdt_2=self.AP[i]['derivative voltage'][unicodeit.replace(
                        'd^2{}/dt^2'.format(self.voltage_option))],
                    dVdt_3=self.AP[i]['derivative voltage'][unicodeit.replace(
                        'd^3{}/dt^3'.format(self.voltage_option))], timestamp=self.AP[i]['timestamp']['timestamp'],
                    dt=self.dt)
            if data_source == 'txt' or data_source == 'mat' or data_source == 'bin' or data_source == 'dat':
                data = self.AP[i]
                index, SpikeThreshold, t_Vth = self.maximum_second_derivative_method_based_on_phase_space(
                    voltage=data['voltage']['voltage'], dVdt_1=data['voltage'][unicodeit.replace('dV/dt')],
                    dVdt_2=data['voltage'][unicodeit.replace('d^2V/dt^2')],
                    dVdt_3=data['voltage'][unicodeit.replace('d^3V/dt^3')], timestamp=data['timestamp']['timestamp'],
                    dt=self.dt)
            self.AP[i]['index'] = index
            self.AP[i]['features']['Vth'] = SpikeThreshold
            self.AP[i]['timestamp']['timestamp_Vth'] = t_Vth

    @staticmethod
    def maximum_slope_method_based_on_phase_space(voltage, dVdt_1, dVdt_2, timestamp, dt):
        """
        Parameters
        ----------
        voltage : array
        dVdt_1 : array
            The first temporal derivative of membrane voltage for a single AP.
        dVdt_2 : array
            The Second temporal derivative of membrane voltage for a single AP.
        timestamp : array
        dt: float
            The time step between data points
        Returns
        -------
        index_Vth：int
            The index of the spike threshold in the action potential voltage sequence.
        Vth：float
        timestamp_Vth：float
            The time corresponding to spike threshold
        """
        index_dvdt1_max = list(dVdt_1).index(get_max_num(dVdt_1))
        # Find the start of the region where dV/dt>0 in the phase space
        for i in range(index_dvdt1_max, -1, -1):
            if dVdt_1[i] <= 0:
                index_dvdt1_start = i + 1
            if i == 0:
                index_dvdt1_start = i
        # Calculate the slope of the phase space
        slope_array = (dVdt_2 / dVdt_1)[index_dvdt1_start:index_dvdt1_max + 1]

        index_Vth = np.where(slope_array == max(slope_array))[0][0] + index_dvdt1_start
        Vth = voltage[index_Vth]
        timestamp_Vth = timestamp[index_Vth]
        return index_Vth, Vth, timestamp_Vth

    @staticmethod
    def maximum_second_derivative_method_based_on_phase_space(voltage, dVdt_1, dVdt_2, dVdt_3, timestamp, dt):
        """
         Parameters
        ----------
        voltage : array
        dVdt_1 : array
            The first temporal derivative of membrane voltage for a single AP.
        dVdt_2 : array
            The Second temporal derivative of membrane voltage for a single AP.
        timestamp : array
        dt: float
            The time step between data points
        Returns
        -------
        index_Vth：int
            The index of the spike threshold in the action potential voltage sequence.
        Vth：float
        timestamp_Vth：float
            The time corresponding to spike threshold
        """
        index_dvdt1_max = np.where(dVdt_1 == max(dVdt_1))[0][0]
        # Find the start of the region where dV/dt>0 in the phase space
        for i in range(index_dvdt1_max, -1, -1):
            if dVdt_1[i] <= 0:
                index_dvdt1_start = i + 1
            if i == 0:
                index_dvdt1_start = i
        # Find the end of the region where dV/dt>0 in the phase space
        for i in range(index_dvdt1_max, len(dVdt_1) - 1):
            if dVdt_1[i] <= 0:
                index_dvdt1_end = i - 1
                break
            if i == len(dVdt_1) - 2:
                index_dvdt1_end = i

        array = ((dVdt_1 * dVdt_3 - dVdt_2 ** 2) / (dVdt_1 ** 3))[index_dvdt1_start:index_dvdt1_end + 1]
        # test the method
        # t_array = np.linspace(0, (len(array) - 1) * dt, len(array)) + min(timestamp) + index_dvdt1_start * dt
        # with open(r'D:\ProgramingProject\python\Platform_Development\results\MaximumSecondDerivativeMethod.pkl',
        #           'wb') as f:
        #     pickle.dump((array, t_array), f)
        index_Vth = np.where(array == max(array))[0][0] + index_dvdt1_start
        Vth = voltage[index_Vth]
        timestamp_Vth = timestamp[index_Vth]
        return index_Vth, Vth, timestamp_Vth

    def calculate_ISI(self):
        """
        Calculate the Inter-Spike Interval (ISI) for all extracted action potentials.

        The method works as follows:
        1. Identify spikes in the membrane voltage sequence and store the time when Vm cross 0 mV.
        2. Find the peak time for each spike.
        3. Calculate the ISI based on the peak times of all identified spikes.
        4. Extract the ISI values for the selected single APs based on their peak times.

        Returns
        -------
        ISI_APs : array
            The ISI values for the extracted APss.

        Notes
        -----
        The calculation will only proceed if at least two spikes are present. If less than two spikes are detected,
        or if no spikes are found, `None` values are returned for all action potentials.
        """
        # Only compute ISI if spikes exist
        if self.spike:
            if self.spike_count >= 2:   # At least two spikes are required for ISI calculation
                list_voltage_max, list_voltage_max_moment, list_index_voltage_max = peak_time(
                    spike_flag=self.spike_flag,
                    voltage=self.voltage,
                    timestamp=self.timestamp)
                logging.info(f'Action potential peak times: {list_voltage_max_moment} ms')

                ISI_all, list_voltage_max = calculate_all_ISI(list_voltage_max_moment=list_voltage_max_moment,
                                                              list_voltage_max=list_voltage_max)
                logging.info(f'ISI values for all action potentials: {ISI_all}, Total number:{ISI_all}')
                ISI_APs = calculate_extracted_AP_ISI(AP=self.AP, list_voltage_max_moment=list_voltage_max_moment,
                                                     ISI_all=ISI_all,
                                                     voltage_option=self.voltage_option, data_source=self.data_source,
                                                     )
                logging.info(f'ISI values for extracted action potentials: {ISI_APs}',)
                return ISI_APs
            else:
                return np.full(len(self.AP), fill_value=None)
        else:
            return np.full(len(self.AP), fill_value=None)

    def calculate_superposition_APs(self):
        """
        Generate the superposition of all extracted APs
        """
        list_index_voltage_max = {}

        for i in self.AP:
            voltage = get_voltage_from_AP_data(AP_data=self.AP, AP_name=i, data_source=self.data_source,
                                               voltage_option=self.voltage_option)
            index = list(voltage).index(max(voltage))
            list_index_voltage_max[i] = index
        store_ap_pre_length = {}
        store_ap_post_length = {}
        max_ap_pre_length = None
        max_ap_post_length = None
        for i in self.AP:
            voltage = get_voltage_from_AP_data(AP_data=self.AP, AP_name=i, data_source=self.data_source,
                                               voltage_option=self.voltage_option)
            ap_pre_length = list_index_voltage_max[i] + 1
            ap_post_length = len(voltage) - ap_pre_length
            if max_ap_post_length is None:
                max_ap_pre_length = ap_pre_length
            else:
                if max_ap_pre_length < ap_pre_length:
                    max_ap_pre_length = ap_pre_length
            if max_ap_post_length is None:
                max_ap_post_length = ap_post_length
            else:
                if max_ap_post_length < ap_post_length:
                    max_ap_post_length = ap_post_length
            store_ap_pre_length[i] = ap_pre_length
            store_ap_post_length[i] = ap_post_length
        SpikeThresholds = {}
        for i in self.AP:
            spike_threshold = self.AP[i]['features']['Vth']
            SpikeThresholds[i] = spike_threshold
        for j in self.AP:
            voltage = get_voltage_from_AP_data(AP_data=self.AP, AP_name=j, data_source=self.data_source,
                                               voltage_option=self.voltage_option)
            ap_voltage_complete = copy.deepcopy(voltage)
            pre = np.full((int(max_ap_pre_length - store_ap_pre_length[j]),), np.nan)
            post = np.full((int(max_ap_post_length - store_ap_post_length[j], )), np.nan)
            voltage_superposition = np.concatenate((pre, ap_voltage_complete, post))
            timestamp_superposition = np.linspace(0,
                                                  (len(voltage_superposition) - 1) * self.dt,
                                                  len(voltage_superposition))

            timestamp_Vth_superposition = timestamp_superposition[
                np.where(voltage_superposition == SpikeThresholds[j])[0][0]]
            self.AP[j]['V_superposition'] = voltage_superposition
            self.AP[j]['timestamp_superposition'] = timestamp_superposition
            self.AP[j]['timestamp_Vth_superposition'] = timestamp_Vth_superposition

    def get_data(self, ISI):
        """
        Store data in self.data
        """
        self.data = copy.deepcopy(self.AP)
        Vth_list = []
        timestamp_Vth_list = []
        V_superposition_list = []
        timestamp_superposition_list = []
        timestamp_Vth_superposition_list = []
        for i in self.AP:
            Vth = self.AP[i]['features']['Vth']
            timestamp_Vth = self.AP[i]['timestamp']['timestamp_Vth']
            V_superposition = self.AP[i]['V_superposition']
            timestamp_superposition = self.AP[i]['timestamp_superposition']
            timestamp_Vth_superposition = self.AP[i]['timestamp_Vth_superposition']
            self.data[i].pop('start')
            self.data[i].pop('stop')
            self.data[i].pop('V_superposition')
            self.data[i].pop('timestamp_superposition')
            self.data[i].pop('timestamp_Vth_superposition')
            self.data[i].pop('index')
            Vth_list.append(Vth)
            timestamp_Vth_list.append(timestamp_Vth)
            V_superposition_list.append(V_superposition)
            timestamp_superposition_list.append(timestamp_superposition)
            timestamp_Vth_superposition_list.append(timestamp_Vth_superposition)
        features = {'Vth': Vth_list, 'ISI': ISI, 'label': None}
        self.data['All'] = {'features': features,
                             'voltage': {'voltage': self.voltage,
                                         'V_superposition': V_superposition_list,
                                         'label': 'Membrane Voltage(mV)'},
                             'timestamp': {'timestamp_Vth': timestamp_Vth_list,
                                           'timestamp': self.timestamp,
                                           'timestamp_superposition': timestamp_superposition_list,
                                           'timestamp_Vth_superposition': timestamp_Vth_superposition_list,
                                           'label': 'time(ms)'}}

    def get_figure_set_origin(self):
        fig_1_1 = {
            '1': {'x': ('All', 'timestamp', 'timestamp_superposition'), 'y': ('All', 'voltage', 'V_superposition'),
                  'label': ''},
            '2': {'x': ('All', 'timestamp', 'timestamp_Vth_superposition'), 'y': ('All', 'features', 'Vth'),
                  'label': ''}}
        fig_1_2 = {
        }
        fig_2_1 = {
                   }
        fig_2_2 = {
                   }
        self.figure_set_origin = {(1, 1): fig_1_1, (1, 2): fig_1_2, (2, 1): fig_2_1, (2, 2): fig_2_2}
        if self.main_window.figure_set_curvature == None:
            self.main_window.figure_set_curvature = self.figure_set_origin.copy()
            self.figure_set = self.main_window.figure_set_curvature
        else:
            self.figure_set = self.main_window.figure_set_curvature


def peak_time(spike_flag, voltage, timestamp):
    """
    Calculate the peak voltage and corresponding time for each action potential (AP)  based on the voltage sequence
    and spike flag (where Vm=0 in a spike).
    """
    list_voltage_max = []
    list_index_voltage_max = []
    list_voltage_max_moment = []
    for j in range(len(spike_flag)):
        voltage_max = max(voltage[spike_flag[j][0]:spike_flag[j][1] + 1])
        index_voltage_max = list(voltage[spike_flag[j][0]:spike_flag[j][1] + 1]).index(voltage_max) + spike_flag[j][0]
        list_voltage_max.append(voltage_max)
        list_index_voltage_max.append(index_voltage_max)
        list_voltage_max_moment.append(timestamp[[index_voltage_max]])
    return list_voltage_max, list_voltage_max_moment, list_index_voltage_max


def calculate_all_ISI(list_voltage_max_moment, list_voltage_max):
    """
    Calculate ISI of all APs.
    """
    ISI_all = []
    for i in range(1, len(list_voltage_max_moment)):
        isi = float(list_voltage_max_moment[i] - list_voltage_max_moment[i - 1])
        ISI_all.append(isi)
    list_voltage_max.pop(0)
    return ISI_all, list_voltage_max


def calculate_extracted_AP_ISI(AP, list_voltage_max_moment, ISI_all, data_source, voltage_option=None):
    """
    Calculate the ISI for each extracted action potential (AP). If the first AP is extracted, its ISI is set to None.
    """
    list_voltage_max_moment.pop(0)
    AP_ISI = []
    for i in AP:
        voltage = get_voltage_from_AP_data(AP_data=AP, AP_name=i, data_source=data_source,
                                           voltage_option=voltage_option)
        timestamp = AP[i]['timestamp']['timestamp']
        timestamp_AP_voltage_max = timestamp[list(voltage).index(max(voltage))]
        if timestamp_AP_voltage_max in list_voltage_max_moment:
            order = list_voltage_max_moment.index(timestamp_AP_voltage_max)
            ISI = ISI_all[order]
            AP[i]['features']['ISI'] = ISI
            AP_ISI.append(ISI)
        else:
            AP_ISI.append(np.NAN)
    return AP_ISI
