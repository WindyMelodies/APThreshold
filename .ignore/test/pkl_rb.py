import pickle

import numpy as np
from matplotlib import pyplot as plt


def mark_threshold_range(array_list, Vth_list, ax):
    Vth_min = min(Vth_list)
    Vth_max = max(Vth_list)
    y_min = np.min(array_list)
    y_max = np.max(array_list)
    # ax.vlines([Vth_min, Vth_max], y_min, y_max, color='g', zorder=3)
    ax.fill_between([Vth_min, Vth_max], y_min, y_max, color='green',
                    alpha=0.3)


with open(
        r"D:\放电阈值平台\性能测试\基于波形曲率的方法\一阶导数法\Yi_adaption，step\SpikeThreshold_datas.pkl",
        'rb') as file:
    data = pickle.load(file)
    print(data.keys())
    for i in data['All'].keys():
        print(data['All'][i].keys())
    print('***')
    print(data['All'].keys())
    # with open(
    #         r"D:\放电阈值平台\性能测试\基于波形曲率的方法\一阶导数法\小鼠初级视觉皮层，long square(1s)\PhysData.pkl",
    #         'rb') as file:
    #     data1 = pickle.load(file)
    #     print(data1.keys())
    #   绘制Iinst-Vs图：Yi-adaption model
with plt.style.context(['science']):
    fig, ax = plt.subplots()
    list_AP = ['AP1', 'AP7', 'AP13', 'AP19', 'AP25', 'AP30']
    array_list = []
    Vth_list = []
    for i in list_AP:
        ax.plot(data[i]['voltage']['Vs'], data[i]['ionic_current']['Iadapt'])
        index = np.where(data[i]['voltage']['Vs'] == data[i]['features']['Vth'])[0][0]
        ax.scatter(data[i]['features']['Vth'], data[i]['ionic_current']['Iadapt'][index], color='r', marker='o',
                   zorder=10, s=2)
        Vth_list.append(data[i]['features']['Vth'])
        array_list = np.hstack((array_list, data[i]['ionic_current']['Iadapt']))
    mark_threshold_range(array_list, Vth_list, ax)
    # ax.set_xlim((-45, -13.56))
    # ax.set_ylim((28.1, 210))
    plt.savefig(r'D:\放电阈值平台\性能测试\基于波形曲率的方法\一阶导数法\Yi_adaption，step\Iadapt_Vs.png',dpi=400)

    #     ax.plot(data1['timestamp']['timestamp'], data1['voltage']['voltage'])
    #     ax.scatter(data['All']['timestamp']['timestamp_Vth'], data['All']['features']['Vth'],s=4,color='r',zorder=10)
    #     ax.set_xticks([])

    #     plt.savefig(r'D:\放电阈值平台\性能测试\基于波形曲率的方法\一阶导数法\小鼠初级视觉皮层，long square(1s)\V.png',dpi=400)
    plt.show()

    # print(data['data']['voltage'])
# with plt.style.context(['science']):
#     fig, ax = plt.subplots()
#     # 取消边框
#     for key, spine in ax.spines.items():
#         # 'left', 'right', 'bottom', 'top'
#         # if key == 'right' or key == 'top' or key == 'left' or key == 'bottom':
#         if key == 'right' or key == 'top':
#             spine.set_visible(False)
#     Vm = data['data']['k=0.4']['voltage']['Vm']
#     t = data['data']['k=0.4']['timestamp']['timestamp']
#     I = data['data']['k=0.4']['Istim']['Istim']
#     plt.plot(t[0:16000], I[0:16000], color='black', linestyle='solid')  # solid,dotted
#     plt.xticks([])
#     plt.yticks([])
#
#     plt.savefig(r'D:\放电阈值平台\论文\放电阈值量化方法图例及数据\斜坡刺激.png', dpi=400)
#     plt.show()
# AP_complete

#
# with open('E:\pythonProject\Platform_Development\(II)RampStimulation.pkl', 'rb') as file1:
#     data1 = pickle.load(file1)
#     print(data1)
# a = []
# with open(r"D:\pythonProject\Platform_Development\results\AP.pkl",
#           'rb') as file:
#     data = pickle.load(file)
#     data1 =copy.deepcopy(data)
#     for i in data1:
#         for j in data1[i]:
#             if j != 'start' and j!= 'stop':
#                 data[i].pop(j)
#     for i in data:
#         a.append(data[i]['start'])
#
# print(numpy.sort(a))
# print(data)

# with open(r"D:\pythonProject\Platform_Development\results\SpikeThreshold_datas.pkl",
#           'rb') as file:
#     data = pickle.load(file)

# print(data.keys())
# # dict_keys(['All', 'AP1', 'AP2', 'AP3', 'AP4', 'AP5', 'AP6', 'AP7', 'AP8', 'AP9', 'AP10', 'AP11', 'AP12',
# print(data['AP1'].keys())
# # dict_keys(['features', 'voltage', 'derivative voltage', 'ionic_current', 'state', 'conductance', 'timeline'])
# print(data['AP1']['features'].keys())
# print(data['AP1']['ionic_current'].keys())
# # dict_keys(['Iadapt', 'label', 'Idleak', 'Ids', 'Ik', 'Ina', 'Isleak', 'Iall'])
# print(data['AP1']['timeline'].keys())
# # dict_keys(['t', 't_SpikeThresholds', 'label'])
# print(data['AP1']['voltage'].keys())
# dict_keys(['Vs', 'label'])
# 适应性电流时间序列
# with plt.style.context(['science']):
#     fig1 = plt.figure()
#     ax = fig1.add_subplot(111)
#     for i in ['AP1', 'AP7', 'AP13', 'AP19', 'AP25', 'AP30']:
#         index = list(data[i]['timeline']['t']).index(data[i]['timeline']['t_SpikeThresholds'])
#         x = data[i]['timeline']['t']
#         y = data[i]['ionic_current']['Iadapt']
#         ax.plot(x, y)
#         threshold_point_Marker(index, ax, x, y)
#     ax.set_xlabel('t(ms)')
#     ax.set_ylabel('I$_{adapt,inst}$($\mu$A/cm$^2$)')
#     # fig1.savefig(
#     #     r'D:\放电阈值平台\平台性能测试\基于波形曲率的方法\一阶导数法\直流刺激\Yi_adaption\Iadaptinst_t.png',
#     #     dpi=400)
#     plt.show()
# 瞬时适应性电流-膜电压
# with plt.style.context(['science']):
#     fig1 = plt.figure()
#     ax = fig1.add_subplot(111)
#     x_list = []
#     y_list = []
#     Vth_list = []
#     for i in ['AP1', 'AP7', 'AP13', 'AP19', 'AP25', 'AP30']:
#         index = list(data[i]['timeline']['t']).index(data[i]['timeline']['t_SpikeThresholds'])
#         x = data[i]['voltage']['Vs']
# #         y = data[i]['derivative voltage']['dVs/dt']
#         x_list.append(copy.deepcopy(x))
#         y_list.append(copy.deepcopy(y))
#         Vth_list.append(copy.deepcopy(data[i]['features']['spike threshold']))
#         ax.plot(x, y)
#         threshold_point_Marker(index, ax, x, y)
#     # 绘制膜电压范围
#     # threshold_range_display(spike_thresholds=Vth_list, ax=ax, x_list=x_list, y_list=y_list)
#     ax.set_xlabel('Vs(mV)')
#     ax.set_ylabel('dVs/dt(mV/ms)')
#     fig1.savefig(
#         r'D:\放电阈值平台\平台性能测试\基于波形曲率的方法\一阶导数法\直流刺激\Yi_adaption\phase_plane_aps.png',
#         dpi=400)
#     plt.show()

# fig1.savefig(
#     r'D:\放电阈值平台\平台性能测试\基于波形曲率的方法\一阶导数法\直流刺激\Yi_adaption\Iinst_Vs.png',
#     dpi=400)
# plt.show()
# 瞬时钾离子电流-膜电压
# with plt.style.context(['science']):
#     fig1 = plt.figure()
#     ax = fig1.add_subplot(111)
#     x_list = []
#     y_list = []
#     Vth_list = []
#     for i in ['AP1', 'AP7', 'AP13', 'AP19', 'AP25', 'AP30']:
#         index = list(data[i]['timeline']['t']).index(data[i]['timeline']['t_SpikeThresholds'])
#         x = data[i]['voltage']['Vs']
#         y = data[i]['ionic_current']['Ik']
#         x_list.append(copy.deepcopy(x))
#         y_list.append(copy.deepcopy(y))
#         Vth_list.append(copy.deepcopy(data[i]['features']['spike threshold']))
#         ax.plot(x, y)
#         ax.set_xlim((-62.52,-24.44))
#         ax.set_ylim((-0.4,70.3))
#         threshold_point_Marker(index, ax, x, y)
#     # 绘制膜电压范围
#     threshold_range_display(spike_thresholds=Vth_list, ax=ax, x_list=x_list, y_list=y_list)
#     ax.set_xlabel('Vs(mV)')
#     ax.set_ylabel('I$_{K,inst}$($\mu$A/cm$^2$)')
#     fig1.savefig(
#         r'D:\放电阈值平台\平台性能测试\基于波形曲率的方法\一阶导数法\直流刺激\Yi_adaption\Ikinst_Vs_local.png',
#         dpi=400)
#     plt.show()
# 瞬时适应性电流+钾离子电流-膜电压
# with plt.style.context(['science']):
#     fig1 = plt.figure()
#     ax = fig1.add_subplot(111)
#     x_list = []
#     y_list = []
#     Vth_list = []
#     for i in ['AP1', 'AP7', 'AP13', 'AP19', 'AP25', 'AP30']:
#         index = list(data[i]['timeline']['t']).index(data[i]['timeline']['t_SpikeThresholds'])
#         x = data[i]['voltage']['Vs']
#         y = data[i]['ionic_current']['Ina']
#         x_list.append(copy.deepcopy(x))
#         y_list.append(copy.deepcopy(y))
#         Vth_list.append(copy.deepcopy(data[i]['features']['spike threshold']))
#         ax.plot(x, y)
#         # ax.set_xlim((-57.63,-23.17))
#         # ax.set_ylim((-3.12,42.91))
#         threshold_point_Marker(index, ax, x, y)
#     # 绘制膜电压范围
#     threshold_range_display(spike_thresholds=Vth_list, ax=ax, x_list=x_list, y_list=y_list)
#     ax.set_xlabel('Vs(mV)')
#     ax.set_ylabel('I$_{Na,inst}$($\mu$A/cm$^2$)')
#     fig1.savefig(
#         r'D:\放电阈值平台\平台性能测试\基于波形曲率的方法\一阶导数法\直流刺激\Yi_adaption\INainst_Vs.png',
#         dpi=400)
#     plt.show()
# 瞬时静电流-膜电压
# with plt.style.context(['science']):
#     fig1 = plt.figure()
#     ax = fig1.add_subplot(111)
#     x_list = []
#     y_list = []
#     Vth_list = []
#     for i in ['AP1', 'AP7', 'AP13', 'AP19', 'AP25', 'AP30']:
#         index = list(data[i]['timeline']['t']).index(data[i]['timeline']['t_SpikeThresholds'])
#         x = data[i]['voltage']['Vs']
#         y = data[i]['ionic_current']['Iall']
#         x_list.append(copy.deepcopy(x))
#         y_list.append(copy.deepcopy(y))
#         Vth_list.append(copy.deepcopy(data[i]['features']['spike threshold']))
#         ax.plot(x, y)
#         ax.set_xlim((-57.63,-23.44))
#         ax.set_ylim((-139,-67))
#         threshold_point_Marker(index, ax, x, y)
#     # 绘制膜电压范围
#     threshold_range_display(spike_thresholds=Vth_list, ax=ax, x_list=x_list, y_list=y_list)
#     ax.set_xlabel('Vs(mV)')
#     ax.set_ylabel('I$_{inst}$($\mu$A/cm$^2$)')
#     fig1.savefig(
#         r'D:\放电阈值平台\平台性能测试\基于波形曲率的方法\一阶导数法\直流刺激\Yi_adaption\Inetinst_Vs_local.png',
#         dpi=400)
#     plt.show()
# with plt.style.context(['science']):
#     fig1 = plt.figure()
#     ax = fig1.add_subplot(111)
#     for i in ['AP1', 'AP7', 'AP13', 'AP19', 'AP25', 'AP30']:
#         index = list(data[i]['timeline']['t']).index(data[i]['timeline']['t_SpikeThresholds'])
#         x = data[i]['timeline']['t']
#         y = data[i]['ionic_current']['Ina']
#         ax.plot(x,y )
#         threshold_point_Marker(index,ax,x,y)
#     ax.set_xlabel('Time(ms)')
#     ax.set_ylabel('I$_{Na,inst}$($\mu$A/cm$^2$)')
#     fig1.savefig(
#         r'D:\放电阈值平台\平台性能测试\基于波形曲率的方法\一阶导数法\直流刺激\Yi_adaption\INainst_t.png',
#         dpi=400)
#   五个动作电位的膜电压时序图
# with plt.style.context(['science']):
#     fig1 = plt.figure()
#     ax = fig1.add_subplot(111)
#     for i in ['AP1', 'AP7', 'AP13', 'AP19', 'AP25', 'AP30']:
#         index = list(data[i]['timeline']['t']).index(data[i]['timeline']['t_SpikeThresholds'])
#         x = data[i]['timeline']['t']
#         y = data[i]['voltage']['Vs']
#         ax.plot(x, y)
#         threshold_point_Marker(index, ax, x, y)
#     ax.set_xlabel('Time(ms)')
#     ax.set_ylabel('Vs(mV)')
#     fig1.savefig(
#         r'D:\放电阈值平台\平台性能测试\基于波形曲率的方法\一阶导数法\直流刺激\Yi_adaption\Vs_t_APs.png',
#         dpi=400)
#
# with plt.style.context(['science']):
#     fig1 = plt.figure()
#     ax = fig1.add_subplot(111)
#     for i in ['AP1', 'AP7', 'AP13', 'AP19', 'AP25', 'AP30']:
#         index = list(data[i]['timeline']['t']).index(data[i]['timeline']['t_SpikeThresholds'])
#         x = data[i]['timeline']['t']
#         y = data[i]['ionic_current']['Iadapt']
#         ax.plot(x,y )
#         threshold_point_Marker(index,ax,x,y)
#     ax.set_xlabel('Time(ms)')
#     ax.set_ylabel('I$_{adapt,inst}$($\mu$A/cm$^2$)')
#     fig1.savefig(
#         r'D:\放电阈值平台\平台性能测试\基于波形曲率的方法\一阶导数法\直流刺激\Yi_adaption\Iadaptinst_t.png',
#         dpi=400)

# AP_complete
# with plt.style.context(['science']):
#     fig1 = plt.figure()
#     ax = fig1.add_subplot(111)
#     for i in range(len(data['All']['voltage']['V_superposition'])):
#         ax.plot(data['All']['timestamp']['timestamp_superposition'][i], data['All']['voltage']['V_superposition'][i], linestyle='-')
#         ax.scatter(data['All']['timestamp']['timestamp_Vth_superposition'], data['All']['features']['Vth'], color='r',
#                    zorder=10,s=2)
#     ax.set_xlabel('Time(ms)')
#     ax.set_ylabel('Membrane voltage(mV)')
#     fig1.savefig(
#         r'D:\pythonProject\Platform_Development\results\AP_complete_Output.png',
#         dpi=400)
#     plt.show()
#     plt.close()
# 阈值特性曲线
# with plt.style.context(['science']):
#     fig1 = plt.figure()
#     ax = fig1.add_subplot(111)
#     ax.scatter(data['All']['features']['dV/dt'], data['All']['features']['Vth'], color='r', zorder=10, s=5)
#     Fitting(x=data['All']['features']['dV/dt'], y=data['All']['features']['Vth'], ax=ax)
#     ax.set_xlabel(unicodeit.replace('dV/dt(mV/ms)'))
#     ax.set_ylabel('Vth(mV)')
#     fig1.savefig(
#         r'D:\pythonProject\Platform_Development\results\Vth-dVdt.png',
#         dpi=400)
#       plt.show()
#     plt.close()

# datas1 = data1['data']
# 斜坡刺激电流
# with plt.style.context(['science']):
#     fig1 = plt.figure()
#     ax = fig1.add_subplot(111)
#     k_str = 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0
#     # k_str = [1.0]
# ax.plot(data['All']['timeline']['t_AP_complete'], data['All']['voltage']['AP_complete'])
#     for i in range(len(k_str)):
#         ax.plot(data['k={}'.format(k_str[i])]['timeline']['t'],
#                 data['k={}'.format(k_str[i])]['Istim'][
#                     'Istim'], linestyle='-')
#     ax.set_xlabel('Time(ms)')
#     ax.set_ylabel('Applied current($\mu$A/cm$^2$)')
#     print('zhengzaihuitu')
#     fig1.savefig(r'E:\pythonProject\latform_Development\RampInput.png', dpi=400)
#     # plt.show()
#     plt.close(fig1)

# 斜坡刺激输出膜电压图
# with plt.style.context(['science']):
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#     voltage_option = 'Vm'
#     k_str = 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5
#     # k_str = [1.0]
#     for i in range(len(k_str)):
#         ax.plot(data['k={}'.format(k_str[i])]['timeline']['t'],
#                 data['k={}'.format(k_str[i])]['voltage']['{}'.format(voltage_option)], zorder=1,
#                 linestyle='-')
#     # ax.scatter(self.data['All']['timeline']['t_Vth'], self.data['All']['Features']['Spike thresholds'],
#     #            label='Vth', marker='*', color='r', zorder=2, s=2)
#     ax.scatter(data['All']['timeline']['t_Vth'],data['All']['Features']['Spike thresholds'],
#                marker='*', color='r', zorder=2, s=2)
#     ax.set_xlabel('Time(ms)')
#     ax.set_ylabel('Membrane voltage(mV)')
#     # ax.legend()
#     print('zhengzaihuitu')
#     fig.savefig(r'E:\pythonProject\Platform_Development\RampOutput.png', dpi=400)
#     # plt.show()
#     plt.close(fig)
#   阈值特性
# with plt.style.context(['science']):
#     fig2 = plt.figure()
#     ax = fig2.add_subplot(111)
#     ax.plot(data['All']['Features']['dV/dt'], data['All']['Features']['Spike thresholds'], color='k', zorder=1)
#     ax.scatter(data['All']['Features']['dV/dt'], data['All']['Features']['Spike thresholds'],
#                c='none', marker='o', edgecolors='r', s=1, zorder=2)
#     ax.plot(datas1['All']['Features']['dV/dt'], datas1['All']['Features']['Spike thresholds'], color='k', zorder=1)
#     ax.scatter(datas1['All']['Features']['dV/dt'], datas1['All']['Features']['Spike thresholds'],
#                c='none', marker='o', edgecolors='b', s=1, zorder=2)
#     ax.set_xlabel('dV/dt(mV/ms)')
#     ax.set_ylabel('Vth(mV)')
#     print('zhengzaihuitu')
#     fig2.savefig(r'E:\pythonProject\Platform_Development\Vth_dvdt.png', dpi=400)
#     plt.close(fig2)
# 相平面图
# with plt.style.context(['science']):
#     fig2 = plt.figure()
#     ax = fig2.add_subplot(111)
#     for i in data:
#         if i == 'All':
#             pass
#         else:
#             index = list(data[i]['timestamp']['timestamp']).index(data[i]['timestamp']['timestamp_Vth'])
#             ax.plot(data[i]['voltage']['voltage'], data[i]['voltage']['dV/dt'], linestyle='-')
#             ax.scatter(data[i]['voltage']['voltage'][index],data[i]['voltage']['dV/dt'][index],marker='o',s=10, zorder=2,color='r')
#
#     fig2.savefig(r'D:\pythonProject\Platform_Development\results\phase_plane.png', dpi=400)
#     ax.set_xlabel('dV/dt(mV/ms)')
#     ax.set_ylabel('Vth(mV)')
#     plt.show()
# 膜电压响应图局部图
# with plt.style.context(['science']):
#     fig2 = plt.figure()
#     ax = fig2.add_subplot(111)
#     ax.plot(data['All']['timestamp']['timestamp'], data['All']['voltage']['voltage'], linestyle='-')
#     ax.scatter(data['All']['timestamp']['timestamp_Vth'], data['All']['features']['Vth'], marker='o', s=10, zorder=2,
#                color='r')
# for i in data:
#     if i == 'All':
#         pass
#     else:
#         index = list(data[i]['timestamp']['timestamp']).index(data[i]['timestamp']['timestamp_Vth'])
#         ax.plot(data[i]['voltage']['voltage'], data[i]['voltage']['dV/dt'], linestyle='-')
#         ax.scatter(data[i]['voltage']['voltage'][index],data[i]['voltage']['dV/dt'][index],marker='o',s=10, zorder=2,color='r')


# ax.set_xlabel('Time(ms)')
# ax.set_ylabel('Vth(mV)')
# ax.set_xlim((1000, 2050))
# ax.set_ylim((-75, 23))
# fig2.savefig(r'D:\pythonProject\Platform_Development\results\V_local.png', dpi=400)
# plt.show()
