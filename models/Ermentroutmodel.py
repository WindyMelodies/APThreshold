import numpy as np


class Model:
    number_of_compartment = 1
    dynamic_variables = ['Vm', 'n', 'm', 'h', 'z', 'Ca']
    initial_value = [-67.97472776, 0.15589198, 0.01008029, 0.96589731, 0.5404368, 0.2884849]
    c = 1
    gna = 100
    gk = 80
    gl = 0.1
    gca = 1
    gm = 5  # 5
    gahp = 0  # 5
    Ena = 50
    Ek = -100
    El = -67
    Eca = 120
    tau_z = 100

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
    def z_inf(Vm):
        return 1 / (1 + np.exp(-(Vm + 20) / 5))

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
        return Model.gca / (1 + np.exp(-(Vm + 25) / 5))

    @staticmethod
    def Gahp(Ca):
        return Model.gahp * Ca / (30 + Ca)

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
    def Iahp(Vm, Ca):
        return Model.Gahp(Ca) * (Vm - Model.Ek)

    @staticmethod
    def Function(t, y, dt, Istim):
        Vm = y[0]
        n = y[1]
        m = y[2]
        h = y[3]
        z = y[4]
        Ca = y[5]

        dy = np.zeros((6,))
        current_index = min(round(t / dt), len(Istim[0]) - 1)
        I = Istim[0][current_index]

        dy[0] = (I - Model.Ina(Vm, m, h) - Model.Ik(Vm, n) - Model.Il(Vm) - Model.Im(Vm, z) - Model.Iahp(Vm,
                                                                                                         Ca) - Model.Ica(
            Vm)) / Model.c
        dy[1] = Model.alpha_n(Vm) * (1 - n) - Model.beta_n(Vm)
        dy[2] = Model.alpha_m(Vm) * (1 - m) - Model.beta_m(Vm)
        dy[3] = Model.alpha_h(Vm) * (1 - h) - Model.beta_h(Vm)
        dy[4] = (Model.z_inf(Vm) - z) / Model.tau_z
        dy[5] = -0.002 * Model.Ica(Vm) - 0.0125 * Ca
