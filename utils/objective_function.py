import logging

import numpy as np
from matplotlib import pyplot as plt

from utils.threshold_equation import solve_threshold_model_euler, FormDynamics


def gama_factor(time_window_sigma, r_rec, N_coinc, N_rec, N_pred):
    # time_window_sigma: unit (ms), r_rec: unit 1/ms.
    return (1 / (1 - 2 * time_window_sigma * r_rec)) * (
            (N_coinc - 2 * N_rec * time_window_sigma * r_rec) / (N_rec + N_pred))


def gama_factor_reverse(time_window_sigma, r_rec, N_coinc, N_rec, N_pred):
    value = gama_factor(time_window_sigma, r_rec, N_coinc, N_rec, N_pred)
    logging.info(f"伽马因子：{value}")
    return 1 - value


def calculate_gama_factor_reverse(x0, kwargs):
    timestamp = kwargs['timestamp']
    voltage = kwargs['voltage']
    time_threshold_estimation = kwargs['time_threshold_estimation']
    time_window_sigma=kwargs['time_window_sigma']
    ThresholdEquation=kwargs['ThresholdEquation']
    ISIs = kwargs['ISIs']
    params_name = ThresholdEquation.params_name
    for i in range(len(params_name)):
        kwargs[params_name[i]] = x0[i]
    dt = timestamp[1] - timestamp[0]
    # solve threshold equation
    theta = solve_threshold_model_euler(dt=dt, ThresholEquation=ThresholdEquation, **kwargs)
    # calculate firing rate
    r_rec = calculate_firing_rate(ISIs=ISIs)
    time_threshold_predict, threshold_predict = predict_spike_count(voltage=voltage, timestamp=timestamp, theta=theta)
    coincident_predict_index, coincident_spike_num = coincident_spike_count(
        time_threshold_predict=time_threshold_predict, time_threshold_estimation=time_threshold_estimation,
        time_window=time_window_sigma)
    logging.info("预测放电次数为{}".format(len(time_threshold_predict)))
    logging.info(f"重合放电次数为{coincident_spike_num}")
    N_rec = len(time_threshold_estimation)
    N_coinc = coincident_spike_num
    N_pred = len(time_threshold_predict)
    return gama_factor_reverse(time_window_sigma=time_window_sigma, r_rec=r_rec, N_rec=N_rec, N_pred=N_pred,
                               N_coinc=N_coinc)


def calculate_firing_rate(ISIs):
    mean_ISI = np.mean(ISIs)
    return 1. / mean_ISI


def coincident_spike_count(time_threshold_predict, time_threshold_estimation, time_window, check=True):
    """
    计算预测放电和实际放电序列中的重合放电次数
    """
    # An array store coincident predicted spike threshold corresponding to each estimated spike threshold

    right_predict_index = []  # 预测放电序列放电时刻数组中的一致性放电索引
    for i in range(len(time_threshold_estimation)):
        coincidence_count_for_one_spike = 0  # 估计所得放电序列中的单个放电的临近一致预测放电个数
        coincident_predict_spike_index = []
        for j in range(len(time_threshold_predict)):
            if abs(time_threshold_predict[j] - time_threshold_estimation[i]) <= time_window:
                coincidence_count_for_one_spike += 1
                coincident_predict_spike_index.append(j)
        # 从单个放电的所有重合放电中筛选出和实际放电最近的一次预测放电
        if coincident_predict_spike_index:
            coincidence_time_spike_predict = [time_threshold_predict[k] for k in coincident_predict_spike_index]
            argmin = np.argmin(np.abs(np.array(coincidence_time_spike_predict) - time_threshold_estimation[i]))
            right_predict_index.append(coincident_predict_spike_index[argmin])
    return right_predict_index, len(right_predict_index)


def predict_spike_count(voltage, timestamp, theta, check=False):
    """
    通过阈值模型预测膜电压放电次数，膜电压由下至上穿过阈值曲线及认为放电
    :param voltage: 膜电压时间序列
    :param timestamp: 时间戳
    :param theta: 预测阈值序列
    :param check: 选择是否通过可视化观察预测结果
    :return: time_threshold_predict（膜电压和阈值相交时刻即放电时刻），threshold_predict（预测的放电阈值）
    """
    cross = False
    time_threshold_predict = []
    threshold_predict = []
    for i in range(len(voltage)):
        if voltage[i] > theta[i]:
            if cross is False:
                cross = True
                time_threshold_predict.append(timestamp[i])
                threshold_predict.append(theta[i])
        else:
            cross = False

    # Visualization
    if check:
        plt.plot(timestamp, voltage, color="black", zorder=1)
        plt.plot(timestamp, theta, color="red", zorder=2)
        plt.scatter(time_threshold_predict, threshold_predict, zorder=3, color="green")
        plt.title(f"Predicted spike count: {len(threshold_predict)}")
        plt.show()

    return time_threshold_predict, threshold_predict
