import numpy as np


class Model:
    number_of_compartment = 1
    dynamic_variables = ['Vm', 'n', 'm', 'h']
    # Set initial value of four dynamic variables of Hodgkin-Huxley model to their steady-state value corresponding to
    # V1/2(n)=-53.41mV
    initial_value = [-64.99972243, 0.31768117, 0.05293422, 0.59611105]

    # initial_value = [-64.24105034, 0.31398956, 0.05786442, 0.56935435]
    # initial_value = [-63.40699404, 0.31145892, 0.06375499, 0.53955046]
    # initial_value = [-62.46720875, 0.31054216, 0.0710238, 0.50574653]
    c = 1.0
    Ena = 50
    Ek = -77
    El = -54.4
    gk = 36
    gna = 120
    gl = 0.3
    shift = 0  # Variable shift is to shift the V1/2(n) to different values, such as -51.41mV when shift is -2 mV

    @staticmethod
    def alpha_n(Vm):
        return 0.01 * (Vm + 55 + Model.shift) / (1 - np.exp(-(Vm + 55 + Model.shift) / 10))

    @staticmethod
    def alpha_m(Vm):
        return 0.1 * (40 + Vm) / (1 - np.exp(-(Vm + 40) / 10))

    @staticmethod
    def alpha_h(Vm):
        return 0.07 * np.exp((-(Vm + 65) / 20))

    @staticmethod
    def beta_n(Vm):
        return 0.125 * np.exp(-(Vm + Model.shift + 65) / 80)

    @staticmethod
    def beta_m(Vm):
        return 4 * np.exp(-(Vm + 65) / 18)

    @staticmethod
    def beta_h(Vm):
        return 1 / (np.exp(-(Vm + 35) / 10) + 1)

    @staticmethod
    def n_inf(Vm):
        return Model.alpha_n(Vm) / (Model.alpha_n(Vm) + Model.beta_n(Vm))

    @staticmethod
    def m_inf(Vm):
        return Model.alpha_m(Vm) / (Model.alpha_m(Vm) + Model.beta_m(Vm))

    @staticmethod
    def h_inf(Vm):
        return Model.alpha_h(Vm) / (Model.alpha_h(Vm) + Model.beta_h(Vm))

    @staticmethod
    def tau_n(Vm):
        return 1 / (Model.alpha_n(Vm) + Model.beta_n(Vm))

    @staticmethod
    def tau_m(Vm):
        return 1 / (Model.alpha_m(Vm) + Model.beta_m(Vm))

    @staticmethod
    def tau_h(Vm):
        return 1 / (Model.alpha_h(Vm) + Model.beta_h(Vm))

    @staticmethod
    def Ina(Vm, m, h):
        return Model.gna * (m ** 3) * h * (Vm - Model.Ena)

    @staticmethod
    def Ik(Vm, n):
        return Model.gk * (n ** 4) * (Vm - Model.Ek)

    @staticmethod
    def Il(Vm):
        return Model.gl * (Vm - Model.El)

    @staticmethod
    def Iall(Vm, n, m, h):
        return Model.Il(Vm) + Model.Ik(Vm, n) + Model.Ina(Vm, m, h)

    @staticmethod
    def Gna(m, h):
        return Model.gna * (m ** 3) * h

    @staticmethod
    def Gk(n):
        return Model.gk * (n ** 4)

    @staticmethod
    def Gl():
        return Model.gl

    @staticmethod
    def Function(t, y, dt, Istim):
        Vm = y[0]
        n = y[1]
        m = y[2]
        h = y[3]

        dy = np.zeros((4,))
        current_index = min(round(t / dt), len(Istim[0]) - 1)
        I = Istim[0][current_index]

        dy[0] = (I - Model.Ina(Vm, m, h) - Model.Ik(Vm, n) - Model.Il(Vm)) / Model.c
        dy[1] = (Model.n_inf(Vm) - n) / Model.tau_n(Vm)
        dy[2] = (Model.m_inf(Vm) - m) / Model.tau_m(Vm)
        dy[3] = (Model.h_inf(Vm) - h) / Model.tau_h(Vm)

        return dy
