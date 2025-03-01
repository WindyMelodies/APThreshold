"""
Class for generating current stimulation of different types to activate biophysical models
"""
import math
import random
import numpy as np


class Stimulus:
    def __init__(self, t):
        self.All_currents_values = None
        self.t = t
        self.I_store_noise = None
        self.I_ramp_value = None
        self.I_sine_value = None
        self.I_step_value = None
        self.currents = []

    def add_current(self, current_type, start_time, end_time, amplitude=None, f=None, k=None, mu=0, theta=None,
                    sigma=None):
        current = {'current_type': current_type, 'start_time': start_time, 'end_time': end_time, 'amplitude': amplitude,
                   'f': f, 'k': k, 'mu': mu, 'theta': theta, 'sigma': sigma}
        self.currents.append(current)

    def get_current(self):
        self.All_currents_values = np.zeros_like(self.t)
        self.I_store_noise = np.zeros_like(self.t)

        for single_current in self.currents:
            start_time = single_current['start_time']
            end_time = single_current['end_time']
            A = single_current['amplitude'] if single_current['amplitude'] is not None else 0
            f = single_current['f'] if single_current['f'] is not None else 10
            k = single_current['k'] if single_current['k'] is not None else 0
            mu = single_current['mu'] if single_current['mu'] is not None else 0
            theta = single_current['theta'] if single_current['theta'] is not None else 0
            sigma = single_current['sigma'] if single_current['sigma'] is not None else 0
            for i in range(len(self.t)):
                if start_time <= self.t[i] <= end_time:
                    if single_current['current_type'] == 'step':
                        self.I_step_value = A
                        self.All_currents_values[i] += self.I_step_value
                    elif single_current['current_type'] == 'sine':
                        self.I_sine_value = A * math.sin(2 * math.pi * f * (self.t[i] - start_time) / 1000)
                        self.All_currents_values[i] += self.I_sine_value
                    elif single_current['current_type'] == 'ramp':
                        self.I_ramp_value = k * (self.t[i] - start_time)
                        self.All_currents_values[i] += self.I_ramp_value
                    elif single_current['current_type'] == 'noise':
                        dt = 0.01  # todo 1、dt 2、ode solver
                        self.I_store_noise[i] += self.I_store_noise[i - 1] + ((
                                mu - self.I_store_noise[i - 1]) /theta + sigma * random.gauss(0, 1)) *dt
                        self.All_currents_values[i] += self.I_store_noise[i]
                    else:
                        pass

