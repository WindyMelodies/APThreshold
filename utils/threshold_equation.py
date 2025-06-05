import numpy as np


def solve_threshold_model_euler(voltage, dt, ThresholEquation, **kwargs):
    theta = np.zeros_like(voltage)
    theta[0] = ThresholEquation.theta_inf(v=voltage[0], **kwargs)
    for i in range(1, len(voltage)):
        y = [theta[i - 1], voltage[i - 1]]
        theta[i] = theta[i - 1] + dt * ThresholEquation.ode_func(y=y, **kwargs)
    return theta


class FormDynamics:
    params_name = ['tau_theta', 'alpha', 'ka', 'ki', 'Vi', 'VT']

    @staticmethod
    def theta_inf(v: float or np.array, **kwargs):
        ka = kwargs['ka']
        ki = kwargs['ki']
        Vi = kwargs["Vi"]
        alpha = kwargs['alpha']
        VT = kwargs['VT']
        return alpha * (v - Vi) + VT + ka * np.log(1 + np.exp((v - Vi) / ki))

    @staticmethod
    def ode_func(y, **kwargs):
        theta = y[0]
        v = y[1]
        tau_theta = kwargs['tau_theta']
        dy = (FormDynamics.theta_inf(v, **kwargs) - theta) / tau_theta
        return dy
