import struct

a = [1., 2., 3., 4., 5.]

# with open('example.dat', 'wb') as f:
#     for value in a:
#         f.write(struct.pack('i', value))

with open('example.dat', 'rb') as f:
    data = f.read()
    a = struct.unpack('i' * (len(data) // 4), data)
    print(a)
