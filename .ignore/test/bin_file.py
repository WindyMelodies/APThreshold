import os

import struct

def read_bin_file(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
        float_data = [struct.unpack('f', binary_data[i:i + 4])[0] for i in range(0, len(binary_data), 4)]
        return float_data
