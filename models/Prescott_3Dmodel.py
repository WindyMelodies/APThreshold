import numpy as np

"""
顺序
参数的定义：
1、间室个数
2、动力学变量（注：名称需和后续函数中传递参数的名称相同）
3、电容、平衡电势、半激活电压、电导等
4、定义函数：稳态门控变量、时间常数、电导、电流
5、常微分方程

语法解释：
@statisticmethod：表示python中类对象的静态函数，使用者理解与否不影响文件的编写，仅需在定义函数之前加上此前缀即可
Model.Ena等参数的调用：表示调用python中类对象的属性（参数），需在调用时在参数名称之前加上Model.字眼
"""


class Model:
    number_of_compartment = 1
    dynamic_variables = ['Vm', 'y', 'z']
    initial_value = [-69.07786247, 7.38854388e-06, 0.0016417]
    c = 2.0
    Ena = 50
    Ek = -100
    El = -70

    beta_z = -21
    gama_z = 15
    beta_y = -10
    gama_y = 10
    beta_m = -1.2
    gama_m = 18
    fi_y = 0.15

    gk = 20
    gna = 20
    gl = 2
    # type I
    Esub = 50
    gsub = 3
    fi_z = 0.5

    # type II
    # Esub = -100
    # gsub = 2
    # fi_z = 0.15

    @staticmethod
    def y_inf(Vm):
        return 0.5 * (1 + np.tanh((Vm - Model.beta_y) / Model.gama_y))

    @staticmethod
    def z_inf(Vm):
        return 0.5 * (1 + np.tanh((Vm - Model.beta_z) / Model.gama_z))

    @staticmethod
    def m_inf(Vm):
        return 0.5 * (1 + np.tanh((Vm - Model.beta_m) / Model.gama_m))

    @staticmethod
    def tau_y(Vm):
        return 1 / np.cosh((Vm - Model.beta_y) / (2 * Model.beta_y))

    @staticmethod
    def tau_z(Vm):
        return 1 / np.cosh((Vm - Model.beta_z) / (2 * Model.gama_z))

    @staticmethod
    def Gna(Vm):
        return Model.gna * Model.m_inf(Vm)

    @staticmethod
    def Gk(y):
        return Model.gk * y

    @staticmethod
    def Gl():
        return Model.gl

    @staticmethod
    def Gsub(z):
        return Model.gsub * z

    @staticmethod
    def Ina(Vm):
        return Model.Gna(Vm) * (Vm - Model.Ena)

    @staticmethod
    def Ik(Vm, y):
        return Model.Gk(y) * (Vm - Model.Ek)

    @staticmethod
    def Isub(Vm, z):
        return Model.Gsub(z) * (Vm - Model.Esub)

    @staticmethod
    def Il(Vm):
        return Model.Gl() * (Vm - Model.El)

    @staticmethod
    def Inet(Vm, y, z):
        return Model.Il(Vm) + Model.Isub(Vm, z) + Model.Ik(Vm, y) + Model.Ina(Vm)

    @staticmethod
    def Function(t, y_output, dt, Istim):
        Vm = y_output[0]
        y = y_output[1]
        z = y_output[2]
        dy = np.zeros((3,))
        current_index = min(round(t / dt), len(Istim[0]) - 1)
        I = Istim[0][current_index]
        dy[0] = (I - Model.Ina(Vm) - Model.Ik(Vm, y) - Model.Isub(Vm, z) - Model.Il(Vm)) / Model.c
        dy[1] = Model.fi_y * (Model.y_inf(Vm) - y) / Model.tau_y(Vm)
        dy[2] = Model.fi_z * (Model.z_inf(Vm) - z) / Model.tau_z(Vm)
        return dy
