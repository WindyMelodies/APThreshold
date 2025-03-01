import pickle

file_path = r"D:\放电阈值平台\性能测试\基于斜坡刺激的方法\Izhikevich(2D)\试验7\RampStimulation.pkl"
with open(file_path, 'rb') as f:
    data = pickle.load(f)
    for i in data['data'].keys():
        if i != 'All':
            print(i, '---', data['data'][i]['features']['dV/dt'])

    # print(data)
