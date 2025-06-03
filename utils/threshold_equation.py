import numpy as np


class FormOne:
    params = {'ka': None, 'ki': None, 'VT': None, 'Vi': None}

    @staticmethod
    def theta(**kwargs):
        ka = kwargs['ka']
        ki = kwargs['ki']
        VT = kwargs['VT']
        Vi = kwargs["Vi"]

    @staticmethod
    def theta_inf(**kwargs):
        ka = kwargs['ka']
        ki = kwargs['ki']
        Vi = kwargs["Vi"]

    @staticmethod
    def tau_theta():
        pass

    @staticmethod
    def alpha_h():
        pass

    @staticmethod
    def beta_h():
        pass


class FormTwo:
    params = {'ka', 'ki', 'VT', 'Vi'}
