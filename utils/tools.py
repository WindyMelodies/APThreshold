import copy
import importlib
import json
import logging
import os
import pickle
import re
import h5py
import scipy
from PySide6.QtWidgets import QFileDialog
import numpy as np


def add_item_to_combox(name_list, combobox):
    for i in name_list:
        combobox.addItem(i)


def get_voltage_names(compartment_num):
    if compartment_num == 1:
        return ['Vm']
    elif compartment_num == 2:
        return ['Vs', 'Vd']
    else:
        name_list = []
        for i in range(compartment_num):
            name = 'V' + '{}'.format(i + 1)
            name_list.append(name)
        return name_list


def get_current_names(compartment_num):
    if compartment_num == 1:
        return ['Istim']
    elif compartment_num == 2:
        return ['Is', 'Id']
    else:
        name_list = []
        for i in range(compartment_num):
            name = 'I' + '{}'.format(i + 1)
            name_list.append(name)
        return name_list


def get_model_names():
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models')
    name_list = []
    for filename in os.listdir(path):
        if filename.endswith('model.py') or 'model' in filename:
            name_list.append(filename.strip('.py'))
    return name_list


def get_model_attributes(model_name):
    model = importlib.import_module(model_name)
    number_of_compartment = model.Model.number_of_compartment
    dynamic_variables = model.Model.dynamic_variables
    initial_value = model.Model.initial_value
    return {'number_of_compartment': number_of_compartment, 'dynamic_variables': dynamic_variables,
            'initial_value': initial_value}


def split_str_to_num(str):
    str = re.split(',|，|。', str)
    str_filter = []
    for i in str:
        if i == '':
            pass
        else:
            str_filter.append(float(i))
    return str_filter


def get_decimal_digits(num):
    str_num = format(num, 'f')
    if '.' in str_num:
        a, b = str_num.split('.')
        return len(b)
    else:
        return 0


def round_timestamp(timestamp, dt):
    decimal_digit = get_decimal_digits(dt)
    return np.around(timestamp, decimal_digit)


def derivative(t, V):
    t = copy.deepcopy(t)
    V = copy.deepcopy(V)
    dVdt1 = np.diff(V) / np.diff(t)
    t = np.delete(t, 0)
    dVdt2 = np.diff(dVdt1) / np.diff(t)
    t = np.delete(t, 0)
    dVdt3 = np.diff(dVdt2) / np.diff(t)
    return np.append(np.full(1, np.nan), dVdt1), np.append(np.full(2, np.nan), dVdt2), np.append(np.full(3, np.nan),
                                                                                                 dVdt3)


def get_AP_or_K_names(data):
    name_list = []
    for i in data:
        if i == 'All':
            pass
        else:
            name_list.append(i)
    return name_list


def get_voltage_from_AP_data(AP_data, AP_name, data_source, voltage_option=None):
    voltage = None
    if data_source == 'simulation':
        voltage = AP_data[AP_name]['voltage']['{}'.format(voltage_option)]
    if data_source == 'txt' or data_source == 'bin' or data_source == 'dat' or data_source == 'mat':
        voltage = AP_data[AP_name]['voltage']['voltage']
    return voltage


def get_voltage_from_data(data, data_source, voltage_option=None):
    voltage = None
    if data_source == 'simulation':
        voltage = data['voltage'][voltage_option]
    if data_source == 'txt' or data_source == 'bin' or data_source == 'dat' or data_source == 'mat':
        voltage = data['voltage']['voltage']
    return voltage


def get_timestamp_from_data(data):
    timestamp = data['timestamp']['timestamp']
    return timestamp


def get_max_num(array):
    return max(array[array != None])


def save_to_mat(file_path, data):
    def dict_to_struct(data, data_new):
        for key, value in data.items():
            if key == 'label':
                pass
            else:
                if '²' in key or '³' in key:
                    key_replaced = key.replace('²', '^2').replace('³', '^3')
                    data_new[key_replaced] = value
                else:
                    if isinstance(value, dict):
                        if '=' in key or '.' in key:
                            data_new[key.replace('=', '_').replace('.', '_')] = dict_to_struct(value, data_new={})
                        else:
                            data_new[key] = dict_to_struct(value, data_new={})
                    elif isinstance(value, np.ndarray):
                        data_new[key] = value
        return data_new

    data_new = {}
    _ = dict_to_struct(data, data_new)
    scipy.io.savemat(file_path, data_new)


def save_to_pickle(file_path, data):
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)


def save_to_json(file_path, data):
    def delete_label(data, data_new):
        for key, value in data.items():
            if key == 'label':
                pass
            else:
                if isinstance(value, dict):
                    data_new[key] = delete_label(value, data_new={})
                elif isinstance(value, np.ndarray):
                    data_new[key] = [None if np.isnan(x) else x for x in value]
        return data_new

    data_new = {}
    with open(file_path, 'w') as json_file:
        json.dump(delete_label(data, data_new), json_file, indent=4)


def save_to_hdf5(file_path, data):
    with h5py.File(file_path, 'w') as f:
        def recursively_save_dict_contents_to_group(h5file, path, dic):
            for key, item in dic.items():
                if key == 'label':
                    pass
                else:
                    if isinstance(item, dict):
                        group = h5file.create_group(f"{path}/{key}")
                        recursively_save_dict_contents_to_group(h5file, f"{path}/{key}", item)
                    else:
                        if '/' in key:
                            key_new = key.replace('/', '_')
                            h5file.create_dataset(f"{path}/{key_new}", data=np.array(item))
                        else:
                            h5file.create_dataset(f"{path}/{key}", data=np.array(item))

        recursively_save_dict_contents_to_group(f, '/', data)


def open_save_data_window(data):
    """
    Save data to different file formats
    """
    file_filters = "MAT Files (*.mat);;HDF5 Files (*.hdf5);;JSON Files (*.json);;Pickle Files (*.pickle)"
    default_file_name = 'data.mat'
    options = QFileDialog.Options()
    default_dir = os.path.join(os.path.abspath('.'), 'results', default_file_name)
    file_path, _ = QFileDialog.getSaveFileName(None, "Save File", default_dir, file_filters, options=options)

    if file_path:
        logging.info(f"File path selected by user: {file_path}")
        if file_path.endswith('hdf5'):
            save_to_hdf5(file_path, data)
        elif file_path.endswith('pickle'):
            save_to_pickle(file_path, data)
        elif file_path.endswith('mat'):
            save_to_mat(file_path, data)
        elif file_path.endswith('json'):
            save_to_json(file_path, data)
    else:
        logging.info("No file is selected.")
