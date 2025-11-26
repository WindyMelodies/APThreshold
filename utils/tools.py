import copy
import importlib
import json
import logging
import os
import pickle
import re
import h5py
import scipy
import unicodeit
from PySide6.QtWidgets import QFileDialog, QMessageBox, QAbstractItemView, QHeaderView, QTableWidgetItem
import numpy as np
from scipy.signal import find_peaks
from utils.threshold_equation import FormOne, FormTwo, FormThree


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
    path = os.path.join(os.path.abspath('.'), 'models')
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
    if data_source == 'txt' or data_source == 'bin' or data_source == 'dat' or data_source == 'mat' or data_source == 'pkl':
        voltage = AP_data[AP_name]['voltage']['voltage']
    return voltage


def get_voltage_from_data(data, data_source, voltage_option=None):
    voltage = None
    if data_source == 'simulation':
        voltage = data['voltage'][voltage_option]
    if data_source == 'txt' or data_source == 'bin' or data_source == 'dat' or data_source == 'mat'or data_source == 'pkl' :
        voltage = data['voltage']['voltage']
    return voltage


def get_derivative_voltage_from_data(data, data_source, voltage_option=None):
    if data_source == 'simulation':
        dVdt_1 = data['derivative voltage'][unicodeit.replace(
            'd{}/dt'.format(voltage_option))]
    if data_source == 'txt' or data_source == 'bin' or data_source == 'dat' or data_source == 'mat'or data_source == 'pkl' :
        dVdt_1 = data['voltage'][unicodeit.replace('dV/dt')]
    return dVdt_1


def get_timestamp_from_data(data):
    timestamp = data['timestamp']['timestamp']
    return timestamp


def get_max_num(array):
    max = -np.inf
    for i in range(len(array)):
        if array[i] == None or array[i] == np.nan:
            pass
        else:
            if max < array[i]:
                max = array[i]
    return max


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


def identify_single_aps(index_peaks, voltage, dVdt1, timestamp):
    ap_start_stop_index = []
    if len(index_peaks) == 0:
        msg_box = QMessageBox(QMessageBox.Information, 'Message', 'No spike data!')
        msg_box.exec()
        return ap_start_stop_index

    spike_timing = timestamp[index_peaks]
    for i in range(len(index_peaks)):
        spike_num = i
        # identify AP onset
        if spike_num == 0:
            dV_before_peak = dVdt1[timestamp <= spike_timing[spike_num]]
            left_ind_front = 0
        else:
            dV_before_peak = dVdt1[
                (timestamp <= spike_timing[spike_num]) & (timestamp >= spike_timing[spike_num - 1])]
            left_ind_front = np.argmax(timestamp >= spike_timing[spike_num - 1])
        min_dv = np.min(dV_before_peak[2:])
        max_dv_ind = np.argmax(dV_before_peak[1:]) + 1
        dV_before_peak = dV_before_peak[1:max_dv_ind]
        # 寻找 dv 最后上升到dv最小值的一半时的索引
        list_temp = np.where(dV_before_peak <= min_dv * 0.5)[0]
        if len(list_temp):
            left_ind_1 = list_temp[-1]
        else:
            left_ind_1 = 0
        left_ind_2 = np.where(dV_before_peak[left_ind_1:] > 0)[0][0]
        start_index = left_ind_front + left_ind_1 + left_ind_2
        # if start_index==0:
        #     start_index+=2
        # identify AP offset
        if spike_num == len(index_peaks) - 1:
            index_after_peak = timestamp >= timestamp[index_peaks[spike_num]]
        else:
            index_after_peak = (timestamp >= timestamp[index_peaks[spike_num]]) & (
                    timestamp <= timestamp[index_peaks[spike_num + 1]])
        dv_after_peak = dVdt1[index_after_peak]
        v_after_peak = voltage[index_after_peak]
        timestamp_after_peak = timestamp[index_after_peak]
        index = np.array([])
        i_loop = 0
        max_loop = 10
        reverse_v_after_peak = -v_after_peak
        peak_prominence = 1
        while index.size == 0:
            index = find_peaks(x=reverse_v_after_peak, prominence=peak_prominence)[0]
            i_loop += 1
            peak_prominence = peak_prominence / 10
            if i_loop >= max_loop:
                break
        if i_loop >= max_loop:
            max_dv = max(dv_after_peak)
            min_dv_index = np.argmin(dv_after_peak)
            dv_after_peak = dv_after_peak[min_dv_index:]
            right_index_1 = np.where(dv_after_peak >= max_dv * 0.3)[0]
            if right_index_1.size == 0:
                right_index_1 = len(dv_after_peak) - 1
            else:
                right_index_1 = right_index_1[0]
            # right_index_2 = np.where(dv_after_peak[0:right_index_1] <= 0)[0][0]
            right_index_2 = 0
            right_index = min_dv_index + right_index_2
        else:
            right_index = index[0]
        stop_index = np.where(timestamp >= timestamp[index_peaks[spike_num]])[0][0] + right_index
        ap_start_stop_index.append((start_index, stop_index))
        # print("self.AP_start_stop_index_list", self.AP_start_stop_index_list)
        # stop_index = round( stop_index + (stop_index - left_ind) * 0.05, 0);
    return ap_start_stop_index


def detect_spike(voltage):
    index_peaks, _ = find_peaks(voltage, height=0, prominence=10, distance=10,
                                width=None)
    print("get_index_peaks：当前膜电压序列中存在放电{}次。".format(len(index_peaks)))
    return index_peaks


def get_threshold_equation(combobox_index):
    if combobox_index == 1:
        return FormOne
    elif combobox_index == 2:
        return FormTwo
    elif combobox_index==3:
        return FormThree

def get_kwargs_for_optimization():
    pass

def explained_variance(Vth_est, Vth_pred):
    average_threshold_estimated = np.average(Vth_est)
    part1 = 0.
    part2 = 0.
    for i in range(len(Vth_pred)):
        part1 += (Vth_pred[i]-Vth_est[i])**2
        part2 += (Vth_est[i]-average_threshold_estimated)**2
    ev = 1. - (part1 / part2)
    return ev

def false_alarms(time_window, timestamp, voltage, theta):
    recorded_spike_numbers = 0
    if recorded_spike_numbers == 0:

        return np.nan

def str_in_dir(a_str, a_dict):
    temp = []
    for i in a_dict.keys():
        if a_str in i:
            temp.append(i)
    if len(temp)>0:
        return True
    else:
        return False

def float_equality_judgement(num, array):
    if not num:
        return np.nan
    array = np.asarray(array)
    mask = ~np.isnan(array)  # 保留不是 nan 的元素
    if not np.any(mask):
        raise ValueError("All elements are NaN.")
    valid_array = array[mask]
    min_index_in_valid = np.argmin(np.abs(valid_array - num))

    # 映射回原始 array 的索引
    original_indices = np.where(mask)[0]
    return original_indices[min_index_in_valid]

def add_features_to_TableWidget_threshold_equation(tableWidget_features, data):
    """
    Add calculated spike features to table widget.
    """
    tableWidget_features.clear()

    font = tableWidget_features.horizontalHeader().font()
    font.setBold(True)
    tableWidget_features.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # Set the vertical title of the table
    tableWidget_features.setRowCount(len(data) - 1)
    row = 0
    for i in data:
        if i == 'All':
            pass
        else:
            item = QTableWidgetItem()
            item.setText(i)
            tableWidget_features.setVerticalHeaderItem(row, item)
            row += 1
    # Set the horizontal title of the table
    # Vth: spike threshold, t_Vth: time of spike threshold, ISI: inter-spike interval, dV/dt:rate of depolarization
    # <V>: average voltage preceding to spike
    col_names = ['Vth', 't_Vth', 'ISI', 'dV/dt', '<V>']
    col_count = 5
    tableWidget_features.setColumnCount(col_count)
    col = 0
    for i in col_names:
        item = QTableWidgetItem()
        item.setText(i)
        tableWidget_features.setHorizontalHeaderItem(col, item)
        tableWidget_features.setColumnWidth(col, 50)
        col += 1
    row = 0
    for i in data:
        if i == 'All':
            pass
        else:
            item_Vth = QTableWidgetItem()
            item_Vth.setText(str(round(data[i]['features']['Vth_pred'][0], 3)))
            tableWidget_features.setItem(row, 0, item_Vth)
            item_t_Vth = QTableWidgetItem()
            item_t_Vth.setText(str(round(data[i]['timestamp']['timestamp_Vth_pred'][0], 3)))
            tableWidget_features.setItem(row, 1, item_t_Vth)
            if 'ISI' in data[i]['features']:
                item_ISI = QTableWidgetItem()
                item_ISI.setText(str(round(data[i]['features']['ISI'][0], 3)))
                tableWidget_features.setItem(row, 2, item_ISI)
            if 'dV/dt_pred' in data[i]['features']:
                item_dVdt = QTableWidgetItem()
                item_dVdt.setText(str(round(data[i]['features']['dV/dt_pred'][0], 3)))
                tableWidget_features.setItem(row, 3, item_dVdt)
            if '<V>_pred' in data[i]['features']:
                item_average_V = QTableWidgetItem()
                item_average_V.setText(str(round(data[i]['features']['<V>_pred'][0], 3)))
                tableWidget_features.setItem(row, 4, item_average_V)
            row += 1
    tableWidget_features.horizontalHeader().setStretchLastSection(True)  # Stretch the last column to fill the space
    tableWidget_features.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


def remove_nan_pairs(X, Y):
    X = np.asarray(X)
    Y = np.asarray(Y)

    # 构造掩码：仅当 X 和 Y 在同一位置都不是 NaN 时为 True
    mask = ~np.isnan(X) & ~np.isnan(Y)

    # 同时过滤 X 和 Y
    X_clean = X[mask]
    Y_clean = Y[mask]

    return X_clean, Y_clean