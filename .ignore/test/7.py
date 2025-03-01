import os
import pickle
list_dir = os.listdir(r'D:\放电阈值平台\性能测试\基于斜坡刺激的方法\HHModel\实验8\数据')
print(list_dir)
for i in range(len(list_dir)):
    list_dir[i] = os.path.join('D:\放电阈值平台\性能测试\基于斜坡刺激的方法\HHModel\实验8\数据',list_dir[i])
data_list = []
for i in list_dir:
    with open(i, 'rb') as f:
        data = pickle.load(f)
        print(data['paras'])