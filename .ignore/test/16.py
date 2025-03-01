import time

import numpy as np
t1 = time.time()
# 假设 initial_value 是一个 1x4 的行向量
initial_value = np.array([1, 2, 3, 4])  # 一维数组即可
# initial_value = np.array([1.1211165561165, 2.1211165561165, 3.1211165561165, 4.1211165561165])
# 创建一个 1000x4 的数组，并填充每行为 initial_value
array_2d = np.full((2, 4), initial_value)
array_2d[1,:] = [1,1,2,2]
print(array_2d)
t2 = time.time()
print(t2-t1)
# print(array_2d)
