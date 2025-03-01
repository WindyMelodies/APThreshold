import os
import matplotlib.pyplot as plt
import pickle

list_dir = os.listdir(r'D:\放电阈值平台\性能测试\基于斜坡刺激的方法\Destexhe\无IM\实验4\数据')
print(list_dir)
for i in range(len(list_dir)):
    list_dir[i] = os.path.join('D:\放电阈值平台\性能测试\基于斜坡刺激的方法\Destexhe\无IM\实验4\数据', list_dir[i])
data_list = []
for i in list_dir:
    with open(i, 'rb') as f:
        data = pickle.load(f)
        data_list.append(data['paras'])
for i in data_list:
    print(i)