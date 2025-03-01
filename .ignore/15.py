import copy
import pickle
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression



def linear_fitting(x, y, axes):
    R = np.corrcoef(x, y)[0, 1]
    x = np.array(x)
    y = np.array(y)
    model = LinearRegression()
    model.fit(x.reshape(-1, 1), y.reshape(-1, 1))
    coef = model.coef_[0, 0]
    intercept = model.intercept_[0]
    X = x
    Y = X * coef + intercept
    axes.plot(X, Y, color="black")
    # axes.set_title('slpoe={},r={}'.format(round(coef, 3), round(R, 3)), loc='right')
    print('拟和直线方程为：', 'y={}x+{}'.format(coef, intercept))
    print('x与y相关性：', R)


with open(r"D:\放电阈值平台\性能测试\基于波形曲率的方法\小鼠初级视觉皮层，long square(1s)\SpikeThreshold_datas.pkl",
          'rb') as file:
    data = pickle.load(file)
    print(data.keys())
    for i in data.keys():
        print(data[i].keys())
    print('***')
    print(data['All']['voltage'].keys())

with plt.style.context(['science']):
    plt.rcParams['savefig.dpi']=400
    fig, ax = plt.subplots()
    Vth = data['All']['features']['Vth']
    dVdt = data['All']['features']['dV/dt']
    ISI = data['All']['features']['ISI']
    average_V = data['All']['features']['<V>']
    ax.scatter(ISI, Vth, zorder=10, s=6, color='red')
    linear_fitting(ISI, Vth, ax)
    # plt.savefig(r'D:\放电阈值平台\论文\性能测试图例\一阶导数方法，生理数据\Vth_average_V.png',dpi=400)
    plt.show()

