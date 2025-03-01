import pickle
import h5py
import numpy as np

# 定义你的数据
with open(r"D:\ProgramingProject\python\Platform_Development_Yi_adaption\results\ResponseOutput.pkl", 'rb') as f:
    data = pickle.load(f)['data']
    print(data.keys())
# 创建 HDF5 文件

