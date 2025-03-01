import pickle
import sys

import numpy
import numpy as np

numpy.set_printoptions(suppress=False, threshold=numpy.inf)

with open(r"D:\ProgramingProject\python\Platform_Development\results\timestamp.pkl", 'rb') as f:
    a = pickle.load(f)
    print(a)

print(np.where(abs(a - 5.220000000000001) <= sys.float_info.epsilon))
print(len(str(5.220000000000001)))
print(8.72-3.5)