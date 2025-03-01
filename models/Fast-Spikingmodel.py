import numpy as np


class Model:
    number_of_compartment = 1
    dynamic_variables = ['Vm', 'n', 'h', 'a', 'b']
    initial_value = [-70.03810532, 0.000208327, 0.852199343, 0.268566988, 0.501587716]
    c = 1.0

    Ena = 50
    Ek = -90
    El = -70
    gk = 225
    gna = 112.5
    gl = 0.25
    gd = 1.8  # Variable parameter: 0.39 for delayed tonic firing and 1.8 for delayed stuttering

    theta_m = -24
    sigma_m = 11.5

    theta_h = -58.3
    sigma_h = -6.7

    theta_n = -12.4
    sigma_n = 6.8

    theta_th = -60
    sigma_th = -12

    theta_tn = -27
    sigma_tn = -15

    theta_a = -50
    sigma_a = 20
    tau_a = 2

    theta_b = -70
    sigma_b = -6
    tau_b = 150

    @staticmethod
    def m_inf(Vm):
        return 1 / (1 + np.exp(-(Vm - Model.theta_m) / Model.sigma_m))

    @staticmethod
    def h_inf(Vm):
        return 1 / (1 + np.exp(-(Vm - Model.theta_h) / Model.sigma_h))

    @staticmethod
    def n_inf(Vm):
        return 1 / (1 + np.exp(-(Vm - Model.theta_n) / Model.sigma_n))

    @staticmethod
    def a_inf(Vm):
        return 1 / (1 + np.exp(-(Vm - Model.theta_a) / Model.sigma_a))

    @staticmethod
    def b_inf(Vm):
        return 1 / (1 + np.exp(-(Vm - Model.theta_b) / Model.sigma_b))

    @staticmethod
    def tau_n(Vm):
        return (0.087 + 11.4 / (1 + (1 + np.exp((Vm + 14.6) / 8.6))) * (
                0.087 + 11.4 / (1 + np.exp(-(Vm - 13) / 18.7))))

    @staticmethod
    def tau_h(Vm):
        return 0.5 + 14 / (1 + np.exp(-(Vm - Model.theta_th) / Model.sigma_th))

    @staticmethod
    def INa(Vm, h):
        return Model.gna * (Model.m_inf(Vm) ** 3) * h * (Vm - Model.Ena)

    @staticmethod
    def Ikdr(Vm, n):
        return Model.gk * (n ** 2) * (Vm - Model.Ek)

    @staticmethod
    def Id(Vm, a, b):
        return Model.gd * (a ** 3) * b * (Vm - Model.Ek)

    @staticmethod
    def Il(Vm):
        return Model.gl * (Vm - Model.El)

    @staticmethod
    def Gk(n):
        return Model.gk * (n ** 2)

    @staticmethod
    def Gna(Vm, h):
        return Model.gna * (Model.m_inf(Vm) ** 3) * h

    @staticmethod
    def Gl():
        return Model.gl

    @staticmethod
    def Gd(a, b):
        return Model.gd * (a ** 3) * b

    @staticmethod
    def Function(t, y, dt, Istim):
        Vm = y[0]
        n = y[1]
        h = y[2]
        a = y[3]
        b = y[4]

        dy = np.zeros((5,))
        current_index = min(round(t / dt), len(Istim[0]) - 1)
        I = Istim[0][current_index]

        dy[0] = I - Model.INa(Vm, h) - Model.Ikdr(Vm, n) - Model.Id(Vm, a, b) - Model.Il(Vm)
        dy[1] = (Model.n_inf(Vm) - n) / Model.tau_n(Vm)
        dy[2] = (Model.h_inf(Vm) - h) / Model.tau_h(Vm)
        dy[3] = (Model.a_inf(Vm) - a) / Model.tau_a
        dy[4] = (Model.b_inf(Vm) - b) / Model.tau_b
        return dy
