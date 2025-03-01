import numpy as np


class Model:

    number_of_compartment = 2
    dynamic_variables = ['Vs', 'Vd', 'h', 'n', 's', 'c', 'q', 'Ca']
    initial_value = [-1.51156162, -1.59661175, 9.97248832e-01, 9.01491522e-04, 0.01229461, 0.00918028, 0.06632326,
                     0.36636408]
    p = 0.5
    Ena = 120
    Eca = 140
    Ek = -15
    El = 0
    c = 3.0  # μF/cm^2
    gL = 0.1
    gna = 30
    gkdr = 15
    gca = 10
    gkahp = 0.8
    gkc = 15
    gc = 2.1  # 1.5-2.1 mS/cm^2

    @staticmethod
    def alpha_m(Vs):
        return (0.32 * (13.1 - Vs)) / (np.exp((13.1 - Vs) / 4) - 1)

    @staticmethod
    def beta_m(Vs):
        return (0.28 * (Vs - 40.1) / (np.exp((Vs - 40.1) / 5) - 1))

    @staticmethod
    def alpha_h(Vs):
        return 0.128 * np.exp((17 - Vs) / 18)

    @staticmethod
    def beta_h(Vs):
        return 4 / (1 + np.exp((40 - Vs) / 5))

    @staticmethod
    def alpha_n(Vs):
        return (0.016 * (35.1 - Vs)) / (np.exp((35.1 - Vs) / 5) - 1)

    @staticmethod
    def beta_n(Vs):
        return 0.25 * np.exp(0.5 - 0.025 * Vs)

    @staticmethod
    def alpha_s(Vd):
        return 1.6 / (1 + np.exp(-0.072 * (Vd - 65)))

    @staticmethod
    def beta_s(Vd):
        return 0.02 * (Vd - 51.1) / (np.exp((Vd - 51.1) / 5) - 1)

    @staticmethod
    def alpha_c(Vd):
        if Vd <= 50:
            return np.exp((Vd - 10) / 11 - (Vd - 6.5) / 27.0) / 18.975
        else:
            return 2 * np.exp((6.5 - Vd) / 27)

    @staticmethod
    def beta_c(Vd):
        if Vd <= 50:
            return 2 * np.exp((6.5 - Vd) / 27) - Model.alpha_c(Vd)
        else:
            return 0

    @staticmethod
    def alpha_q(Ca):
        return min(0.00002 * Ca, 0.01)

    @staticmethod
    def beta_q():
        return 0.001

    @staticmethod
    def m_inf(Vs):
        return Model.alpha_m(Vs) / (Model.alpha_m(Vs) + Model.beta_m(Vs))

    @staticmethod
    def h_inf(Vs):
        return Model.alpha_h(Vs) / (Model.alpha_h(Vs) + Model.beta_h(Vs))

    @staticmethod
    def n_inf(Vs):
        return Model.alpha_n(Vs) / (Model.alpha_n(Vs) + Model.beta_n(Vs))

    @staticmethod
    def s_inf(Vd):
        return Model.alpha_s(Vd) / (Model.alpha_s(Vd) + Model.beta_s(Vd))

    @staticmethod
    def c_inf(Vd):
        return Model.alpha_c(Vd) / (Model.alpha_c(Vd) + Model.beta_c(Vd))

    @staticmethod
    def q_inf(Ca):
        return Model.alpha_q(Ca) / (Model.alpha_q(Ca) + Model.beta_q())

    @staticmethod
    def tau_h(Vs):
        return 1 / (Model.alpha_h(Vs) + Model.beta_h(Vs))

    @staticmethod
    def tau_n(Vs):
        return 1 / (Model.alpha_n(Vs) + Model.beta_n(Vs))

    @staticmethod
    def tau_s(Vd):
        return 1 / (Model.alpha_s(Vd) + Model.beta_s(Vd))

    @staticmethod
    def tau_c(Vd):
        return 1 / (Model.alpha_c(Vd) + Model.beta_c(Vd))

    @staticmethod
    def tau_q(Ca):
        return 1 / (Model.alpha_q(Ca) + Model.beta_q())

    @staticmethod
    def chi(Ca):
        return min(Ca / 250, 1)

    @staticmethod
    def Ina(Vs, h):
        return Model.gna * (Model.m_inf(Vs) ** 2) * h * (Vs - Model.Ena)

    @staticmethod
    def Ik(Vs, n):
        return Model.gkdr * n * (Vs - Model.Ek)

    @staticmethod
    def Isl(Vs):
        return Model.gL * (Vs - Model.El)

    @staticmethod
    def Ica(Vd, s):
        return Model.gca * (s ** 2) * (Vd - Model.Eca)

    @staticmethod
    def Idl(Vd):
        return Model.gL * (Vd - Model.El)

    @staticmethod
    def Ikc(Vd, c, Ca):
        return Model.gkc * Model.chi(Ca) * c * (Vd - Model.Ek)

    @staticmethod
    def Ikahp(Vd, q):
        return Model.gkahp * q * (Vd - Model.Ek)

    @staticmethod
    def Ids(Vs, Vd):
        return Model.gc * (Vd - Vs)

    @staticmethod
    def Function(t, y, dt, Istim):
        Vs = y[0]
        Vd = y[1]
        h = y[2]
        n = y[3]
        s = y[4]
        c = y[5]
        q = y[6]
        Ca = y[7]

        dy = np.zeros((8,))
        current_index = min(int(round(t / dt, 0)), len(Istim[0]) - 1)
        Is = Istim[0][current_index]
        Id = Istim[1][current_index]

        dy[0] = (Is / Model.p + Model.Ids(Vs, Vd) / Model.p - Model.Ina(Vs, h) - Model.Ik(Vs, n) - Model.Isl(
            Vs)) / Model.c

        dy[1] = (Id / (1 - Model.p) - Model.Ids(Vs, Vd) / (1 - Model.p) - Model.Ica(Vd, s) - Model.Ikahp(Vd,
                                                                                                         q) - Model.Ikc(
            Vs, c, Ca) - Model.Idl(Vd)) / Model.c
        # dy[1] = (Id / (1 - Model.p) - Model.Ids(Vs, Vd) / (1 - Model.p) - Model.Idl(Vd))
        dy[2] = Model.alpha_h(Vs) * (1 - h) - Model.beta_h(Vs) * h
        dy[3] = Model.alpha_n(Vs) * (1 - n) - Model.beta_n(Vs) * n
        dy[4] = Model.alpha_s(Vd) * (1 - s) - Model.beta_s(Vd) * s
        dy[5] = Model.alpha_c(Vd) * (1 - c) - Model.beta_c(Vd) * c
        dy[6] = Model.alpha_q(Ca) * (1 - q) - Model.beta_q() * q
        dy[7] = -0.13 * Model.Ica(Vd, s) - 0.075 * Ca
        return dy
