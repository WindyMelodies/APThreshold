"""Class for importing experimental recordings."""
import logging
import os

import matplotlib.pyplot as plt
import scipy.io as sio
import struct
import numpy as np
from utils.curvature_based_method import calculate_all_ISI, calculate_extracted_AP_ISI, peak_time
from utils.condition_check import spike_check
import unicodeit
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from .ui_import_data_window import Ui_import_datas_widget
from utils.tools import derivative, round_timestamp, get_decimal_digits


class ImportDataWidget(Ui_import_datas_widget, QWidget):
    """
    This widget provides functionality for importing and processing various data files (.dat, .txt, .bin, .mat).
    It handles the following tasks:
    1. Reading voltage data from files.
    2. Acquiring the sampling frequency from user interface.
    3. Generating timestamps and computing the first, second, and third derivatives of the membrane voltage.
    4. Storing all data in the `data` dictionary.
    5. File format validation after importing data.
    6. When the "OK" button is clicked:
        - If the sampling frequency is non-zero, the software will process the data by generating timestamps and
          calculating derivatives.
        - If the sampling frequency is zero, an error message will prompt the user not to proceed with the data reading.
    """
    flag_for_fig_window = 'import_datas'

    def __init__(self, main_window):
        super().__init__()
        self.data = None
        self.file_path = None
        self.figure_set = None
        self.figure_set_origin = None
        self.dt = None
        self.main_window = main_window
        self.setupUi(self)
        self.lineEdit_minimal_ISI.setStyleSheet("background-color: silver; color: black;")
        self.lineEdit_maximal_ISI.setStyleSheet("background-color: silver; color: black;")
        self.lineEdit_spik_count.setStyleSheet("background-color: silver; color: black;")
        self.lineEdit_import_file.setStyleSheet("background-color: silver; color: black;")
        self.setAcceptDrops(True)
        self.set_signal_slot()
        self.get_figure_set_origin()

    def set_signal_slot(self):
        """
        Connect the signals from the UI elements to their respective slot functions.
        """
        self.pushButton_import_file.clicked.connect(self.get_datafile_path)
        self.pushButton_other_file_run.clicked.connect(self.read_data_file)

    def get_datafile_path(self):
        """
        Open a file dialog to allow the user to select a data file, and read data.
        """
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        data_path = os.path.join(os.path.abspath('.'), 'data')
        file_dialog.setDirectory(data_path)
        file_dialog.setNameFilter('(*.dat *.mat *.txt *.bin)')
        file_dialog.show()
        if file_dialog.exec():
            self.file_path = file_dialog.selectedFiles()[0]
            if self.file_path:
                self.lineEdit_import_file.setText(os.path.split(self.file_path)[1])
                self.read_data_file()
        file_dialog.deleteLater()

    def read_data_file(self):
        """
        Read the selected data file and process it based on its format, and calculate inter-spike interval (ISI).
        """

        if self.file_path:
            file_format = self.file_path.split('.')[-1]
            logging.info(f'File format: {file_format}')
            if self.sender().objectName() == 'pushButton_other_file_run':
                if self.spinBox_sample_rate.value() == 0:
                    msg_box = QMessageBox(QMessageBox.Information, 'Message', 'Sampling rate is 0Hz!')
                    msg_box.exec()
                else:
                    self.dt = 1000 / (self.spinBox_sample_rate.value() * 1000)
                    if file_format == 'txt':
                        self.data = self.return_data(self.get_txt_data(), self.spinBox_sample_rate.value() * 1000)
                    if file_format == 'dat':
                        self.data = self.return_data(self.get_dat_data(), self.spinBox_sample_rate.value() * 1000)
                    if file_format == 'bin':
                        self.data = self.return_data(self.get_bin_data(), self.spinBox_sample_rate.value() * 1000)
                    if file_format == 'mat':
                        self.data = self.return_data(self.get_mat_data(), self.spinBox_sample_rate.value() * 1000)
                    spike, spike_count, spike_flag = spike_check(self.data['voltage']['voltage'])
                    # ISI calculation
                    ISI = np.array([])
                    voltage = self.data['voltage']['voltage']
                    sample_rate = self.spinBox_sample_rate.value() * 1000
                    timestamp = np.arange(len(voltage)) * 1000 / sample_rate
                    dt = 1000 / sample_rate
                    timestamp = round_timestamp(timestamp, dt)
                    if spike:
                        if spike_count >= 2:
                            list_voltage_max, list_voltage_max_moment, list_index_voltage_max = peak_time(
                                spike_flag=spike_flag,
                                voltage=voltage,
                                timestamp=timestamp)

                            ISI, list_voltage_max = calculate_all_ISI(
                                list_voltage_max_moment=list_voltage_max_moment,
                                list_voltage_max=list_voltage_max)
                    if len(ISI):
                        max_ISI = round(max(ISI), get_decimal_digits(dt))
                        min_ISI = round(min(ISI), get_decimal_digits(dt))
                        self.lineEdit_spik_count.setText(str(spike_count))
                        self.lineEdit_minimal_ISI.setText(str(min_ISI))
                        self.lineEdit_maximal_ISI.setText(str(max_ISI))
                        # Calculate coefficient variation of ISIs.
                        # mean = np.mean(ISI)
                        # std = np.std(ISI)
                        # cv_isi = std / mean

        else:
            msg_box = QMessageBox(QMessageBox.Information, 'Message', 'Please import data！')
            msg_box.exec()

    def get_txt_data(self):
        voltage = []
        if self.comboBox_unit_voltage.currentIndex() == 0:
            with open(self.file_path, 'r') as f:
                for line in f:
                    voltage.append(float(line) * 1000)
        else:
            with open(self.file_path, 'r') as f:
                for line in f:
                    voltage.append(float(line))
        return voltage

    def get_dat_data(self):
        with open(self.file_path, 'rb') as file:
            binary_data = file.read()
            float_data = [struct.unpack('f', binary_data[i:i + 4])[0] for i in range(0, len(binary_data), 4)]
            if self.comboBox_unit_voltage.currentIndex() == 0:
                voltage = np.array(float_data) * 1000
            else:
                voltage = np.array(float_data)
        return voltage

    def get_mat_data(self):
        voltage = []
        try:
            mat_data = sio.loadmat(self.file_path)
            if 'voltage' in mat_data:
                voltage = mat_data['voltage']
                if self.comboBox_unit_voltage.currentIndex() == 0:
                    voltage = voltage * 1000
            else:
                logging.info("Error: 'voltage' not found in the .mat file.")
        except Exception as e:
            logging.info(f"Error reading .mat file: {e}")
        return voltage

    def get_bin_data(self):
        with open(self.file_path, 'rb') as file:
            binary_data = file.read()
            float_data = [struct.unpack('f', binary_data[i:i + 4])[0] for i in range(0, len(binary_data), 4)]
            float_data = np.array(float_data) * 1000
            return float_data

    def update_adc_unit(self):
        index = self.comboBox_ADC_chanel.currentIndex()
        self.lineEdit_ADC_unit.setText(self.abf.adcUnits[index])

    def get_figure_set_origin(self):
        fig_1_1 = {}
        fig_1_2 = {}
        fig_2_1 = {}
        fig_2_2 = {}
        self.figure_set_origin = {(1, 1): fig_1_1, (1, 2): fig_1_2, (2, 1): fig_2_1, (2, 2): fig_2_2}
        if self.main_window.figure_set_experiment == None:
            self.main_window.figure_set_experiment = self.figure_set_origin.copy()
            self.figure_set = self.main_window.figure_set_experiment
        else:
            self.figure_set = self.main_window.figure_set_experiment

    @staticmethod
    def return_data(voltage, sample_rate):
        dt = 1000. / sample_rate
        timestamp = np.linspace(0, (len(voltage) - 1) * dt, len(voltage))
        timestamp = round_timestamp(timestamp, dt)
        dvdt1, dvdt2, dvdt3 = derivative(timestamp, voltage)
        data = {
            'voltage': {
                'voltage': voltage,
                unicodeit.replace('dV/dt'): dvdt1,
                unicodeit.replace('d^2V/dt^2'): dvdt2,
                unicodeit.replace('d^3V/dt^3'): dvdt3
            },
            'timestamp': {'timestamp': timestamp}
        }
        return data
