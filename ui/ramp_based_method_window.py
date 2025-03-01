"""Class used to quantifying spike threshold using ramp stimulation-based method"""
import inspect
import logging
import time as current_time
import unicodeit
from PySide6.QtWidgets import QWidget, QMessageBox
from calculate_feature_window import CalculateFeatureWindow
from models.Stimulus import Stimulus
from ui.set_fig_window_Vth import SetFigWindowVth
from ui_ramp_based_method_window import Ui_RampMethodWindow
from utils.ode_solver import ODE_python_method, Euler_method, RK_method
from utils.plotting import Plotting
from utils.tools import *


class RampMethodWindow(QWidget, Ui_RampMethodWindow):
    def __init__(self, main_window):
        super().__init__()
        self.ParasOfFeaturesWindow = None
        self.features_option = {'<Vm>': 0, 'dV/dt': [None, 0]}
        self.result = {}
        self.data = {}
        self.plotting = None
        self.figure_set = None
        self.figure_set_origin = None
        self.setupUi(self)
        self.init_ui()
        self.signal_slot()
        self.main_window = main_window

    def init_ui(self):
        """
        Init the RampMethodWindow user interface
        """
        model_name_list = get_model_names()
        for i in model_name_list:
            self.comboBox_model_ramp.addItem(i.replace('model', ' ') + 'model')
        self.update_combobox_voltage_ramp()
        self.update_combobox_current_ramp()

    def signal_slot(self):
        """
        Connect particular signal to slot function
        """
        self.comboBox_model_ramp.currentIndexChanged.connect(self.update_combobox_voltage_ramp)
        self.comboBox_model_ramp.currentIndexChanged.connect(self.update_combobox_current_ramp)
        self.pushButton_run_ramp.clicked.connect(self.output_of_all_k)
        self.pushButton_set_paras_ramp.clicked.connect(self.show_features_window)

    def show_features_window(self):
        """Create a CalculateFeatureWindow object for calculating spike features"""
        if self.data == {}:
            msg_box = QMessageBox(QMessageBox.Information, 'Message', 'No spike data!')
            msg_box.exec()
        else:
            self.ParasOfFeaturesWindow = CalculateFeatureWindow(mainWindow=self.main_window, data=self.data,
                                                                features_option=self.features_option,
                                                                tableWidget=self.tableWidget_features_ramp, sender_name=
                                                                'Y')
            self.ParasOfFeaturesWindow.show()

    def update_combobox_current_ramp(self):
        """
        Update current stimulation names in 'Istim' drop-down list when different neuronal models are selected .
        For a two-compartment model, the current stimulation names for the soma and dendrite compartments are 'Is' and
        'Id', respectively. Different current stimulation names are used to apply stimuli to different compartments.
         """
        current_model_name = self.comboBox_model_ramp.currentText().replace(' model', 'model')
        number_of_compartment = get_model_attributes(current_model_name)['number_of_compartment']
        current_name_list = get_current_names(number_of_compartment)
        self.comboBox_stimulus_name_ramp.clear()
        add_item_to_combox(current_name_list, self.comboBox_stimulus_name_ramp)

    def update_combobox_voltage_ramp(self):
        """
        Similar to the 'update_combobox_current_ramp' function, this function is used to update voltage names (e.g., Vs,
        Vd) corresponding to different compartments.
        """
        current_model_name = self.comboBox_model_ramp.currentText().replace(' model', 'model')
        number_of_compartment = get_model_attributes(current_model_name)['number_of_compartment']
        voltage_name_list = get_voltage_names(number_of_compartment)
        self.comboBox_voltage_ramp.clear()
        add_item_to_combox(voltage_name_list, self.comboBox_voltage_ramp)

    def get_data_for_one_k(self, k):
        """Quantify spike threshold of one user-defined ramp slope. This function measure the threshold by applying a
        series of ramp currents. Keep increasing the stimulation duration until spike occurs, and ensure that the error
        of spike threshold is less than precision."""
        a = current_time.time()
        precision = self.doubleSpinBox_precision_ramp.value()
        dt = 1  # Step size for adjusting the ramp current duration
        time = 1
        timeline = self.doubleSpinBox_ramp_timeline.value()
        model_name = self.comboBox_model_ramp.currentText().replace(' model', 'model')
        compartment_num = get_model_attributes(model_name)['number_of_compartment']
        dynamic_variables = get_model_attributes(model_name)['dynamic_variables']
        voltage_option = self.comboBox_voltage_ramp.currentText()
        ode_option = self.comboBox_ramp_ode_option.currentText()
        ode_dt = self.doubleSpinBox_dt_ramp.value()
        stimulus_name = self.comboBox_stimulus_name_ramp.currentText()
        k = k

        # First while loop determines how long the ramp stimulus must be applied to fire the neuron.
        while not Spike(time=time, timeline=timeline, model_name=model_name, ode_option=ode_option, k=k, ode_dt=ode_dt,
                        stimulus_name=stimulus_name, voltage_option=voltage_option, compartment_num=compartment_num,
                        dynamic_variables=dynamic_variables):
            time = time + 5
        # Determine the exact time when the spike occurs (the last non-spike time and the first spike time).
        count = 1
        while True:
            while True:
                time_substract_dt = round(time - dt, get_decimal_digits(dt))
                spike = Spike(time=time_substract_dt, timeline=timeline, model_name=model_name, ode_option=ode_option,
                              k=k,
                              ode_dt=ode_dt, stimulus_name=stimulus_name, voltage_option=voltage_option,
                              compartment_num=compartment_num, dynamic_variables=dynamic_variables)
                if not spike:
                    logging.info(f'Critical spike time：{time} ms')
                    break
                else:
                    time = round(time - dt, get_decimal_digits(dt))
            time_substract_dt = round(time - dt, get_decimal_digits(dt))
            # Ensure the precision of the spike threshold

            V_time = V(time=time, timeline=timeline, model_name=model_name, ode_option=ode_option, k=k, ode_dt=ode_dt,
                       stimulus_name=stimulus_name, voltage_option=voltage_option, compartment_num=compartment_num,
                       dynamic_variables=dynamic_variables)
            V_time_substract_dt = V(time=time_substract_dt, timeline=timeline, model_name=model_name,
                                    ode_option=ode_option, k=k, ode_dt=ode_dt,
                                    stimulus_name=stimulus_name, voltage_option=voltage_option,
                                    compartment_num=compartment_num,
                                    dynamic_variables=dynamic_variables)
            logging.info('\n')
            logging.info(f'V_time_substract_dt: {V_time_substract_dt}', )
            logging.info(f'V_time: {V_time} time: {time}')
            logging.info(f'dt: {dt}')
            logging.info(f'ode_dt: {ode_dt}')

            if V_time - V_time_substract_dt < precision:
                break
            else:
                if count == 1:
                    # On the first iteration, no need to reduce dt, keep it as 1.
                    count += 1
                else:
                    count += 1
                    dt = dt / 10
                    logging.info(f'Reduced dt to: {dt}')
                    if ode_dt >= dt:
                        ode_dt = dt
                        # Due to the reduction of step size dt of ramp current, the step size ode_dt of solving ODE also
                        # need to decrease.
                        while True:
                            spike = Spike(time=time, timeline=timeline, model_name=model_name,
                                          ode_option=ode_option,
                                          k=k,
                                          ode_dt=ode_dt, stimulus_name=stimulus_name, voltage_option=voltage_option,
                                          compartment_num=compartment_num, dynamic_variables=dynamic_variables)
                            if spike:
                                logging.info('spike at {} time'.format(time))
                                break
                            else:
                                time = round(time + dt * 10, get_decimal_digits(dt * 10))
        b = current_time.time()
        logging.info(f'k={k}, Spike threshold quantification time: {b - a} seconds')
        return {'time': time, 'ode_dt': ode_dt, 'dt': dt}

    def get_data_for_all_k(self):
        """Quantify spike thresholds of all user-defined slopes, and get their related spike data"""
        k_str = self.lineEdit_k_ramp.text()
        k_str = split_str_to_num(k_str)
        result = {}
        for i in range(len(k_str)):
            self.result[k_str[i]] = self.get_data_for_one_k(k_str[i])
            result[k_str[i]] = self.result[k_str[i]]['time']
        logging.info(result)
        return result

    def output_of_all_k(self):
        """Quantify spike threshold using ramp stimulation-based method, and store all related spike data"""
        self.result = {}
        self.data = {}
        self.plotting = None
        self.figure_set = None
        self.figure_set_origin = None
        a = current_time.time()
        result = self.get_data_for_all_k()
        timeline = self.doubleSpinBox_ramp_timeline.value()
        model_name = self.comboBox_model_ramp.currentText().replace(' model', 'model')
        compartment_num = get_model_attributes(model_name)['number_of_compartment']
        dynamic_variables = get_model_attributes(model_name)['dynamic_variables']
        voltage_option = self.comboBox_voltage_ramp.currentText()
        ode_option = self.comboBox_ramp_ode_option.currentText()
        stimulus_name = self.comboBox_stimulus_name_ramp.currentText()
        for i in result:
            name = 'k={}'.format(float(i))
            time = result[i]
            dt = self.result[i]['dt']
            ode_dt = self.result[i]['ode_dt']
            self.data[name] = output_of_one_k(time=time, timeline=timeline, model_name=model_name,
                                              ode_option=ode_option, k=float(i), dt=dt, ode_dt=ode_dt,
                                              stimulus_name=stimulus_name, compartment_num=compartment_num,
                                              voltage_option=voltage_option, dynamic_variables=dynamic_variables)
        Vth_list = []
        time_vth_list = []
        for i in self.data:
            if i == 'All':
                pass
            else:
                Vth_list.append(self.data[i]['features']['Vth'])
                time_vth_list.append(self.data[i]['timestamp']['timestamp_Vth'])
        logging.info(f"Spike threshold:{Vth_list}")

        self.data['All'] = {'features': {'Vth': Vth_list},
                            'timestamp': {'timestamp_Vth': time_vth_list}}
        # rate of depolarization dV/dt
        dv_dt_list = []
        for i in self.data:
            if i == 'All':
                pass
            else:
                dv_dt = self.data[i]['features']['dV/dt']

                dv_dt_list.append(dv_dt)
        self.data['All']['features']['dV/dt'] = dv_dt_list

        self.get_figure_set_origin()
        b = current_time.time()
        logging.info(f"Total time: {b - a} seconds")

        self.main_window.add_features_to_TableWidget(tableWidget_features=self.tableWidget_features_ramp,
                                                     data=self.data)
        if self.data:
            if 'Vth' in self.data['All']['features'].keys():
                Vth_list = self.data['All']['features']['Vth']
                Vth_max = round(max(Vth_list), 3)
                Vth_min = round(min(Vth_list), 3)
                Vth_mean = round(np.mean(Vth_list), 3)
                Vth_stand_deviation = round(np.std(Vth_list), 3)
                self.main_window.lineEdit_SD_Vth.setText(str(Vth_stand_deviation))
                self.main_window.lineEdit_mean_Vth.setText(str(Vth_mean))
                self.main_window.lineEdit_maximum_Vth.setText(str(Vth_max))
                self.main_window.lineEdit_minimum_Vth.setText(str(Vth_min))

        self.plotting = Plotting(data=self.data, figure_set=self.figure_set, axes=self.main_window.names['axes_Vth'])
        self.main_window.names['Canvas_Vth'].draw()
        if 'SetFigWindow_ramp' in self.main_window.names_window:
            self.main_window.names_window['SetFigWindow_ramp'].close()

            if 'SetFigWindow_ramp' in self.main_window.names_window:
                self.main_window.names_window['SetFigWindow_ramp'].deleteLater()
                self.main_window.names_window.pop('SetFigWindow_ramp')
            self.main_window.names_window['SetFigWindow_ramp'] = SetFigWindowVth(
                data_operation_module=self,
                main_window=self)
            self.main_window.names_window['SetFigWindow_ramp'].show()

    def get_figure_set_origin(self):
        fig_1_1 = {}
        fig_1_2 = {}
        fig_2_1 = {}
        fig_2_2 = {}
        voltage_option = self.comboBox_voltage_ramp.currentText()
        k_str = self.lineEdit_k_ramp.text()
        k_str = split_str_to_num(k_str)

        for i in range(len(k_str)):
            fig_1_1['{}'.format(i + 1)] = {'x': ('k={}'.format(k_str[i]), 'timestamp', 'timestamp'),
                                           'y': ('k={}'.format(k_str[i]), 'voltage',
                                                 '{}'.format(voltage_option)), 'label': ''}
            fig_2_1['{}'.format(i + 1)] = {'x': ('k={}'.format(k_str[i]), 'timestamp', 'timestamp'),
                                           'y': ('k={}'.format(k_str[i]), 'Istim',
                                                 '{}'.format(self.comboBox_stimulus_name_ramp.currentText())),
                                           'label': ''}
        num = len(fig_1_1)
        fig_1_1['{}'.format(num + 1)] = {'x': ('All', 'timestamp', 'timestamp_Vth'),
                                         'y': ('All', 'features', 'Vth'), 'label': 'Vth'}
        self.figure_set_origin = {(1, 1): fig_1_1, (1, 2): fig_1_2, (2, 1): fig_2_1, (2, 2): fig_2_2}
        if self.main_window.figure_set_ramp == None:
            self.main_window.figure_set_ramp = self.figure_set_origin.copy()
            self.figure_set = self.main_window.figure_set_ramp
        else:
            self.main_window.figure_set_ramp[(1, 1)] = self.figure_set_origin[(1, 1)]
            self.main_window.figure_set_ramp[(2, 1)] = self.figure_set_origin[(2, 1)]
            self.figure_set = self.main_window.figure_set_ramp


def get_voltage_name(compartment_num):
    if compartment_num == 1:
        return ['Vm']
    elif compartment_num == 2:
        return ['Vs', 'Vd']
    else:
        name_list = []
        for i in range(compartment_num):
            name = 'V' + '{}'.format(i + 1)
            name_list.append(name)
        return name_list


def output_of_one_k(time, timeline, model_name, ode_option, k, dt, ode_dt, stimulus_name, compartment_num,
                    voltage_option,
                    dynamic_variables):
    data = {}
    t = np.round(np.linspace(0, timeline, int(timeline / ode_dt) + 1), decimals=get_decimal_digits(ode_dt))
    model = importlib.import_module(model_name).Model
    Function = model.Function

    initial_value = model.initial_value

    Istim = get_stimulus(stop=time, k=k, stimulus_name=stimulus_name, t=t,
                         compartment_num=compartment_num)
    if ode_option == 'Euler':
        solution = Euler_method(t, ode_dt, Istim, initial_value, Function)
    if ode_option == 'odeint':
        solution = ODE_python_method(t, ode_dt, initial_value, Function,
                                     Istim=Istim)
    if ode_option == 'Runge-Kutta 45':
        solution = RK_method(t, ode_dt, initial_value, Function,
                             Istim=Istim)
    dynamic_variables_values = {}
    flag = 0

    for i in dynamic_variables:
        dynamic_variables_values[i] = solution[:, flag]
        flag += 1
    Vth_index = int(round(time / ode_dt, 0))
    Vth = dynamic_variables_values[voltage_option][Vth_index]
    logging.info('Index is {}'.format(Vth_index))
    logging.info('Spike time：{}'.format(time))
    logging.info('Spike threshold：{}'.format(Vth))
    dv_dt = get_rate_of_depolarization(V=dynamic_variables_values[voltage_option], time=time, ode_dt=ode_dt)
    average_voltage = get_average_voltage(V=dynamic_variables_values[voltage_option], time=time, ode_dt=ode_dt)
    methodlist = [(methodname, methon) for methodname, methon in
                  inspect.getmembers(model, inspect.isfunction)]
    methoddict = {}
    for i in methodlist:
        methoddict[i[0]] = i[1]
    method_Ionic_cuttent_list = {}
    for i in methoddict:
        if 'I' in i:
            method_Ionic_cuttent_list[i] = methoddict[i]
    method_conductance_list = {}
    for j in methoddict:
        if 'G' in j:
            method_conductance_list[j] = methoddict[j]

    subdata_current = {}
    for i in method_Ionic_cuttent_list:
        try:
            args = method_Ionic_cuttent_list[i].__code__.co_varnames
            kargs = {}
            for j in range(len(args)):
                kargs[args[j]] = dynamic_variables_values[args[j]]
            subdata_current[i] = method_Ionic_cuttent_list[i](**kargs)
        except:
            pass

    subdata_conductance = {}
    for i in method_conductance_list:
        try:
            args = method_conductance_list[i].__code__.co_varnames
            kargs = {}
            for j in range(len(args)):
                kargs[args[j]] = dynamic_variables_values[args[j]]
            if len(method_conductance_list[i](**kargs)) == len(t):
                subdata_conductance[i] = method_conductance_list[i](**kargs)
        except:
            pass

    subdata_timeline = {'timestamp': t, 'timestamp_Vth': time}

    subdata_state = {}
    for i in dynamic_variables_values:
        if 'V' in i:
            pass
        else:
            subdata_state[i] = dynamic_variables_values[i]

    subdata_stim = Istim

    subdata_voltage = {}
    for i in dynamic_variables_values:
        if 'V' in i:
            subdata_voltage[i] = dynamic_variables_values[i]

    subdata_derivative_voltage = {}
    for i in get_voltage_name(compartment_num):
        dvdt1 = np.diff(dynamic_variables_values[i]) / ode_dt
        dvdt2 = np.diff(dvdt1) / ode_dt
        dvdt3 = np.diff(dvdt2) / ode_dt
        subdata_derivative_voltage[unicodeit.replace('d{}/dt'.format(i))] = np.append(np.full(1, np.NAN), dvdt1)
        subdata_derivative_voltage[unicodeit.replace('d^2{}/dt^2'.format(i))] = np.append(np.full(2, np.NAN), dvdt2)
        subdata_derivative_voltage[unicodeit.replace('d^3{}/dt^3'.format(i))] = np.append(np.full(3, np.NAN), dvdt3)
    data['timestamp'] = subdata_timeline
    data['voltage'] = subdata_voltage
    if subdata_state != {}:
        data['state'] = subdata_state
    data['conductance'] = subdata_conductance
    if subdata_current != {}:
        data['ionic_current'] = subdata_current
    data['derivative voltage'] = subdata_derivative_voltage
    if subdata_stim != []:
        values = {}
        stimulus_name = []
        if compartment_num == 1:
            stimulus_name = ['Istim']
        elif compartment_num == 2:
            stimulus_name = ['Is', 'Id']
        else:
            for i in range(compartment_num):
                name = 'Istim' + '{}'.format(i + 1)
                stimulus_name.append(name)
        for i in range(len(stimulus_name)):
            values[stimulus_name[i]] = Istim[i]
        data['Istim'] = values
    data['features'] = {'Vth': Vth, 'dV/dt': dv_dt, '<V>': average_voltage}
    return data


def V(time, timeline, model_name, ode_option, k, ode_dt, stimulus_name, compartment_num, voltage_option,
      dynamic_variables):
    """
    Simulate biophysical model under a particular ramp stimulation.
    """
    t = np.round(np.linspace(0, timeline, int(timeline / ode_dt) + 1), decimals=get_decimal_digits(ode_dt))
    model = importlib.import_module(model_name).Model
    Function = model.Function

    initial_value = model.initial_value
    Istim = get_stimulus(stop=time, k=k, stimulus_name=stimulus_name, t=t, compartment_num=compartment_num)
    if ode_option == 'euler':
        solution = Euler_method(t, ode_dt, Istim, initial_value, Function)
    if ode_option == 'odeint':
        solution = ODE_python_method(t, ode_dt, initial_value, Function,
                                     Istim=Istim)
    if ode_option == 'rk45':
        solution = RK_method(t, ode_dt, initial_value, Function,
                             Istim=Istim)
    dynamic_variables_values = {}
    flag = 0

    for i in dynamic_variables:
        dynamic_variables_values[i] = solution[:, flag]
        flag += 1
    index = int(time / ode_dt)

    return dynamic_variables_values[voltage_option][index]


def Spike(time, timeline, model_name, ode_option, k, ode_dt, stimulus_name, compartment_num, voltage_option,
          dynamic_variables):
    """
    Apply a ramp current and check if a spike occurs in voltage trace.
    """
    # Get ramp stimulation sequence and run simulation.
    t = np.round(np.linspace(0, timeline, int(timeline / ode_dt) + 1), decimals=get_decimal_digits(ode_dt))
    model = importlib.import_module(model_name).Model
    Function = model.Function

    initial_value = model.initial_value
    Istim = get_stimulus(stop=time, k=k, stimulus_name=stimulus_name, t=t, compartment_num=compartment_num)
    if ode_option == 'euler':
        solution = Euler_method(t, ode_dt, Istim, initial_value, Function)
    if ode_option == 'odeint':
        solution = ODE_python_method(t, ode_dt, initial_value, Function,
                                     Istim=Istim)
    if ode_option == 'rk45':
        solution = RK_method(t, ode_dt, initial_value, Function,
                             Istim=Istim)
    dynamic_variables_values = {}
    flag = 0

    for i in dynamic_variables:
        dynamic_variables_values[i] = solution[:, flag]
        flag += 1
    logging.info('Detect if the ramp current of {} ms induces a spike'.format(time))
    # Identify a spike when V > 0 mV.
    if (dynamic_variables_values[voltage_option] > 0).any():
        logging.info('Spike occurs')
        return True
    else:
        logging.info('No spike occurs.')
        return False


def get_rate_of_depolarization(V, time, ode_dt):
    """
    Calculate rate of depolarization (dV/dt) preceding to spike. In this function, the dV/dt is the slope of membrane
    voltage from the ramp onset to offset.
    """
    V_on = V[0]
    index_stimulus_off = int(time / ode_dt)
    V_off = V[index_stimulus_off]
    dv_dt = (V_off - V_on) / time
    return dv_dt


def get_average_voltage(V, time, ode_dt):
    """
    Calculate average membrane voltage (<V>) over a time period
    """
    index_stimulus_off = int(time / ode_dt)
    average_voltage = np.mean(V[0:index_stimulus_off])
    return average_voltage


def get_stimulus(stop, k, stimulus_name, t, compartment_num):
    stimulus = {}
    name_list = get_current_names(compartment_num)

    for i in name_list:
        stimulus[i] = None
    for i in stimulus:
        stimulus[i] = Stimulus(t)
    current_type = 'ramp'
    stimulus[stimulus_name].add_current(current_type=current_type, start_time=0, end_time=stop,
                                        k=k)
    for i in stimulus:
        stimulus[i].get_current()
        stimulus[i] = stimulus[i].All_currents_values
    stimulus = [stimulus[i] for i in stimulus]
    return stimulus
