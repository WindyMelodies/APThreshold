import pickle

from matplotlib import pyplot as plt
plt.rcParams['savefig.dpi']=400
with open(
        r"D:\放电阈值平台\性能测试\基于波形曲率的方法\小鼠初级视觉皮层，long square(1s)\SpikeThreshold_datas.pkl",
        'rb') as file:
    data = pickle.load(file)
    print(data.keys())
    for i in data.keys():
        print(data[i].keys())
    print('***')
    print(data['AP1']['voltage'].keys())
    print(data['All']['voltage'].keys())
    print(data['All']['timestamp'].keys())
    with plt.style.context(['science']):
        fig, ax = plt.subplots()
        # 取消边框
        # for key, spine in ax.spines.items():
        # 'left', 'right', 'bottom', 'top'
        # if key == 'right' or key == 'top' or key == 'left' or key == 'bottom':
        # if key == 'right' or key == 'top':
        #     spine.set_visible(False)
        for i in data.keys():
            if i =='All':
                pass
            else:
                x = data[i]['voltage']['voltage']
                y = data[i]['voltage']['dV/dt']
                ax.plot(x, y, color='#0357A2')
                # index = list(x).index(data[i]['features']['Vth'])
                # ax.scatter(data[i]['voltage']['voltage'][index],data[i]['voltage']['dV/dt'][index],s=2,color='r',zorder=10)

        plt.show()