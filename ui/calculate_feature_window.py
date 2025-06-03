"""
Class for calculating features of spike threshold dynamics, which include the depolarization rate (dV/dt) and average
membrane voltage (<Vm>) of action potentials, based on user-defined options.
"""
import logging
import numpy as np
import unicodeit
from PySide6.QtWidgets import QWidget
from ui import Ui_Form_paras_of_features
from utils.condition_check import data_source_check
from utils.tools import get_AP_or_K_names


class CalculateFeatureWindow(QWidget, Ui_Form_paras_of_features):

    def __init__(self, mainWindow, data, features_option, tableWidget, sender_name=None):
        """
        Initializes the feature calculation window
        """
        super().__init__()
        self.setupUi(self)
        self.option = features_option
        self.MainWindow = mainWindow
        self.data_source = None
        self.voltage_option = None
        self.tableWidget = tableWidget
        self.data = data
        self.set_slot_func()
        if sender_name:
            # For ramp stimulation-based method
            self.data_source = 'simulation'
            self.voltage_option = self.MainWindow.rampMethod_window.comboBox_voltage_ramp.currentText()
            self.dt = self.MainWindow.rampMethod_window.doubleSpinBox_dt_ramp.value()
        else:
            # For waveform curvature-based method
            self.data_source, self.voltage_option, _, self.dt = data_source_check(self.MainWindow)

    def set_slot_func(self):
        self.pushButton_save.clicked.connect(self.calculate_clicked)
        self.pushButton_canel.clicked.connect(self.cancel_clicked)

    def calculate_clicked(self):
        """
        The function is triggered when the "Calculate" button is clicked.
        It collects input parameters and calculates the features.
        """
        self.close()
        time_period_Vm = self.doubleSpinBox_time_average_Vm.value()
        time_period_dvdt = self.doubleSpinBox_time_dvdt.value()
        button_list = [self.radioButton_average_dvdt, self.radioButton_slope_two_points, self.radioButton_maximum]
        # Determine depolarization rate calculation method
        num = 1
        for i in button_list:
            if i.isChecked():
                self.option['dV/dt'][0] = num
                self.option['dV/dt'][1] = time_period_dvdt
                break
            num += 1
        self.option['<Vm>'] = time_period_Vm
        self.get_features()
        self.MainWindow.add_features_to_TableWidget(tableWidget_features=self.tableWidget, data=self.data)

    def get_features(self):
        """
        Calculate features: depolarization rate (dV/dt) and average membrane voltage (<Vm>) of action potentials,
        based on the selected options and store them in the data dictionary.
        """
        name_list = get_AP_or_K_names(self.data)
        logging.info('Option of feature calculation：{}'.format(self.option))
        # Calculate depolarization rate dV/dt
        if self.option['dV/dt'][0] is None or self.option['dV/dt'][1] == 0:
            pass
        else:
            time_period = self.option['dV/dt'][1]
            dVdt_list = []
            if self.option['dV/dt'][0] == 1:  # Average of dVm/dt over a time period

                for i in name_list:
                    spike_moment = self.data[i]['timestamp']['timestamp_Vth'][0]

                    timestamp = np.array(self.data[i]['timestamp']['timestamp'])
                    if self.data_source == 'simulation':
                        dVdt_1 = self.data[i]['derivative voltage'][
                            unicodeit.replace('d{}/dt'.format(self.voltage_option))]
                    else:
                        dVdt_1 = self.data[i]['voltage'][unicodeit.replace('dV/dt')]
                    dVdt = self.dVdt_average(spike_moment=spike_moment, timestamp=timestamp, time_period=time_period,
                                             dVdt_1=dVdt_1)
                    dVdt_list.append(dVdt)
                    self.data[i]['features']['dV/dt'] = [dVdt]
                    logging.info(f'{i} : {dVdt}')

            if self.option['dV/dt'][0] == 2:  # Slope of Vm within a time period

                for i in name_list:
                    spike_moment = self.data[i]['timestamp']['timestamp_Vth'][0]
                    timestamp = np.array(self.data[i]['timestamp']['timestamp'])
                    if self.data_source == 'simulation':
                        voltage = self.data[i]['voltage']['{}'.format(self.voltage_option)]
                    else:
                        voltage = self.data[i]['voltage']['voltage']
                    dVdt = self.dVdt_slope(spike_moment=spike_moment, timestamp=timestamp, time_period=time_period,
                                           voltage=voltage)
                    dVdt_list.append(dVdt)
                    self.data[i]['features']['dV/dt'] = [dVdt]
                    logging.info(f'{i} : {dVdt}')

            if self.option['dV/dt'][0] == 3:  # Maximum of dVm/dt during upstroke
                for i in name_list:
                    spike_moment = self.data[i]['timestamp']['timestamp_Vth'][0]
                    timestamp = np.array(self.data[i]['timestamp']['timestamp'])
                    if self.data_source == 'simulation':
                        dVdt_1 = self.data[i]['derivative voltage'][
                            unicodeit.replace('d{}/dt'.format(self.voltage_option))]
                        voltage = self.data[i]['voltage']['{}'.format(self.voltage_option)]
                    else:
                        dVdt_1 = self.data[i]['voltage'][unicodeit.replace('dV/dt')]
                        voltage = self.data[i]['voltage']['voltage']
                    dVdt = self.dVdt_max(spike_moment=spike_moment, timestamp=timestamp,
                                         dVdt_1=dVdt_1, voltage=voltage)
                    dVdt_list.append(dVdt)
                    self.data[i]['features']['dV/dt'] = [dVdt]
            self.data['All']['features']['dV/dt'] = dVdt_list

        # Calculate average membrane voltage <V>
        average_Vm_list = []
        if self.option['<Vm>'] == 0:
            pass
        else:
            time_period = self.option['<Vm>']
            for i in name_list:
                timestamp = np.array(self.data[i]['timestamp']['timestamp'])
                spike_moment = self.data[i]['timestamp']['timestamp_Vth'][0]
                if self.data_source == 'simulation':
                    voltage = self.data[i]['voltage']['{}'.format(self.voltage_option)]
                else:
                    voltage = self.data[i]['voltage']['voltage']
                average_V = self.average_V(spike_moment=spike_moment, time_period=time_period,
                                           timestamp=timestamp, voltage=voltage)
                average_Vm_list.append(average_V)
                self.data[i]['features']['<V>'] = [average_V]
            self.data['All']['features']['<V>'] = average_Vm_list

    def cancel_clicked(self):
        self.close()

    def show(self):
        super().show()
        self.doubleSpinBox_time_average_Vm.setValue(self.option['<Vm>'])
        if self.option['dV/dt'][0] == None:
            pass
        if self.option['dV/dt'][0] == 1:
            self.radioButton_average_dvdt.setChecked(True)
        if self.option['dV/dt'][0] == 2:
            self.radioButton_slope_two_points.setChecked(True)
        if self.option['dV/dt'][0] == 3:
            self.radioButton_maximum.setChecked(True)
        self.doubleSpinBox_time_dvdt.setValue(self.option['dV/dt'][1])

    @staticmethod
    def dVdt_average(spike_moment, timestamp, time_period, dVdt_1):
        start_index = np.abs(timestamp - (spike_moment - time_period)).argmin()
        stop_index = np.abs(timestamp - spike_moment).argmin()
        dvdt = dVdt_1[start_index:stop_index]
        dVdt_average = np.average(dvdt)
        return dVdt_average

    @staticmethod
    def dVdt_slope(spike_moment, timestamp, time_period, voltage):
        start_index = np.abs(timestamp - (spike_moment - time_period)).argmin()
        stop_index = np.abs(timestamp - spike_moment).argmin()
        dVdt_slope = (voltage[stop_index] - voltage[start_index]) / time_period
        return dVdt_slope

    @staticmethod
    def dVdt_max(spike_moment, timestamp, voltage, dVdt_1):
        voltage_max = np.max(voltage)
        index_voltage_max = np.where(abs(voltage - voltage_max) <= 10e-8)[0][0]
        index_upstroke_start = np.where(abs(timestamp - spike_moment) <= 10e-8)[0][0]
        index_upstroke_stop = index_voltage_max
        dVdt_max = max(dVdt_1[index_upstroke_start:index_upstroke_stop])
        return dVdt_max

    @staticmethod
    def average_V(spike_moment, time_period, timestamp, voltage):
        start_index = np.abs(timestamp - (spike_moment - time_period)).argmin()
        stop_index = np.abs(timestamp - spike_moment).argmin()
        average_V = np.average(voltage[start_index: stop_index])
        return average_V
