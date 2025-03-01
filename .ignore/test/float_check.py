import sys

import numpy as np

a = [1.000000001, 2.00000000001, 3.0000000000000003]
print(a)
print(np.linspace(0, 100, 100001))
print(max(a))
print(np.max(a))
print(np.where(a == np.max(a))[0][0])
# print(a[np.where(a == np.max(a))])

a = np.array(a)
print(a.dtype)
if np.max(a) == max(a):
    print(True)

print(a[2])
print(len(str(a[2])))
b = float(3.00000000000000000001)

print(b)
print(type(b))
print(sys.float_info.epsilon)



