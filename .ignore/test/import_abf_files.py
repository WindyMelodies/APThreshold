import numpy as np

print(np.array(np.arange(20000) * 5e-5, dtype=np.float64))
import matplotlib.pyplot as plt
import pyabf

abf = pyabf.ABF(r"D:\pythonProject\Platform_Development\abfs\ic-ramp-ap.abf")
datas = abf.data_I
data_time = abf.abfDateTime  # abf生成日期
print(datas[0])
print(len(datas[0]))

# plt.plot(data)
# chanel:1
# sweep:11
# 获得abf文件的通道数目和sweep数量
print('通道数', abf.channelCount)
print('adc通道', abf.adcNames)
print('dac通道', abf.dacNames)
print('sweep个数', abf.sweepCount)
print('采样频率', abf.sampleRate)
print('刺激电流信息', abf.sweepEpochs)
print('单个sweep时长', abf.sweepIntervalSec)
print()
abf.setSweep(sweepNumber=10, channel=0)
# print(abf.sweepX)
# print(abf.sweepY)

print(0.1415646546465)
plt.plot(abf.sweepX, abf.sweepC)
plt.ylabel(abf.sweepLabelC)
plt.xlabel(abf.sweepLabelX)
plt.show()
print(np.array(np.arange(20000) * 5e-5, dtype=np.float64))
