import numpy as np

# Select Im current as adaption current in model
class Model:
    number_of_compartment = 1
    dynamic_variables = ['Vm', 'n', 'm', 'h', 'z']
    initial_value = [-66.13470015, 0.0433335, 0.01759918, 0.99494189, 9.83445241e-05]
    c = 1
    gna = 100
    gk = 80
    gl = 0.1
    gca = 1
    gm = 5  # 5
    Ena = 50
    Ek = -100
    El = -67
    Eca = 120

    @staticmethod
    def alpha_m(Vm):
        return 0.32 * (Vm + 54) / (1 - np.exp(-(Vm + 54) / 4))

    @staticmethod
    def beta_m(Vm):
        return 0.28 * (Vm + 27) / (np.exp((Vm + 27) / 5) - 1)

    @staticmethod
    def alpha_h(Vm):
        return 0.128 * np.exp(-(Vm + 50) / 18)

    @staticmethod
    def beta_h(Vm):
        return 4 / (1 + np.exp(-(Vm + 27) / 5))

    @staticmethod
    def alpha_n(Vm):
        return 0.032 * (Vm + 52) / (1 - np.exp(-(Vm + 52) / 5))

    @staticmethod
    def beta_n(Vm):
        return 0.5 * np.exp(-(Vm + 57) / 40)

    @staticmethod
    def alpha_z(Vm):
        return 1 / (1 + np.exp(-(Vm + 20) / 5))

    @staticmethod
    def w_inf(Vm):
        return 1/(1+np.exp(-(25+Vm)/5))

    @staticmethod
    def Gna(m, h):
        return Model.gna * (m ** 3) * h

    @staticmethod
    def Gk(n):
        return Model.gk * (n ** 4)

    @staticmethod
    def Gm(z):
        return Model.gm * z

    @staticmethod
    def Gca(Vm):
        return Model.gca *Model.w_inf(Vm)

    @staticmethod
    def Ina(Vm, m, h):
        return Model.Gna(m, h) * (Vm - Model.Ena)

    @staticmethod
    def Ik(Vm, n):
        return Model.Gk(n) * (Vm - Model.Ek)

    @staticmethod
    def Il(Vm):
        return Model.gl * (Vm - Model.El)

    @staticmethod
    def Im(Vm, z):
        return Model.Gm(z) * (Vm - Model.Ek)

    @staticmethod
    def Ica(Vm):
        return Model.Gca(Vm) * (Vm - Model.Eca)

    @staticmethod
    def Function(t, y, dt, Istim):
        Vm = y[0]
        n = y[1]
        m = y[2]
        h = y[3]
        z = y[4]

        dy = np.zeros((5,))
        current_index = min(round(t / dt), len(Istim[0]) - 1)
        I = Istim[0][current_index]

        dy[0] = (I - Model.Ina(Vm, m, h) - Model.Ik(Vm, n) - Model.Il(Vm) - Model.Im(Vm, z)  - Model.Ica(
            Vm)) / Model.c
        dy[1] = Model.alpha_n(Vm) * (1 - n) - Model.beta_n(Vm)*n
        dy[2] = Model.alpha_m(Vm) * (1 - m) - Model.beta_m(Vm)*m
        dy[3] = Model.alpha_h(Vm) * (1 - h) - Model.beta_h(Vm)*h
        dy[4] = 0.01*(Model.alpha_z(Vm)-z)

        return dy
