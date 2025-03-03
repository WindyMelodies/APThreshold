"""Class for solving ordinary differential equations (ODEs).
Here, we provide three ODE solver: euler method, fourth-order to fifth-order Runge-Kutta method, and odeint function
from the SciPy library of Python"""
import logging
# -*- coding: UTF-8 -*
import time
from utils.tools import *
import unicodeit
import copy
import importlib
import inspect
import os
import sys
import numpy as np
from scipy.integrate import odeint, solve_ivp
from models.Stimulus import Stimulus


def Euler_method(t, dt, Istim, initial_value, Function):
    """
    Solve ODEs using the Euler method.

    Returns
    -------
    sol : ndarray
        Array of shape (len(t), len(initial_value)) containing the solution to the ODEs.
        The solution can be accessed by 'Vm=sol[:,0]', where `Vm` represents the neuron’s membrane potential.

    """
    sol = np.full((len(t), len(initial_value)), initial_value)
    for i in range(len(t)):
        if i == 0:
            pass
        else:
            if i == 1:
                y_pre = sol[0, :]
            else:
                y_pre = sol[i - 1, :]
            dydt = Function(t[i - 1], y_pre, dt, Istim)
            y = dydt * dt + y_pre
            sol[i] = y
    return sol


def ODE_python_method(t, dt, initial_value, Function, **kwargs):
    """Solve ODEs using the `odeint` solver from SciPy."""
    sol = odeint(Function, y0=initial_value, t=t, tfirst=True, args=(dt, kwargs['Istim']))
    return sol


def RK_method(t, dt, initial_value, Function, **kwargs):
    """Solve ODEs using the Runge-Kutta 45 (RK45) method from SciPy."""
    sol = solve_ivp(Function, t_span=[min(t), max(t)], y0=initial_value, method='RK45', t_eval=t,
                    args=(dt, kwargs['Istim']))
    return sol.y.T


class Model:
    """
    A class for simulation neuronal biophysical neuronal models.
    This class performs the following tasks:
    1. Load the target neuron model.
    2. Solve the neuron model using specified ODE solvers.
    3. Compute the current and conductance data for the neuron model.
    4. Organize the results into a dictionary for storage and further analysis.
    """
    flag = 'ap'
    sys.path.append(os.path.join(os.path.abspath('.'), 'models'))
    labels = {'voltage': 'Membrane voltage(mV)', 'derivative voltage': '', 'ionic_current': 'Current(μA/cm^2)',
              'state': '', 'conductance': 'Conductance(mS/cm^2', 'Istim': 'Applied current(μA/cm^2)',
              'timestamp': 'Time(ms)'
              }
    datatypes = ['voltage', 'derivative voltage', 'state', 'ionic_current', 'conductance', 'Istim', 'timestamp']

    def __init__(self, main_window):
        """
        Initializes the Model class by loading the neuron model and setting up necessary parameters.
        """
        self.dt = None
        self.main_window = main_window
        self.subdata_conductance = None
        self.dynamic_variables_values = None
        self.subdata_current = None
        # Load the selected neuron model
        self.model_name = self.main_window.comboBox_model.currentText().replace(' model', 'model')

        self.ode_option = self.main_window.comboBox_ode_option.currentText()
        # Import the selected model module
        self.model = importlib.import_module(self.model_name)
        # Get model parameters
        self.initial_value = self.model.Model.initial_value
        self.Function = self.model.Model.Function

        self.dynamic_variables = self.model.Model.dynamic_variables
        self.compartment_num = self.model.Model.number_of_compartment
        # Initialize lists and data structures for storing simulation results
        self.method_conductance_list = None
        self.method_Ionic_cuttent_list = None
        self.data = {}
        # Record the simulation time and run simulation
        a = time.time()
        self.output()
        self.get_methods()
        self.GetOtherValues()
        b = time.time()
        logging.info('*' * 8)
        logging.info('Data calculation time: {:.2f} seconds'.format(b - a))
        self.get_data()

        self.figure_set = None
        self.figure_set_origin = None
        self.get_figure_set_origin()

    @staticmethod
    def get_stimulus(main_window, t, compartment_num):
        """Generate current stimulation that is applied to the selected neuronal model"""
        stimulus = {}
        if compartment_num == 1:
            name_list = ['Istim']
        elif compartment_num == 2:
            name_list = ['Is', 'Id']
        else:
            name_list = []
            for i in range(compartment_num):
                name = 'Istim' + '{}'.format(i + 1)
                name_list.append(name)
        for i in name_list:
            stimulus[i] = None
        for i in stimulus:
            stimulus[i] = Stimulus(t)
        for i in range(main_window.tabWidget_stimulus.count()):
            index_current_stim = main_window.tabWidget_stimulus.widget(i).objectName().strip('tab_stim')
            tab_name = 'stim' + index_current_stim
            stimulus_name = main_window.names['comboBox_' + tab_name + '_name'].currentText()
            start_time = main_window.names['doubleSpinBox_' + tab_name + '_start'].value()
            end_time = main_window.names['doubleSpinBox_' + tab_name + '_stop'].value()

            if main_window.names['comboBox_' + tab_name].currentText() == 'DC':
                current_type = 'step'
                amplitude = main_window.names['doubleSpinBox_' + tab_name + '_amplitude'].value()
                stimulus[stimulus_name].add_current(current_type=current_type, start_time=start_time, end_time=end_time,
                                                    amplitude=amplitude)
            elif main_window.names['comboBox_' + tab_name].currentText() == 'AC':
                current_type = 'sine'
                amplitude = main_window.names['doubleSpinBox_' + tab_name + '_amplitude'].value()
                f = main_window.names['spinBox_' + tab_name + '_frequency'].value()
                stimulus[stimulus_name].add_current(current_type=current_type, start_time=start_time, end_time=end_time,
                                                    amplitude=amplitude,
                                                    f=f)
            elif main_window.names['comboBox_' + tab_name].currentText() == 'Ramp':
                current_type = 'ramp'
                k = main_window.names['doubleSpinBox_' + tab_name + '_K'].value()
                stimulus[stimulus_name].add_current(current_type=current_type, start_time=start_time, end_time=end_time,
                                                    k=k)
            elif main_window.names['comboBox_' + tab_name].currentText() == 'OU process':
                current_type = 'noise'
                mu = main_window.names['doubleSpinBox_' + tab_name + '_mu'].value()
                theta = main_window.names['doubleSpinBox_' + tab_name + '_theta'].value()
                sigma = main_window.names['doubleSpinBox_' + tab_name + '_sigma'].value()
                stimulus[stimulus_name].add_current(current_type=current_type, start_time=start_time, end_time=end_time,
                                                    mu=mu,
                                                    sigma=sigma,
                                                    theta=theta)
        stimulus_paras = {}
        for i in name_list:
            stimulus_paras[i] = stimulus[i].currents
        for i in stimulus:
            stimulus[i].get_current()
            stimulus[i] = stimulus[i].All_currents_values
        stimulus = [stimulus[i] for i in stimulus]
        return stimulus, stimulus_paras

    def output(self):
        """
        Run simulation
        """
        self.timestamp = self.main_window.spinBox_timeline.value()
        self.dt = self.main_window.doubleSpinBox_dt.value()
        self.t = np.round(np.linspace(0, self.timestamp, int(self.timestamp / self.dt) + 1),
                          get_decimal_digits(self.dt))
        self.t = round_timestamp(self.t, self.dt)
        self.Istim = self.get_stimulus(self.main_window, self.t, self.compartment_num)[0]

        if self.ode_option == 'Euler':
            self.solution = Euler_method(self.t, self.dt, self.Istim, self.initial_value, self.Function)
        if self.ode_option == 'Odeint':
            self.solution = ODE_python_method(self.t, self.dt, self.initial_value, self.Function,
                                              Istim=self.Istim)
        if self.ode_option == 'Runge-Kutta 45':
            self.solution = RK_method(self.t, self.dt, self.initial_value, self.Function,
                                      Istim=self.Istim)
        dynamic_variables_values = {}
        flag = 0
        for i in self.dynamic_variables:
            dynamic_variables_values[i] = self.solution[:, flag]
            flag += 1
        self.dynamic_variables_values = dynamic_variables_values

    def get_methods(self):
        """
        Retrieve the methods from the neuron model class for calculating spike data.

        This method performs the following steps:
        1. Retrieves all methods from the neuron model class.
        2. Extracts methods related to ionic current calculations.
        3. Extracts methods related to ionic conductance calculations.
        """
        methodlist = [(methodname, methon) for methodname, methon in
                      inspect.getmembers(self.model.Model, inspect.isfunction)]
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
        self.method_conductance_list = method_conductance_list
        self.method_Ionic_cuttent_list = method_Ionic_cuttent_list

    def GetOtherValues(self):
        # Get ionic currents
        self.subdata_current = {}
        for i in self.method_Ionic_cuttent_list:
            try:
                args = self.method_Ionic_cuttent_list[i].__code__.co_varnames
                kargs = {}
                for j in range(len(args)):
                    kargs[args[j]] = self.dynamic_variables_values[args[j]]
                self.subdata_current[i] = self.method_Ionic_cuttent_list[i](**kargs)
            except:
                pass
        # Get ionic conductances
        self.subdata_conductance = {}
        for i in self.method_conductance_list:
            try:
                args = self.method_conductance_list[i].__code__.co_varnames
                kargs = {}
                for j in range(len(args)):
                    kargs[args[j]] = self.dynamic_variables_values[args[j]]
                if len(self.method_conductance_list[i](**kargs)) == len(self.t):
                    self.subdata_conductance[i] = self.method_conductance_list[i](**kargs)
            except:
                pass

        # Get timestamp
        self.subdata_timestamp = {'timestamp': self.t}

        # Get gating variables
        self.subdata_state = {}
        for i in self.dynamic_variables_values:
            if 'V' in i:
                pass
            else:
                self.subdata_state[i] = self.dynamic_variables_values[i]
        # Get stimulus current
        self.subdata_stim = self.Istim
        # Get membrane voltage
        self.subdata_voltage = {}
        for i in self.dynamic_variables_values:
            if 'V' in i:
                self.subdata_voltage[i] = self.dynamic_variables_values[i]
                logging.info(f"Average voltage: {np.average(self.dynamic_variables_values[i])}")

        # Get derivative of membrane voltage (first, second, and third derivatives)
        self.subdata_derivative_voltage = {}
        for i in self.get_voltage_name(self.compartment_num):
            dvdt1 = np.diff(self.dynamic_variables_values[i]) / self.dt
            dvdt2 = np.diff(dvdt1) / self.dt
            dvdt3 = np.diff(dvdt2) / self.dt
            self.subdata_derivative_voltage[unicodeit.replace('d{}/dt'.format(i))] = np.append(np.full(1,
                                                                                                       np.nan), dvdt1)
            self.subdata_derivative_voltage[unicodeit.replace('d^2{}/dt^2'.format(i))] = np.append(
                np.full(2, np.nan), dvdt2)
            self.subdata_derivative_voltage[unicodeit.replace('d^3{}/dt^3'.format(i))] = np.append(
                np.full(3, np.nan), dvdt3)

    @staticmethod
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

    @staticmethod
    def get_current_name(compartment_num):
        if compartment_num == 1:
            return ['Istim']
        elif compartment_num == 2:
            return ['Is', 'Id']
        else:
            name_list = []
            for i in range(compartment_num):
                name = 'I' + '{}'.format(i + 1)
                name_list.append(name)
            return name_list

    def get_data(self):
        """Store all spike data"""
        self.data['timestamp'] = self.subdata_timestamp
        self.data['voltage'] = self.subdata_voltage
        if self.subdata_state != {}:
            self.data['state'] = self.subdata_state
        self.data['conductance'] = self.subdata_conductance
        if self.subdata_current != {}:
            self.data['ionic_current'] = self.subdata_current
        self.data['derivative voltage'] = self.subdata_derivative_voltage
        if self.subdata_stim != []:
            values = {}
            stimulus_name = []
            if self.compartment_num == 1:
                stimulus_name = ['Istim']
            elif self.compartment_num == 2:
                stimulus_name = ['Is', 'Id']
            else:
                for i in range(self.compartment_num):
                    name = 'Istim' + '{}'.format(i + 1)
                    stimulus_name.append(name)
            for i in range(len(stimulus_name)):
                values[stimulus_name[i]] = self.Istim[i]
            self.data['Istim'] = values
        for i in self.data:
            self.data[i]['label'] = self.labels[i]
        return self.data

    def get_figure_set_origin(self):
        """Define the original figure set for plotting neuron model data"""
        self.figure_set_origin = {}
        fig_1_1 = {'1': {'x': ('timestamp', 'timestamp'), 'y': ('voltage', 'Vm'), 'label': ''}}
        fig_1_2 = {}
        fig_2_1 = {}
        fig_2_2 = {}
        self.figure_set_origin = {(1, 1): fig_1_1, (1, 2): fig_1_2, (2, 1): fig_2_1, (2, 2): fig_2_2}
        if self.main_window.figure_set_simulation == None:
            self.main_window.figure_set_simulation = copy.deepcopy(self.figure_set_origin)
            self.figure_set = self.main_window.figure_set_simulation
        else:
            self.figure_set = self.main_window.figure_set_simulation
