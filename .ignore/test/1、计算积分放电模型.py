import matplotlib.pyplot as plt
import numpy as np

number_of_compartment = 1
dynamic_variables = ['Vm']
initial_value = [-70]
theta = -63
El = -70  # 单位：毫伏
Rm = 100  # 单位：兆欧
tau_m = 5  # 单位：毫秒
delta = 1  # 单位：毫伏
t_spike = None  # 将初始的放电时刻设置为空


def stimulus_generation():
    pass


def Function(t, y, dt, Istim):
    Vm = y[0]
    dy = np.zeros((1,))
    current_index = min(round(t / dt), len(Istim[0]) - 1)
    I = Istim[0][current_index]
    # 模型达到阈值后立刻恢复为静息值，并且在绝对不应期内仍保持静息值
    dy[0] = ((El - Vm) + Rm * I * 0.001 + delta * np.exp((Vm - theta) / delta)) / tau_m
    return dy


def euler_method(t, dt, Istim, initial_value, Vth, t_ref):
    """
    desc：欧拉法求解微分方程，得到数组形式的解
        data(dict):{
        'timestamp':
        }
    :param t: 时间线
    :param dt: 步长
    :param initial_value: 神经元动力学变量的初值，为一个列表
    :param Function: 神经元模型提前定义的常微分方程组
    :param kwargs:
    :return: sol：神经元模型的解，使用方法：Vm=sol[0,:]（按列对应动力学变量的解）
    """
    t_spike = None
    sol = np.full((len(t), len(initial_value)), initial_value)
    for i in range(1, len(t)):
        if sol[i - 1, 0] > Vth:
            t_spike = t[i - 1]
        else:
            if t_spike:
                print(123)
                if t[i] - t_spike <= t_ref:
                    pass
                else:
                    y_pre = sol[i - 1, :]
                    dydt = Function(t[i - 1], y_pre, dt, Istim)
                    y = dydt * dt + y_pre
                    sol[i] = y
            else:
                y_pre = sol[i - 1, :]
                dydt = Function(t[i - 1], y_pre, dt, Istim)
                y = dydt * dt + y_pre
                sol[i] = y
    return sol


def get_stimulus():
    pass


simulation_duration = 500  # ms
dt = 0.01
t = np.linspace(0, simulation_duration, int(simulation_duration / dt + 1))
Is = np.full((1, len(t)), 70.0)
print(Is)
sol = euler_method(t, dt, Is, initial_value=[-70.0], Vth=theta, t_ref=0.8)
V = sol[:, 0]
plt.plot(t, V)
plt.show()
