import h5py

target_file = r"D:\pythonProject\Platform_Development\import_datas\Generalized leaky integrate-and-fire models classify multiple neuron types\474637201_ephys.nwb"
file = h5py.File(target_file, 'r')
print(file['nwb_version'])
print(file.keys())
# <KeysViewHDF5 ['acquisition', 'analysis', 'epochs', 'file_create_date', 'general', 'identifier', 'nwb_version', 'processing', 'session_description', 'session_start_time', 'stimulus']>
print(file['acquisition'].keys())
# <KeysViewHDF5 ['images', 'timeseries']>
print(file['acquisition']['timeseries']['Sweep_10'].keys())
# <KeysViewHDF5 ['aibs_stimulus_amplitude_pa', 'aibs_stimulus_interval', 'aibs_stimulus_name', 'bias_current', 'bridge_balance', 'capacitance_compensation', 'comments', 'data', 'description', 'electrode_name', 'initial_access_resistance', 'num_samples', 'seal', 'source', 'starting_time']>
print()
a = file['acquisition']['timeseries']['Sweep_10']['data']
# print(a.value)
print(a.attrs['unit'])
print(file['nwb_version'][()])
