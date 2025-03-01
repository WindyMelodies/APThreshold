import os
import pickle
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint

# # 定义微分方程
# def model(y, t):
#     return -y  # 一个简单的微分方程示例
#
# # 定义初始条件和时间点
# y0 = 1
# t = np.linspace(0, 5, 100)
#
# # 使用 odeint 求解微分方程
# result = odeint(model, y0, t)
#
# # 将结果保存到文件中
# with open('odeint_result.pkl', 'wb') as file_path:
#     pickle.dump(result, file_path)


#
# # 从文件中加载序列化的对象
# with open('odeint_result.pkl', 'rb') as file_path:
#     loaded_result = pickle.load(file_path)
#
# # 现在 loaded_result 包含了之前保存的结果
# print(loaded_result)

# data = {
#     'list1': [1, 2, 3, 4, 5],
#     'list2': ['a', 'b', 'c', 'd', 'e'],
#     'dict1': {'key1': 'value1', 'key2': 'value2'}
# }
#
# # 将数据结构保存到文件中
# with open('data_structure.pkl', 'wb') as file_path:
#     pickle.dump(data, file_path)
#
# # 从文件中加载数据结构
# with open('data_structure.pkl', 'rb') as file_path:
#     loaded_data = pickle.load(file_path)
#
# # 现在 loaded_data 包含了之前保存的数据结构
# print(loaded_data)
# dir_path = os.path.dirname(os.path.dirname(__file__))
# target_file_path = os.path.join(dir_path, 'results', 'ResponseOutput.pkl')
#
# with open(target_file_path, 'rb') as file_path:
#     loaded_data = pickle.load(file_path)
# print(loaded_data.keys())
# print(len(loaded_data['AP8']['voltage']['Vs']))
# print(loaded_data['AP8']['voltage'])
# print(loaded_data['AP8']['timeline'].keys())
# print(loaded_data['AP8']['timeline']['t'])


# target_file_path = r'D:\pythonProject\Platform_Development\results\SpikeThreshold_datas.pkl'
# with open(target_file_path, 'rb') as file_path:
#     loaded_data = pickle.load(file_path)
# print(loaded_data['All'])

# 绘制膜电压时间响应图
target_file_path_II = r"D:\放电阈值平台\平台性能测试\基于斜坡刺激的方法\(II类，beta_w=-13)Yi_adaption model(0.5,5.5,0.05)\RampStimulation.pkl"
with open(target_file_path_II, 'rb') as file:
    loaded_data_II = pickle.load(file)
target_file_path_I = r"D:\放电阈值平台\平台性能测试\基于斜坡刺激的方法\(I类，beta_w=0)Yi_adaption model(0.5,5.5,0.05)\RampStimulation.pkl"
with open(target_file_path_I, 'rb') as file:
    loaded_data_I = pickle.load(file)
# ['All']['voltage']['spike thresholds']
# ['data']['All']['Features']['Spike thresholds']  ['data']['All']['Features']['dV/dt']


# 相平面图
# with plt.style.context(['science']):
#             fig = plt.figure()
#             ax = fig.add_subplot(111)
#             ax.plot(self['voltage']['Vm'], self['derivative voltage']['dVm/dt'])
#             ax.set_xlabel('Vm(mV)')
#             ax.set_ylabel('dVm/dt(mV/ms)')
#             # ax.legend()
#             print('zhengzaihuitu')
#             fig.savefig(r'D:\pythonProject\Platform_Development\phase_plane.png', dpi=400)
#             plt.close(fig)
# 膜电压响应图
# with plt.style.context(['science']):
#             fig = plt.figure()
#             ax = fig.add_subplot(111)
#             ax.plot(self['timeline']['t'][0:10000], self['voltage']['Vm'][0:10000])
#             ax.set_xlabel('time(ms)')
#             ax.set_ylabel('Vm(mV)')
#             # ax.legend()
#             print('zhengzaihuitu')
#             fig.savefig(r'D:\pythonProject\Platform_Development\sub_figure.png', dpi=400)
#             plt.close(fig)
# 斜坡刺激法两类神经元阈值特性曲线图
with plt.style.context(['science']):
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot(loaded_data_I['data']['All']['Features']['dV/dt'], loaded_data_I['data']['All']['Features']['Spike thresholds'])
            ax.scatter(loaded_data_I['data']['All']['Features']['dV/dt'], loaded_data_I['data']['All']['Features']['Spike thresholds'],
                       c='none', marker='o', edgecolors='r', s=10)
            ax.plot(loaded_data_II['data']['All']['Features']['dV/dt'],
                    loaded_data_II['data']['All']['Features']['Spike thresholds'])
            ax.scatter(loaded_data_II['data']['All']['Features']['dV/dt'],
                       loaded_data_II['data']['All']['Features']['Spike thresholds'],
                       c='none', marker='o', edgecolors='r', s=10)
            ax.set_xlabel('dV/dt(mV/ms)')
            ax.set_ylabel('Vth(mV)')
            # ax.legend()
            print('zhengzaihuitu')
            fig.savefig(r'D:\pythonProject\Platform_Development\results\sub_figure.png', dpi=400)
            plt.close(fig)
