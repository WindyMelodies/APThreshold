import pickle
import matplotlib.pyplot as plt

with open(r"D:\放电阈值平台\性能测试\基于斜坡刺激的方法\Destexhe\无IM\实验4\数据\0.3.pkl", 'rb') as f:
    data = pickle.load(f)
    print(data.keys())
    print(data['paras'])