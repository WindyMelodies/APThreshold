import numpy as np


class Model:
    # Iahp: gadapt = 10, beta_z = 0, gama_z = 5, tau_z = 200
    # Im: gadapt = 2, beta_z = -23, gama_z = 5, tau_z = 200

    number_of_compartment = 2
    dynamic_variables = ['Vs', 'Vd', 'w', 'z']  # dynamic variable name
    initial_value = [-69.6033054, -69.8016527, 9.00188204e-07, 8.95479034e-05]

    c = 2
    Vds = 0
    p = 0.5

    Ena = 50
    Ek = -100
    Esl = -70
    Edl = -70

    beta_m = -1.2
    gama_m = 18
    beta_w = 0
    gama_w = 10
    fi_w = 0.15

    gc = 1
    gna = 20
    gk = 20
    gsl = 2
    gdl = 2
    # Im
    gadapt = 2
    beta_z = -23
    gama_z = 5
    tau_z = 200

    # Iahp
    # gadapt = 10
    # beta_z = 0
    # gama_z = 5
    # tau_z = 200

    @staticmethod
    def m_inf(Vs):
        return 0.5 * (1 + np.tanh((Vs - Model.beta_m) / Model.gama_m))

    @staticmethod
    def w_inf(Vs):
        return 0.5 * (1 + np.tanh((Vs - Model.beta_w) / Model.gama_w))

    @staticmethod
    def tau_w(Vs):
        return 1 / np.cosh((Vs - Model.beta_w) / (2 * Model.gama_w))

    @staticmethod
    def z_inf(Vs):
        return 1 / (1 + np.exp((Model.beta_z - Vs) / Model.gama_z))

    @staticmethod
    def Ina(Vs):
        return Model.Gna(Vs) * (Vs - Model.Ena)

    @staticmethod
    def Ik(Vs, w):
        return Model.Gk(w) * (Vs - Model.Ek)

    @staticmethod
    def Iadapt(Vs, z):
        return Model.Gadapt(z) * (Vs - Model.Ek)

    @staticmethod
    def Isleak(Vs):
        return Model.Gsl() * (Vs - Model.Esl)

    @staticmethod
    def Idleak(Vd):
        return Model.Gdl() * (Vd - Model.Edl)

    @staticmethod
    def Ids(Vs, Vd):
        return Model.gc * (Vd + Model.Vds - Vs)

    @staticmethod
    def Inet(Vs, Vd, w, z):
        return -Model.Ids(Vs, Vd) / Model.p + Model.Ina(Vs) + Model.Ik(Vs, w) + Model.Iadapt(Vs, z) + Model.Isleak(Vs)

    @staticmethod
    def Gna(Vs):
        return Model.gna * Model.m_inf(Vs)

    @staticmethod
    def Gk(w):
        return Model.gk * w

    @staticmethod
    def Gadapt(z):
        return Model.gadapt * z

    @staticmethod
    def Gsl():
        return Model.gsl

    @staticmethod
    def Gdl():
        return Model.gdl

    @staticmethod
    def Function(t, y, dt, Istim):
        Vs = y[0]
        Vd = y[1]
        w = y[2]
        z = y[3]
        dy = np.zeros((4,))
        current_index = min(int(round(t / dt, 0)), len(Istim[0]) - 1)
        Is = Istim[0][current_index]
        Id = Istim[1][current_index]
        dy[0] = (Is / Model.p + Model.Ids(Vs, Vd) / Model.p - Model.Ina(Vs) - Model.Ik(Vs, w) - Model.Iadapt(Vs,
                                                                                                             z) - Model.Isleak(
            Vs)) / Model.c
        dy[1] = (Id / (1 - Model.p) - Model.Ids(Vs, Vd) / (1 - Model.p) - Model.Idleak(Vd)) / Model.c
        dy[2] = Model.fi_w * (Model.w_inf(Vs) - w) / Model.tau_w(Vs)
        dy[3] = (Model.z_inf(Vs) - z) / Model.tau_z
        return dy
