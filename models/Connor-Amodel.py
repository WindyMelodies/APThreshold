import numpy as np


class Model:
    number_of_compartment = 1
    dynamic_variables = ['Vm', 'n', 'm', 'h', 'A', 'B']
    initial_value = [-67.97472776, 0.15589198, 0.01008029, 0.96589731, 0.5404368, 0.2884849]
    c = 1.0
    Ena = 55
    Ek = -72
    El = -17
    EA = -75
    gk = 20
    gna = 120
    gl = 0.3
    gA = 60         # typeI：60  typeII：0，30
    MSHFT = -5.3
    HSHFT = -12
    NSHFT = -4.3

    @staticmethod
    def alpha_n(Vm):
        return 0.01 * (Vm + 50 + Model.NSHFT) / (1 - np.exp(-(Vm + 50 + Model.NSHFT) / 10))

    @staticmethod
    def alpha_m(Vm):
        return -0.1 * (35 + Model.MSHFT + Vm) / (np.exp(-(Vm + 35 + Model.MSHFT) / 10) - 1)

    @staticmethod
    def alpha_h(Vm):
        return 0.07 * np.exp((-(Vm + 60 + Model.HSHFT) / 20))

    @staticmethod
    def beta_n(Vm):
        return 0.125 * np.exp(-(Vm + 60 + Model.NSHFT) / 80)

    @staticmethod
    def beta_m(Vm):
        return 4 * np.exp(-(Vm + 60 + Model.MSHFT) / 18)

    @staticmethod
    def beta_h(Vm):
        return 1 / (np.exp(-(Vm + 30 + Model.HSHFT) / 10) + 1)

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
    def A_inf(Vm):
        return ((0.0761 * np.exp((Vm + 94.22) / 31.84)) / (1 + np.exp((Vm + 1.17) / 28.93))) ** (1 / 3)

    @staticmethod
    def B_inf(Vm):
        return 1 / ((1 + np.exp((Vm + 53.3) / 14.54)) ** 4)

    @staticmethod
    def tau_n(Vm):
        return 1 / (1.9 * (Model.alpha_n(Vm) + Model.beta_n(Vm)))

    @staticmethod
    def tau_m(Vm):
        return 1 / (3.8 * (Model.alpha_m(Vm) + Model.beta_m(Vm)))

    @staticmethod
    def tau_h(Vm):
        return 1 / (3.8 * (Model.alpha_h(Vm) + Model.beta_h(Vm)))

    @staticmethod
    def tau_A(Vm):
        return 0.3632 + (1.158 / (1 + np.exp((Vm + 55.96) / 20.12)))

    @staticmethod
    def tau_B(Vm):
        return 1.24 + 2.678 / (1 + np.exp((Vm + 50) / 16.027))

    @staticmethod
    def Ina(Vm, m, h):
        return Model.gna * (m ** 3) * h * (Vm - Model.Ena)

    @staticmethod
    def Ik(Vm, n):
        return Model.gk * (n ** 4) * (Vm - Model.Ek)

    @staticmethod
    def IL(Vm):
        return Model.gl * (Vm - Model.El)

    @staticmethod
    def IA(Vm, A, B):
        return Model.gA * (A ** 3) * B * (Vm - Model.EA)

    @staticmethod
    def Inet(Vm, m, h, n, A, B):
        return Model.Ina(Vm, m, h) + Model.Ik(Vm, n) + Model.IL(Vm) + Model.IA(Vm, A, B)

    @staticmethod
    def Gna(m, h):
        return Model.gna * (m ** 3) * h

    @staticmethod
    def Gk(n):
        return Model.gk * (n ** 4)

    @staticmethod
    def GL():
        return Model.gl

    @staticmethod
    def GA(A, B):
        return Model.gA * (A ** 3) * B

    @staticmethod
    def Function(t, y, dt, Istim):
        Vm = y[0]
        n = y[1]
        m = y[2]
        h = y[3]
        A = y[4]
        B = y[5]
        dy = np.zeros((6,))
        current_index = min(round(t / dt), len(Istim[0]) - 1)
        I = Istim[0][current_index]

        dy[0] = (I - Model.Ina(Vm, m, h) - Model.Ik(Vm, n) - Model.IL(Vm) - Model.IA(Vm, A, B)) / Model.c
        dy[1] = (Model.n_inf(Vm) - n) / Model.tau_n(Vm)
        dy[2] = (Model.m_inf(Vm) - m) / Model.tau_m(Vm)
        dy[3] = (Model.h_inf(Vm) - h) / Model.tau_h(Vm)
        dy[4] = (Model.A_inf(Vm) - A) / Model.tau_A(Vm)
        dy[5] = (Model.B_inf(Vm) - B) / Model.tau_B(Vm)
        return dy
