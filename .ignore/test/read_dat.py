# 读取二进制文件
file_path = "C:/xppall/test.dat"
with open(file_path, 'rb') as file:
    data = file.read()  # 读取整个文件
    data = data[0:100]
    print(data)  # 以字节格式输出内容
