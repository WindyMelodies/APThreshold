import numpy as np


class Model:
    # Im: gadapt = 0.5, beta_z = -35, gama_z = 4, tau_z = 100
    # Iahp: gadapt = 5, beta_z = 0, gama_z = 4, tau_z = 100

    number_of_compartment = 1
    dynamic_variables = ['Vm', 'w', 'z']
    initial_value = [-69.39044634, 9.39338242e-07, 0.00018451]
    c = 2

    beta_m = -1.2
    gama_m = 18
    beta_w = 0
    gama_w = 10
    fi_w = 0.15

    gna = 20
    gk = 20
    gl = 2

    Ena = 50
    Ek = -100
    El = -70

    gadapt = 0.5
    beta_z = -35
    gama_z = 4
    tau_z = 100

    @staticmethod
    def m_inf(Vm):
        return 0.5 * (1 + np.tanh((Vm - Model.beta_m) / Model.gama_m))

    @staticmethod
    def w_inf(Vm):
        return 0.5 * (1 + np.tanh((Vm - Model.beta_w) / Model.gama_w))

    @staticmethod
    def tau_w(Vm):
        return 1 / np.cosh((Vm - Model.beta_w) / (2 * Model.gama_w))

    @staticmethod
    def z_inf(Vm):
        return 1 / (1 + np.exp((Model.beta_z - Vm) / Model.gama_z))

    @staticmethod
    def Ina(Vm):
        return Model.Gna(Vm) * (Vm - Model.Ena)

    @staticmethod
    def Ik(Vm, w):
        return Model.Gk(w) * (Vm - Model.Ek)

    @staticmethod
    def Iadapt(Vm, z):
        return Model.Gadapt(z) * (Vm - Model.Ek)

    @staticmethod
    def Il(Vm):
        return Model.Gl() * (Vm - Model.El)

    @staticmethod
    def Inet(Vm, w, z):
        return Model.Ina(Vm) + Model.Ik(Vm, w) + Model.Iadapt(Vm, z) + Model.Il(Vm)

    @staticmethod
    def Gna(Vm):
        return Model.gna * Model.m_inf(Vm)

    @staticmethod
    def Gk(w):
        return Model.gk * w

    @staticmethod
    def Gadapt(z):
        return Model.gadapt * z

    @staticmethod
    def Gl():
        return Model.gl

    @staticmethod
    def Function(t, y, dt, Istim):
        Vm = y[0]
        w = y[1]
        z = y[2]
        # print(t)
        dy = np.zeros((3,))
        current_index = min(int(round(t / dt, 0)), len(Istim[0]) - 1)
        I = Istim[0][current_index]

        dy[0] = (I - Model.Ina(Vm) - Model.Ik(Vm, w) - Model.Iadapt(Vm, z) - Model.Il(Vm)) / Model.c
        dy[1] = Model.fi_w * (Model.w_inf(Vm) - w) / Model.tau_w(Vm)
        dy[2] = (Model.z_inf(Vm) - z) / Model.tau_z
        return dy
