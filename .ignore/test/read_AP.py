

import numpy as np
import pickle

# 读取AP.pkl
with open(r"D:\ProgramingProject\python\Platform_Development_Yi_adaption\results\AP.pkl", 'rb') as f:
    a = pickle.load(f)
    b = {}
    for i in a:
        b[i] = {'start':a[i]['start'],'stop':a[i]['stop']}
    print(b)


