# condition_check.py - Functions for checking data source and identifying spike
import logging


def data_source_check(main_window):
    """
    This function determines the spike data source based on the interface location, distinguishing between simulation
    data and experimental recordings.
    """
    data_source = None
    voltage_option = None
    data = None
    dt = None
    if main_window.toolBox_aquire_ap.currentIndex() == 0:
        if main_window.Model:
            logging.info(
                'The window is located in the simulation section. Threshold will be calculated using simulation data.')
            data_source = 'simulation'
            voltage_option = main_window.comboBox_voltage_option.currentText()
            data = main_window.Model.data
            dt = main_window.Model.dt
    else:
        if main_window.widget_physiological_data.data:
            logging.info(
                'The window is located in the imported data section. Spike threshold '
                'will be estimated using imported experimental data.')
            data_source = main_window.widget_physiological_data.file_path.split('.')[-1]
            data = main_window.widget_physiological_data.data
            dt = main_window.widget_physiological_data.dt  # time step dt
            logging.info(f'Data source: {data_source}')
            logging.info(f'Voltage option: {voltage_option}')
            logging.info(f'Dt: {dt}')
    return data_source, voltage_option, data, dt


def data_exists_check(main_window):
    """
    Check if the "Action Potential" window has run a simulation or imported experimental recordings.
    """
    flag = 0
    if main_window.toolBox_aquire_ap.currentIndex() == 0:
        if main_window.Model:
            flag += 1
    else:
        if main_window.widget_physiological_data.data:
            flag += 1
    if flag >= 1:
        return True
    else:
        return False


def spike_check(voltage):
    """
    Identify spikes in a voltage trace. A spike is identified when the voltage exceeds 0 mV and then decrease below 0 mV.
    """
    flag = 0  # flag=0 means voltage hasn't exceeded 0, flag=1 means voltage has exceeded 0
    spike_count = 0
    spike_flag = []
    for i in range(len(voltage)):

        if flag == 0:
            if voltage[i] > 0:
                flag = 1
                pre_index = i
        if flag == 1:
            if voltage[i] < 0:
                flag = 0
                post_index = i
                spike_count += 1
                spike_flag.append((pre_index, post_index))
    spike_count = len(spike_flag)
    logging.info(f'Total number of spikes: {spike_count}')
    if spike_count == 0:
        spike = False
    else:
        spike = True
    return spike, spike_count, spike_flag
