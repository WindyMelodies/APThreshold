import brainpy as bp
import brainpy.math as bm
import numpy as np
import matplotlib.pyplot as plt


class ExpIF(bp.dyn.NeuGroup):
    def __init__(self, size, V_rest=-65., V_reset=-68., V_th=20., V_T=-59.9, delta_T=3.48, R=1., tau=10., t_ref=0.8,
                 name=None):
        super(ExpIF, self).__init__(size=size, name=name)

        # 初始化参数
        self.V_rest = V_rest
        self.V_reset = V_reset
        self.V_th = V_th
        self.V_T = V_T
        self.delta_T = delta_T
        self.R = R
        self.tau = tau
        self.t_ref = t_ref

        # 初始化变量
        self.V = bm.Variable(bm.random.randn(self.num) + V_reset)
        self.input = bm.Variable(bm.zeros(self.num))
        self.t_last_spike = bm.Variable(bm.ones(self.num) * -1e7)  # 上一次脉冲发放时刻
        self.refractory = bm.Variable(bm.zeros(self.num, dtype=bool))  # 是否处于不应期
        self.spike = bm.Variable(bm.zeros(self.num, dtype=bool))  # 脉冲发放状态

        # 积分函数:使用指数欧拉方法积分
        self.integral = bp.odeint(f=self.derivative, method='exponential_euler')

        # 定义膜电位关于时间变化的微分方程

    def derivative(self, V, t, Iext):
        exp_v = self.delta_T * bm.exp((V - self.V_T) / self.delta_T)
        dvdt = (- (V - self.V_rest) + exp_v + self.R * Iext) / self.tau
        return dvdt

        # 更新函数

    def update(self, tdi):
        t, dt = tdi.t, tdi.dt
        refractory = (t - self.t_last_spike) <= self.t_ref  # 是否处于不应期
        V = self.integral(self.V, t, self.input, dt=dt)  # 根据时间步长更新膜电位
        V = bm.where(refractory, self.V, V)
        spike = V > self.V_th  # 更新脉冲状态
        self.spike.value = spike
        self.t_last_spike = bm.where(spike, t, self.t_last_spike)  # 更新上次脉冲时间
        self.V.value = bm.where(spike, self.V_reset, V)
        self.refractory.value = bm.logical_or(refractory, spike)
        self.input[:] = 0  # 重置外界输入


group = ExpIF(1)
runner = bp.dyn.DSRunner(group, monitors=['V'], inputs=('input', 5.), dt=0.01)
runner(500)
fig = plt.figure(figsize=(3.5,2.625))
plt.plot(runner.mon.ts, runner.mon.V)
plt.xlabel('t(ms)')
plt.ylabel('V')
plt.show()