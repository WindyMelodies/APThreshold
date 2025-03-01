import matplotlib.pyplot as plt

import pickle

import numpy as np

with open(r"D:\放电阈值平台\性能测试\基于斜坡刺激的方法\HHModel\实验17\RampStimulation.pkl", 'rb') as f:
    data_1 = pickle.load(f)
    data_1 = data_1['data']

    dVdt = np.array(data_1['All']['features']['dV/dt'])
    a = np.abs(dVdt - 1)
    b = np.abs(dVdt - 4.5)
    print(a)
    print(b)
    index_left = a.argmin()
    index_right = b.argmin()
    print(index_right, index_left)
