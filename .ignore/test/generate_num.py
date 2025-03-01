import numpy as np

a = np.linspace(0.2, 4.5, 16
                )
b = ''
for i in range(len(a)):
    a[i] = round(a[i], 2)
for i in range(len(a)):
    if i == len(a) - 1:
        b = b + str(a[i])
    else:
        b = b + str(a[i]) + ','
print(b)
