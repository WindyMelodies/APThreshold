import numpy as np


class Model:
    number_of_compartment = 1
    dynamic_variables = ['Vm', 'n']
    initial_value = [-64.99972243, 0.317681168]  # todo

    gl = 2
    gca = 4
    gk = 8
    El = -60
    Eca = 120
    Ek = -84
    V1 = -1.2
    V2 = 18
    V3 = 12
    V4 = 17.4

    @staticmethod
    def m_inf(Vm):
        return 0.5 * (1 + np.cosh((Vm - Model.V1) / Model.V2))

    @staticmethod
    def n_inf(Vm):
        return 0.5 * (1 + np.cosh((Vm - Model.V3) / Model.V4))

    @staticmethod
    def tau_n(Vm):
        return 1 / (np.cosh((Vm - Model.V3) / (2 * Model.V4)))

    @staticmethod
    def Ica(Vm):
        return Model.gca * Model.m_inf(Vm) * (Vm - Model.Eca)

    @staticmethod
    def Ik(Vm, n):
        return Model.gk * n * (Vm - Model.Ek)

    @staticmethod
    def Il(Vm):
        return Model.gl * (Vm - Model.El)

    @staticmethod
    def Gl():
        return Model.gl

    @staticmethod
    def Gca(Vm):
        return Model.gca * Model.m_inf(Vm)

    @staticmethod
    def Gk(n):
        return Model.gk * n

    @staticmethod
    def Function(t, y, dt, Istim):
        Vm = y[0]
        n = y[1]

        dy = np.zeros((2,))
        current_index = min(round(t / dt), len(Istim) - 1)
        I = Istim[0][current_index]

        dy[0] = I - Model.Ica(Vm) - Model.Ik(Vm, n) - Model.Il(Vm)
        dy[1] = (Model.n_inf(Vm) - n) / Model.tau_n(Vm)
        return dy
