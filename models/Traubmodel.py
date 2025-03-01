import numpy as np


class Model:
    number_of_compartment = 1
    dynamic_variables = ['Vm', 'n', 'm', 'h', 'p']
    # initial_value = [-69.99517006, 0.01132227, 0.00329145, 0.99931825, 0.01059959]  # Vshift = -63
    initial_value = [-70.05254901, 0.05995339, 0.00324974, 0.99932816, 0.01135952]  # Vshift =-73
    c = 1
    El = -70
    Ena = 50
    Ek = -90
    gl = 0.045
    gna = 51.6
    gk = 10
    gm = 0  # 0.2-0.5
    Vshift = -63
    shift = -10  # -10

    @staticmethod
    def alpha_m(Vm):
        return -0.32 * (Vm - Model.Vshift - 13) / (np.exp(-(Vm - Model.Vshift - 13) / 4) - 1)

    @staticmethod
    def beta_m(Vm):
        return 0.28 * (Vm - Model.Vshift - 40) / (np.exp((Vm - Model.Vshift - 40) / 5) - 1)

    @staticmethod
    def alpha_h(Vm):
        return 0.128 * (np.exp(-(Vm - Model.Vshift - 17) / 18))

    @staticmethod
    def beta_h(Vm):
        return 4 / (1 + np.exp(-(Vm - Model.Vshift - 40) / 5))

    @staticmethod
    def alpha_n(Vm):
        return -0.032 * (Vm - Model.Vshift - Model.shift - 15) / (
                np.exp(-(Vm - Model.Vshift - Model.shift - 15) / 5) - 1)

    @staticmethod
    def beta_n(Vm):
        return 0.5 * np.exp(-(Vm - Model.Vshift - Model.shift - 10) / 40)

    @staticmethod
    def alpha_p(Vm):
        return 0.0001 * (Vm + 30) / (1 - np.exp(-(Vm + 30) / 9))

    @staticmethod
    def beta_p(Vm):
        return -0.0001 * (Vm + 30) / (1 - np.exp((Vm + 30) / 9))

    @staticmethod
    def Ina(Vm, m, h):
        return Model.gna * (m ** 3) * h * (Vm - Model.Ena)

    @staticmethod
    def Ik(Vm, n):
        return Model.gk * (n ** 4) * (Vm - Model.Ek)

    @staticmethod
    def Im(Vm, p):
        return Model.gm * p * (Vm - Model.Ek)

    @staticmethod
    def Il(Vm):
        return Model.gl * (Vm - Model.El)

    @staticmethod
    def Function(t, y, dt, Istim):
        Vm = y[0]
        n = y[1]
        m = y[2]
        h = y[3]
        p = y[4]

        dy = np.zeros((5,))
        current_index = min(round(t / dt), len(Istim[0]) - 1)
        I = Istim[0][current_index]

        dy[0] = (I - Model.Il(Vm) - Model.Ina(Vm, m, h) - Model.Ik(Vm, n) - Model.Im(Vm, p)) / Model.c
        dy[1] = Model.alpha_n(Vm) * (1 - n) - Model.beta_n(Vm) * n
        dy[2] = Model.alpha_m(Vm) * (1 - m) - Model.beta_m(Vm) * m
        dy[3] = Model.alpha_h(Vm) * (1 - h) - Model.beta_h(Vm) * h
        dy[4] = Model.alpha_p(Vm) * (1 - p) - Model.beta_p(Vm) * p
        return dy
