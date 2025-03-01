import numpy as np
import pickle

with open(r"D:\ProgramingProject\python\Platform_Development_Yi_adaption\results\data.pickle", 'rb') as f:
    data = pickle.load(f)

    print(data['k=1.0'].keys())
    print(data['k=1.0']['timestamp'])
    V = data['k=1.0']['voltage']['Vm']
    print(np.mean(V[0:5938]))