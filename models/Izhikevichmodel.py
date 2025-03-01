import numpy as np


class Model:
    number_of_compartment = 1
    dynamic_variables = ['Vm', 'n']
    # initial_value = [-65.95295126, 0.00027717]  # n_V_half (half-activation voltage of n): -25mV
    initial_value = [-66.01707003, 0.00074349]    # n_V_half (half-activation voltage of n): -30mV
    # initial_value = [-66.17866888, 0.00195436]  # n_V_half (half-activation voltage of n): -35mV
    # initial_value = [-66.54826978, 0.00491932]  # n_V_half (half-activation voltage of n): -40mV

    c = 1.0

    Ena = 60
    Ek = -90

    tau = 1

    gk = 10
    gna = 20
    gl = 8
    m_V_half = -20
    # type I
    El = -80
    n_V_half = -30

    # type II
    # n_V_half = -45
    # El = -78

    @staticmethod
    def n_inf(Vm):
        return 1 / (1 + np.exp((Model.n_V_half - Vm) / 5))

    @staticmethod
    def m_inf(Vm):
        return 1 / (1 + np.exp((-20 - Vm) / 15))

    @staticmethod
    def Gna(Vm):
        return Model.gna * Model.m_inf(Vm)

    @staticmethod
    def Gk(n):
        return Model.gk * n

    @staticmethod
    def Gl():
        return Model.gl

    @staticmethod
    def Ina(Vm):
        return Model.Gna(Vm) * (Vm - Model.Ena)

    @staticmethod
    def Ik(Vm, n):
        return Model.Gk(n) * (Vm - Model.Ek)

    @staticmethod
    def Il(Vm):
        return Model.gl * (Vm - Model.El)

    @staticmethod
    def Inet(Vm, n):
        return Model.Il(Vm) + Model.Ina(Vm) + Model.Ik(Vm, n)

    @staticmethod
    def Function(t, y, dt, Istim):
        Vm = y[0]
        n = y[1]

        dy = np.zeros((2,))
        current_index = min(round(t / dt), len(Istim[0]) - 1)
        I = Istim[0][current_index - 1]

        dy[0] = (I - Model.Ina(Vm) - Model.Ik(Vm, n) - Model.Il(Vm)) / Model.c
        dy[1] = (Model.n_inf(Vm) - n) / Model.tau
        return dy
