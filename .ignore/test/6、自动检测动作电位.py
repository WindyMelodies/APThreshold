import pickle

import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import find_peaks, peak_widths

with open(r"D:\ProgramingProject\python\Platform_Development_Yi_adaption\results\data.pickle", "rb") as f:
    pkl_datas = pickle.load(f)
    Vm = np.array(pkl_datas['voltage']['Vm'])
    peaks, properties = find_peaks(Vm, height=0, prominence=0.5)
    width_results = peak_widths(Vm, peaks, rel_height=0.9)
    print(peaks)
    # 提取起点和终点
    start_points = width_results[2]  # 左边界位置
    end_points = width_results[3]  # 右边界位置

plt.figure(figsize=(10, 6))
t = np.linspace(0, 200, 20001)
plt.plot(t, Vm, label="Signal")
plt.plot(t[peaks], Vm[peaks], "x", label="Prominence", color='orange')
# 使用 plt.hlines 绘制宽度
plt.hlines(width_results[1], t[start_points.astype(int)], t[end_points.astype(int)],
           color="green", label="Width at Half Maximum")

# 添加图例
plt.legend()
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.title("Signal with Peaks and Widths")
plt.show()
