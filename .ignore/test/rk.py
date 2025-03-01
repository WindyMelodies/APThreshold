import copy
from scipy.integrate import odeint
import numpy as np
from matplotlib import pyplot as plt
from models.Stimulus import Stimulus

"""
稳态值：v0=-64.99972243，n0=0.317681168，m0=0.052934218，h0=0.596111046
具备功能：计算模型的所有基础数值包括膜电压、门控变量、电导、离子电流、刺激电流的数组值
"""


class HHmodel:

    def __init__(self, t, I, dt=1e-2, v0=-64.99972243, n0=0.317681168, m0=0.052934218,
                 h0=0.596111046, c=1, Ena=50, Ek=-77, El=-54.4, gk=36, gna=120, gl=0.3):
        # 单个动作电位
        self.t_complete = None
        self.t_adjustment = None
        self.spike = False  # 储存True、False 目的：判断是否放电
        self.spike_times = None  # 储存：放电次数
        self.spike_flag = []  # 储存：所有单个动作电位去极化和复极化过0的索引
        self.spike_flag_final = []  # 储存：所有单个动作电位最终地去极化起点和复极化终点
        self.spike_ap_voltage = []  # 储存：所有单个动作电位的膜电压值
        self.spike_ap_dvdt1 = []  # 储存：所有单个动作电位的膜电压值一阶时间导数
        self.spike_ap_dvdt2 = []
        self.spike_ap_dvdt3 = []
        self.spike_ap_voltage_drawing_complete = []
        self.spike_ap_voltage_drawing_adjustment = []
        self.data_spike_ap_original = []

        # 数据分类
        self.data_voltage = []
        self.data_variable = []
        self.data_conductance = []
        self.data_ionic_currents = []
        self.data_stimulus = []
        self.data_differential_values = []
        self.data_spike_ap_voltage_drawing = []
        self.abc = []
        self.v_values = []
        self.n_values = []
        self.m_values = []
        self.h_values = []
        self.I = I
        self.c = c
        self.Ena = Ena
        self.Ek = Ek
        self.El = El
        self.gk = gk
        self.gna = gna
        self.gl = gl
        self.t = t
        self.dt = dt
        self.m0 = m0
        self.v0 = v0
        self.n0 = n0
        self.h0 = h0

        # 膜电压对时间导数值
        self.dvdt1 = [None]
        self.dvdt2 = [None, None]
        self.dvdt3 = [None, None, None]

    def alpha_n(self, V):
        return 0.01 * (V + 55) / (1 - np.exp(-(V + 55) / 10))

    def alpha_m(self, V):
        return 0.1 * (40 + V) / (1 - np.exp(-(V + 40) / 10))

    def alpha_h(self, V):
        return 0.07 * np.exp((-(V + 65) / 20))

    def beta_n(self, V):
        return 0.125 * np.exp(-(V + 65) / 80)

    def beta_m(self, V):
        return 4 * np.exp(-(V + 65) / 18)

    def beta_h(self, V):
        return 1 / (np.exp(-(V + 35) / 10) + 1)

    #   门控变量的稳态值

    def n_s(self, V):
        return self.alpha_n(V) / (self.alpha_n(V) + self.beta_n(V))

    def m_s(self, V):
        return self.alpha_m(V) / (self.alpha_m(V) + self.beta_m(V))

    def h_s(self, V):
        return self.alpha_h(V) / (self.alpha_h(V) + self.beta_h(V))

    #   计算门控变量对应的时间常数

    def tau_n(self, V):
        return 1 / (self.alpha_n(V) + self.beta_n(V))

    def tau_m(self, V):
        return 1 / (self.alpha_m(V) + self.beta_m(V))

    def tau_h(self, V):
        return 1 / (self.alpha_h(V) + self.beta_h(V))

    def I_na(self, V, m, h):
        return self.gna * (m ** 3) * h * (V - self.Ena)

    def I_k(self, V, n):
        return self.gk * (n ** 4) * (V - self.Ek)

    def I_l(self, V):
        return self.gl * (V - self.El)

    def rk_4(self):

        self.v_values.append(self.v0)
        self.n_values.append(self.n0)
        self.m_values.append(self.m0)
        self.h_values.append(self.h0)
        for i in range(1,len(self.t)):
            n_k1=0

if __name__ == '__main__':
    start = 0
    width = 100
    timeline = 100
    dt = 0.01
    num = int(timeline / dt) + 1
    t = np.linspace(0, timeline, num)
    I = Stimulus(t)
    # I.add_current(current_type='step', amplitude=10, start_time=start, end_time=start + width)
    I.add_current(current_type='noise', theta=10, sigma=10, start_time=start, end_time=start + width)
    I.get_current()
    a = HHmodel(t=t, I=I)
    a.main()
    # print(len(a.abc))
    # print(a.spike_ap_voltage_drawing_adjustment)
    # print('动作电位个数为：{}'.format(len(a.data_spike_ap_voltage_drawing_adjustment[0])))
    # for i in range(len(a.data_spike_ap_voltage_drawing_adjustment[0])):

    # print('每个动作电位长度为：{}'.format(len(a.data_spike_ap_voltage_drawing_adjustment[0][i])))
    # for i in range(len(a.spike_ap_voltage_drawing_adjustment)):
    # print(len(a.spike_ap_voltage_drawing_adjustment[0]))
