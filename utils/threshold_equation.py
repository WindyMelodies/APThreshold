import numpy as np
from utils.exceptions import OptimizationInterruptedException


def solve_threshold_model_euler(voltage, dt, ThresholEquation, **kwargs):
    theta = np.zeros_like(voltage)
    theta[0] = ThresholEquation.theta_inf(v=voltage[0], **kwargs)
    for i in range(1, len(voltage)):
        y = [theta[i - 1], voltage[i - 1]]
        theta[i] = theta[i - 1] + dt * ThresholEquation.ode_func(y=y, **kwargs)
    return theta


class FormOne:
    params_name = ['tau_theta', 'alpha', 'ka', 'ki', 'Vi', 'VT']

    @staticmethod
    def theta_inf(v: float or np.array, **kwargs):
        ka = kwargs['ka']
        ki = kwargs['ki']
        Vi = kwargs["Vi"]
        alpha = kwargs['alpha']
        VT = kwargs['VT']
        return alpha * (v - Vi) + VT + ka * np.log(1 + np.exp((Vi - v) / ki))

    @staticmethod
    def ode_func(y, **kwargs):
        theta = y[0]
        v = y[1]
        tau_theta = kwargs['tau_theta']
        dy = (FormOne.theta_inf(v, **kwargs) - theta) / tau_theta
        if "optimizer_thread" in kwargs:
            if kwargs['optimizer_thread'].isInterruptionRequested():
                # 如果收到中断请求，则抛出自定义异常以停止 CMA-ES
                raise OptimizationInterruptedException("Optimization interrupted by user.")
        return dy

class FormTwo:
    params_name = ['tau_theta', 'ka', 'ki', 'Vi', 'VT']

    @staticmethod
    def theta_inf(v: float or np.array, **kwargs):
        ka = kwargs['ka']
        ki = kwargs['ki']
        Vi = kwargs["Vi"]
        VT = kwargs['VT']
        return VT + ka * np.log(1 + np.exp((Vi - v) / ki))

    @staticmethod
    def ode_func(y, **kwargs):
        theta = y[0]
        v = y[1]
        tau_theta = kwargs['tau_theta']
        dy = (FormTwo.theta_inf(v, **kwargs) - theta) / tau_theta
        if "optimizer_thread" in kwargs:
            if kwargs['optimizer_thread'].isInterruptionRequested():
                # 如果收到中断请求，则抛出自定义异常以停止 CMA-ES
                raise OptimizationInterruptedException("Optimization interrupted by user.")
        return dy

class FormThree:
    params_name = ['tau_theta', 'alpha', 'Vi', 'VT']

    @staticmethod
    def theta_inf(v: float, **kwargs):
        Vi = kwargs["Vi"]
        alpha = kwargs['alpha']
        VT = kwargs['VT']

        if v<Vi:
            return VT
        else:
            return alpha*(v-Vi) +VT

    @staticmethod
    def ode_func(y, **kwargs):
        theta = y[0]
        v = y[1]
        tau_theta = kwargs['tau_theta']
        dy = (FormThree.theta_inf(v, **kwargs) - theta) / tau_theta
        if "optimizer_thread" in kwargs:
            if kwargs['optimizer_thread'].isInterruptionRequested():
                # 如果收到中断请求，则抛出自定义异常以停止 CMA-ES
                raise OptimizationInterruptedException("Optimization interrupted by user.")
        return dy
