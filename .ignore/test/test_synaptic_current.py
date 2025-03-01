import numpy
import numpy as np
import matplotlib.pyplot as plt

from utils.tools import *

# 参数设置

gsyn = 1
ti_str = '20,40,60,80'
tau = 10  # ms
dt = 0.01

decimal_length = get_decimal_digits(dt)
ti_list = split_str_to_num(ti_str)
ti_list.sort()
t = np.linspace(0, 100, 10001)
t = numpy.around(t, decimals=decimal_length)

value_list = np.zeros_like(ti_list)
Gsyn_list = []

for i in range(len(t)):

    for j in range(len(value_list)):
        if t[i] >= ti_list[j]:
            value_list[j] = gsyn * ((t[i] - ti_list[j]) / tau) * np.exp(-(t[i] - ti_list[j]) / tau)

        else:
            value_list[j] = 0

    Gsyn = value_list.sum()
    Gsyn_list.append(Gsyn)
with plt.style.context(['science', 'ieee']):
    plt.plot(t, Gsyn_list)
    plt.xlabel('time(ms)')
    plt.ylabel('conductance')
    plt.savefig(r'E:\pythonProject\Platform_Development\123.png')
    # plt.show()
