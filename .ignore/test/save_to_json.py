#  测试半激活电压的改变
import json
import pickle
import numpy as np

# 递归地将嵌套字典转换为适用于 MATLAB 的结构体格式
unreadable_character = ['²', '³']





with open(r"D:\ProgramingProject\python\Platform_Development_Yi_adaption\results\ResponseOutput.pkl", 'rb') as f:
    data = pickle.load(f)['data']

data_new = {}
data_1 = delete_label(data=data, data_new=data_new)


