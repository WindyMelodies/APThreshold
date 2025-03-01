import time

a = time.time()
with open(r"C:\Users\win10\Desktop\123.txt", 'r') as f:
    voltage = []
    for line in f:
        voltage.append(float(line))
    print(voltage)
b = time.time()
