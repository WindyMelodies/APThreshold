import numpy as np


class Model:
    number_of_compartment = 1
    dynamic_variables = ['Vm', 'n']
    # [-69.39276118, 1.26410023e-05]: initial_value for excitability type II
    initial_value = [-69.39276118, 1.26410023e-05]
    c = 2
    Bm = -1.2
    Bn = -13  # Excitability: 0mV (type I), -13mV (type I), -21mV (type I)
    Am = 18
    An = 10
    fi = 0.15
    gna = 20
    gk = 20
    gl = 2
    Ena = 50
    Ek = -100
    El = -70

    @staticmethod
    def m_inf(Vm):
        return 0.5 * (1 + np.tanh((Vm - Model.Bm) / Model.Am))

    @staticmethod
    def n_inf(Vm):
        return 0.5 * (1 + np.tanh((Vm - Model.Bn) / Model.An))

    @staticmethod
    def tau_n(Vm):
        return 1 / np.cosh((Vm - Model.Bn) / (2 * Model.An))

    @staticmethod
    def Ina(Vm):
        return Model.gna * Model.m_inf(Vm) * (Vm - Model.Ena)

    @staticmethod
    def Ik(Vm, n):
        return Model.gk * n * (Vm - Model.Ek)

    @staticmethod
    def Il(Vm):
        return Model.gl * (Vm - Model.El)

    @staticmethod
    def Inet(Vm, n):
        return Model.Il(Vm) + Model.Ik(Vm, n) + Model.Ina(Vm)

    @staticmethod
    def Gna(Vm):
        return Model.gna * Model.m_inf(Vm)

    @staticmethod
    def Gk(n):
        return Model.gk * n

    @staticmethod
    def Function(t, y, dt, Istim):
        Vm = y[0]
        n = y[1]

        dy = np.zeros((2,))
        current_index = min(int(round(t / dt, 0)), len(Istim[0]) - 1)
        I = Istim[0][current_index]

        dy[0] = (I - Model.Ina(Vm) - Model.Ik(Vm, n) - Model.Il(Vm)) / Model.c
        dy[1] = Model.fi * (Model.n_inf(Vm) - n) / Model.tau_n(Vm)
        return dy
