import pandas as pd
import json

#  测试半激活电压的改变
import json
import pickle
from bisect import bisect_left
import matplotlib.pyplot as plt
import numpy as np

from models.Izhikevichmodel import Model

import pickle

import numpy as np
import scipy.io

# 递归地将嵌套字典转换为适用于 MATLAB 的结构体格式
unreadable_character = ['²', '³']


def delete_label(data, data_new):
    for key, value in data.items():
        if key == 'label':
            pass
        else:
            if isinstance(value, dict):
                # 递归调用以转换内部字典
                data_new[key] = delete_label(value, data_new={})
            elif isinstance(value, np.ndarray):
                # 如果是 NumPy 数组，直接保留
                data_new[key] = [None if np.isnan(x) else x for x in value]
    return data_new

with open(r"D:\ProgramingProject\python\Platform_Development_Yi_adaption\results\ResponseOutput.pkl", 'rb') as f:
    data = pickle.load(f)['data']



data_new = {}
data_1 = delete_label(data=data, data_new=data_new)



# 转换 JSON 数据为 DataFrame
# 将嵌套的字典展平并合并到一个 DataFrame 中
df = pd.json_normalize(data_1)

# 导出为 CSV 文件
df.to_csv('output.csv', index=False)
