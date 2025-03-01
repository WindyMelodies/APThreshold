from encodings.utf_8 import decode
from allensdk.core import nwb_data_set
from pynwb import NWBHDF5IO
import h5py
file_path = r"D:\pythonProject\Platform_Development\datas\Generalized leaky integrate-and-fire models classify multiple neuron types\474637201_ephys.nwb"
# with h5py.File(file_path,'r') as f:
#     print(f)

# with h5py.File(file_path,'a') as f:
#     # print(decode(f['nwb_version'][()])[0].strip('NWB-'))
#     # f.attrs['nwb_version'] = decode(f['nwb_version'][()])[0].strip('NWB-')
#     print(f.attrs['nwb_version'])

file = nwb_data_set.NwbDataSet(file_name=file_path)

sweep_numbers = file.get_sweep_numbers()
sweep_data = file.get_sweep(sweep_number=10)
print(sweep_data)



print(sweep_numbers)


