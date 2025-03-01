import pickle

import numpy as np
import scipy.io

# 递归地将嵌套字典转换为适用于 MATLAB 的结构体格式
unreadable_character = ['²', '³']


# def dict_to_struct(data, data_new):
#     for key, value in data.items():
#         if key == 'label':
#             pass
#         else:
#             if '²' in key or '³' in key:
#                 key_replaced = key.replace('²', '^2').replace('³', '^3')
#                 data_new[key_replaced] = value
#                 print(key_replaced)
#             else:
#                 if isinstance(value, dict):
#                     # 递归调用以转换内部字典
#                     data_new[key] = dict_to_struct(value, data_new={})
#                 elif isinstance(value, np.ndarray):
#                     # 如果是 NumPy 数组，直接保留
#                     data_new[key] = value
#                 else:
#                     # 对于非字典和数组的情况，也保持原样
#                     data_new[key] = value
#     return data_new


# 示例数据
data = {
    'k=1.0': {
        'timestamp': {
            'timestamp': np.array([0.0000e+00, 1.0000e-03, 2.0000e-03, 9.9998e+01, 9.9999e+01, 1.0000e+02]),
            'timestamp_Vth': 25.825
        },
        'voltage': {
            'Vm': np.array([-67.97472776, -67.9786562, -67.98257188, -69.61170302])
        },
        'state': {
            'n': np.array([0.15589198, 0.15589197, 0.15589195, 0.13938085])
        }
    },
    'k=2.0': {
        'timestamp': {
            'timestamp': np.array([0.0000e+00, 1.0000e-03, 2.0000e-03, 9.9998e+01, 9.9999e+01, 1.0000e+02]),
            'timestamp_Vth': 25.825
        },
        'voltage': {
            'Vm': np.array([-67.97472776, -67.9786562, -67.98257188, -69.61170302])
        },
        'state': {
            'd': np.array([0.15589198, 0.15589197, 0.15589195, 0.13938085])
        }
    }
}
# with open(r"D:\ProgramingProject\python\Platform_Development_Yi_adaption\results\ResponseOutput.pkl", 'rb') as f:
#     data = pickle.load(f)['data']
# 将数据递归转换为 MATLAB 可识别的结构体格式
data_new = {}
# matlab_data = dict_to_struct(data, data_new)
print(data_new)
print(data_new.keys())

# 保存为 .mat 文件
scipy.io.savemat('output_file.mat', data)
