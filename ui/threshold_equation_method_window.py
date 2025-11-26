import copy
import numpy as np
from ui.configure_equation_parameters_workflow1 import ConfigureEquationParametersWindow
from ui.configure_stimulation_window import ConfigureStimulationWindow
from ui.html_mathml import html_mathml_1, html_mathml_2, html_mathml_3
from ui.set_fig_window_Vth import SetFigWindowVth
from ui.ui_threshold_equation_method_workflow_2_panel import Ui_workflow_2_panel
from ui.ui_threshold_euqation_method_main_window import Ui_threshold_euqation_method_main_window
from ui.ui_threshold_equation_method_workflow_1_panel import Ui_workflow_1_panel
from PySide6.QtWidgets import QWidget, QMessageBox, QAbstractItemView, QTableWidgetItem, QHeaderView
from utils.condition_check import data_exists_check, check_equation_params_consistent, data_source_check, \
    identify_APs_consistent, spike_check
from utils.curvature_based_method import peak_time, calculate_all_ISI, ISI
from utils.objective_function import predict_spike_count, coincident_spike_count
from utils.plotting import Plotting
from utils.threshold_equation import solve_threshold_model_euler
from utils.tools import get_threshold_equation, get_voltage_from_data, get_timestamp_from_data, get_decimal_digits, \
    round_timestamp, get_voltage_from_AP_data, float_equality_judgement, false_alarms, explained_variance, \
    add_features_to_TableWidget_threshold_equation
from ui import CalculateFeatureWindow


class ThresholdEquationMethodMainWindow(QWidget, Ui_threshold_euqation_method_main_window):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

class ThresholdEquationMethodWorkflowTwoWindow(QWidget, Ui_workflow_2_panel):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.configure_stimulation_window = ConfigureStimulationWindow()
        self.signal_slot()
        self.show_equation_form()

    def signal_slot(self):
        self.pushButton_set_stimulation.clicked.connect(self.configure_stimulation_window.show)
        self.comboBox_threshold_equation_option.currentIndexChanged.connect(self.show_equation_form)
        self.webEngineView_threshold_equation.loadFinished.connect(self.adjust_height)

    def show_equation_form(self):
        index = self.comboBox_threshold_equation_option.currentIndex() + 1
        if index == 1:
            self.webEngineView_threshold_equation.setHtml(html_mathml_1)
        elif index == 2:
            self.webEngineView_threshold_equation.setHtml(html_mathml_2)
        elif index == 3:
            self.webEngineView_threshold_equation.setHtml(html_mathml_3)

    def adjust_height(self):
        # 使用 JavaScript 获取文档高度
        self.webEngineView_threshold_equation.page().runJavaScript("""
                Math.max(
                    document.body.scrollHeight, 
                    document.body.offsetHeight, 
                    document.documentElement.clientHeight, 
                    document.documentElement.scrollHeight, 
                    document.documentElement.offsetHeight
                );
            """, 0, self.set_height)

    def set_height(self, height):
        if height and isinstance(height, (int, float)):
            # 设置最小高度为计算高度 + 10px 的边距
            self.webEngineView_threshold_equation.setMinimumHeight(int(height))

class ThresholdEquationMethodWorkflowOneWindow(QWidget, Ui_workflow_1_panel):

    def __init__(self, main_window):
        self.main_window = main_window
        self.ParasOfFeaturesWindow = None
        self.data = None
        self.figure_set = None
        self.features_option = {'<Vm>': 0, 'dV/dt': [None, 0]}
        super().__init__()
        self.configure_parameters_window = None
        self.setupUi(self)
        self.signal_slot()
        self.show_equation_form()
        self.get_figure_set_origin()

    def signal_slot(self):
        self.comboBox_threshold_equation_option_workflow_1.currentIndexChanged.connect(self.show_equation_form)
        self.webEngineView_threshold_equation_workflow_1.page().loadFinished.connect(self.adjust_height)
        self.pushButton_config_threshold_params_workflow_1.clicked.connect(self.show_configure_equation_params_window)
        self.pushButton_run_workflow_1.clicked.connect(self.run_clicked)
        self.pushButton_calculate.clicked.connect(self.calculate_clicked)
        self.pushButton_set_parameters_workflow_1.clicked.connect(self.show_features_window)

    def show_features_window(self):
        """Create a CalculateFeatureWindow object for calculating spike features"""
        if self.data == {}:
            msg_box = QMessageBox(QMessageBox.Information, 'Message', 'No spike data!')
            msg_box.exec()
        else:
            self.ParasOfFeaturesWindow = CalculateFeatureWindow(mainWindow=self.main_window, data=self.data,
                                                                features_option=self.features_option,
                                                                tableWidget=self.tableWidget_features_workflow_1,
                                                                sender_name=
                                                                'threshold_equation')
            self.ParasOfFeaturesWindow.show()

    def show_equation_form(self):
        index = self.comboBox_threshold_equation_option_workflow_1.currentIndex() + 1
        if index == 1:
            self.webEngineView_threshold_equation_workflow_1.setHtml(html_mathml_1)
        elif index == 2:
            self.webEngineView_threshold_equation_workflow_1.setHtml(html_mathml_2)
        elif index == 3:
            self.webEngineView_threshold_equation_workflow_1.setHtml(html_mathml_3)

    def show_configure_equation_params_window(self):
        self.comboBox_threshold_equation_option_workflow_1.setEnabled(False)
        threshold_equation_index = self.comboBox_threshold_equation_option_workflow_1.currentIndex() + 1
        if not self.configure_parameters_window:
            self.configure_parameters_window = ConfigureEquationParametersWindow(
                equation_index=threshold_equation_index,
                equation_option_combobox=self.comboBox_threshold_equation_option_workflow_1,
                main_window=self.main_window)
        if self.configure_parameters_window:
            self.configure_parameters_window.equation_index=threshold_equation_index
        self.configure_parameters_window.init_ui()
        self.configure_parameters_window.show()

    def adjust_height(self):
        # 使用 JavaScript 获取文档高度
        self.webEngineView_threshold_equation_workflow_1.page().runJavaScript("""
                Math.max(
                    document.body.scrollHeight, 
                    document.body.offsetHeight, 
                    document.documentElement.clientHeight, 
                    document.documentElement.scrollHeight, 
                    document.documentElement.offsetHeight
                );
            """, 0, self.set_height)

    def set_height(self, height):
        if height and isinstance(height, (int, float)):
            # 设置最小高度为计算高度 + 10px 的边距
            self.webEngineView_threshold_equation_workflow_1.setMinimumHeight(int(height))

    def run_clicked(self):
        """
        1. 判断是否有膜电压序列。
        2. 判断阈值公式是否已设置参数
        3. Vm+阈值公式计算阈值θ的时间序列（整个放电过程）
        4. 计算电压范围内的稳态阈值
        5. 计算False alarms   暂时取消，放在后面的计算放电特征一栏计算，或者另外布置界面进行计算
        6. 检测"Spike threshold"界面的“Waveform curvature-based method”是否已经估计放电阈值。
            如果是，则将数据全部复制，然后赋值给当前模块的data，赋值前要“Action potential”界面的APs起止时间是否和“Spike threshold”数据中一致，如果一致，才进行复制。
        此时，数据中已经包含了估计阈值estimated threshold voltage，需要和后面的predicted threshold voltage进行区分。如果数据一致，
            如果否，检测"Action potential"界面是否已经提取单个动作电位。
            如果存在单个动作电位，则使用阈值公式方法估计单个动作电位阈值，否则不进行单个动作电位阈值估计。
        7. 如果有单个动作电位且估计了每个动作电位的阈值，则计算Explained variance。
        8. 存储所有放电数据。
        """
        # Step 1
        if not data_exists_check:
            msg_box = QMessageBox(QMessageBox.Information, 'Message', 'No membrane voltage!')
            msg_box.exec()
            return 0
        # Step 2
        if not self.configure_parameters_window:
            msg_box = QMessageBox(QMessageBox.Information, 'Message', 'Configure threshold equation parameters!')
            msg_box.exec()
            return 0

        if not self.configure_parameters_window.params_res:
            msg_box = QMessageBox(QMessageBox.Information, 'Message', 'Configure threshold equation parameters!')
            msg_box.exec()
            return 0

        # 检查阈值公式参数信息是否和当前所选阈值公式相匹配。考虑情况：当阈值公式选项更改时，参数配置未更改。如何判断面板配置参数信息和阈值公式参数对应。
        threshold_equation = get_threshold_equation(
            self.comboBox_threshold_equation_option_workflow_1.currentIndex() + 1)
        if not check_equation_params_consistent(threshold_equation, self.configure_parameters_window):
            msg_box = QMessageBox(QMessageBox.Information, 'Message', 'Configure threshold equation parameters!')
            msg_box.exec()
            return 0
        self.data = {}

        # Step 3
        data_source, voltage_option, simulation_data, dt = data_source_check(self.main_window)
        voltage = np.array(get_voltage_from_data(simulation_data, data_source, voltage_option=voltage_option))
        timestamp = np.array(get_timestamp_from_data(data=simulation_data))
        params_res = self.configure_parameters_window.params_res
        theta = solve_threshold_model_euler(voltage=voltage, dt=dt, ThresholEquation=threshold_equation, **params_res)

        # Step 4
        v_min = int(np.min(voltage))
        v_max = int(np.max(voltage))
        v_theta_inf = np.linspace(v_min, v_max, 1 + 100 * (v_max - v_min))
        theta_inf = np.zeros_like(v_theta_inf)
        if threshold_equation.__name__ == 'FormThree':
            for i in range(len(v_theta_inf)):
                theta_inf[i] = threshold_equation.theta_inf(v=v_theta_inf[i], **params_res)
        else:
            theta_inf = threshold_equation.theta_inf(v=v_theta_inf, **params_res)

        # Step 5 False alarms (fa)
        # real_spike_num =
        # predict_spike_num =
        # fa = np.abs((predict_spike_num-real_spike_num) / real_spike_num)

        # Step 6
        condition_1 = False
        # 判断是否提取单个动作电位以及是否对提取的单个动作电位已经进行阈值估计:condition_1
        AP = self.main_window.AP
        if len(self.main_window.AP) > 0 and self.main_window.CurvatureSpikeThreshold:
            data_estimated = self.main_window.CurvatureSpikeThreshold.data
            condition_1 = identify_APs_consistent(AP=AP, data=data_estimated, dt=dt)
        single_AP = False
        if condition_1:
            self.data = update_estimated_data(data_estimated)
            single_AP = True
        elif len(self.main_window.AP) > 0:
            single_AP = True
            # 判断是否提取单个动作电位。如果是，则提取单个动作电位数据，并估计单个动作电位的阈值。
            # 这里AP有两种可能，第一种是仅含有开始和结束时间，第二种可能是含有单个动作电位的所有数据。
            # 在当前这种情况下，未估计放电阈值（则AP仅有时间信息），或者AP和估计阈值不对应（则AP仅有时间信息），则需要重新提取动作电位。
            # 基于AP计算放电特征等数据，然后直接将数据存放至data。

            decimal_digits = get_decimal_digits(dt)
            timestamp = np.array(timestamp)

            for i in AP:
                self.data[i] = {}
                self.data[i]['features'] = {}
                if 'start' in AP[i]:
                    start = round(AP[i]['start'], decimal_digits)
                    stop = round(AP[i]['stop'], decimal_digits)
                    index1 = np.argmin(np.abs(timestamp - start))
                    index2 = np.argmin(np.abs(timestamp - stop))
                    for j in simulation_data:
                        self.data[i][j] = {}
                        for k in simulation_data[j]:
                            if k == 'label':
                                self.data[i][j][k] = simulation_data[j][k]
                            else:
                                self.data[i][j][k] = simulation_data[j][k][index1:index2 + 1]
            self.data['All'] = {'features': {'ISI': []},
                                'voltage': {'voltage': voltage,
                                            'label': 'Membrane Voltage(mV)'},
                                'timestamp': {'timestamp': timestamp,
                                              'label': 'time(ms)'}}
            ISI(voltage=voltage, timestamp=timestamp, data=self.data, data_source=data_source,
                voltage_option=voltage_option)
            calculate_superposition_APs(self.data, voltage_option=voltage_option, data_source=data_source, dt=dt)

        add_theta_to_data(theta=theta, theta_inf=theta_inf, data=self.data, v_theta_inf=v_theta_inf)

        # Step 7 预测单个动作电位阈值，如果预测到多次“放电”，则取最接近峰值的一个阈值电压作为放电阈值。区分，
        # 区分估计放电阈值和预测放电阈值以及预测阈值时间序列。把估计阈值更称为estimated_threshold，然后把预测阈值称作predicted_threshold，把预测阈值时间序列称作theta
        # 特征量（包括dV/dt，<V>）也需要进行区分，可以使用后缀进行区分，用
        if single_AP:
            for i in self.data:
                if 'AP' in i:
                    theta = self.data[i]['theta']['theta']
                    timestamp = self.data[i]['timestamp']['timestamp']
                    voltage = get_voltage_from_AP_data(AP_data=self.data, AP_name=i, data_source=data_source,
                                                       voltage_option=voltage_option)
                    spike_threshold, time_spike_threshold = predict_spike_threshold(theta=theta,
                                                                                    timestamp=timestamp,
                                                                                    voltage=voltage)
                    self.data[i]['features']['Vth_pred'] = [spike_threshold]
                    self.data[i]['timestamp']['timestamp_Vth_pred'] = [time_spike_threshold]
            # Step 8 叠加动作电位的预测阈值
            SpikeThresholds_pred = {}
            for i in AP:
                spike_threshold = self.data[i]['features']['Vth_pred']
                SpikeThresholds_pred[i] = spike_threshold[0]
                if  not SpikeThresholds_pred[i]:
                    print("BG!!!")
                timestamp_superposition = self.data[i]['timestamp']['timestamp_superposition']
                voltage_superposition = self.data[i]['voltage']['V_superposition']
                print("curr SpikeThresholds_pred[i]:",SpikeThresholds_pred[i])
                print("curr type(SpikeThresholds_pred[i]):", type(SpikeThresholds_pred[i]))
                timestamp_Vth_superposition_pred = timestamp_superposition[
                    float_equality_judgement(num=SpikeThresholds_pred[i], array=voltage_superposition)]
                self.data[i]['timestamp']['timestamp_Vth_superposition_pred'] = [timestamp_Vth_superposition_pred]
            self.update_data()
        # 2. Close the feature calculation window.
        if self.ParasOfFeaturesWindow:
            self.ParasOfFeaturesWindow.cancel_clicked()
        else:
            pass
        # 3. Update the feature table
        add_features_to_TableWidget_threshold_equation(self.tableWidget_features_workflow_1, self.data)
        # 4. Plotting
        self.plotting_curvature = Plotting(data=self.data,
                                           figure_set=self.figure_set,
                                           axes=self.main_window.names['axes_Vth'])
        self.main_window.names['Canvas_Vth'].draw()
        # 5. Update SetFigWindow_Vth for new data visualization
        if 'SetFigWindow_Vth' in self.main_window.names_window:
            self.main_window.names_window['SetFigWindow_Vth'].close()

            if 'SetFigWindow_Vth' in self.main_window.names_window:
                self.main_window.names_window['SetFigWindow_Vth'].deleteLater()
                self.main_window.names_window.pop('SetFigWindow_Vth')
            self.main_window.names_window['SetFigWindow_Vth'] = SetFigWindowVth(
                data_operation_module=self,
                main_window=self.main_window)
            self.main_window.names_window['SetFigWindow_Vth'].show()
        # 6. display Vth (spike threshold) info
        self.main_window.lineEdit_SD_Vth.setText("")
        self.main_window.lineEdit_mean_Vth.setText("")
        self.main_window.lineEdit_maximum_Vth.setText("")
        self.main_window.lineEdit_minimum_Vth.setText("")
        if self.data:
            if 'Vth_pred' in self.data['All']['features'].keys():
                Vth_list = self.data['All']['features']['Vth_pred']
                Vth_max = round(max(Vth_list), 3)
                Vth_min = round(min(Vth_list), 3)
                Vth_mean = round(np.mean(Vth_list), 3)
                Vth_stand_deviation = round(np.std(Vth_list), 3)
                self.main_window.lineEdit_SD_Vth.setText("{:.3f}".format(Vth_stand_deviation))
                self.main_window.lineEdit_mean_Vth.setText("{:.3f}".format(Vth_mean))
                self.main_window.lineEdit_maximum_Vth.setText("{:.3f}".format(Vth_max))
                self.main_window.lineEdit_minimum_Vth.setText("{:.3f}".format(Vth_min))
                self.main_window.groupBox_Vth.setTitle("Predicted Vth info")

    def update_data(self):
        """将AP中的放电特征数据更新至All中"""
        # timestamp_Vth_superposition_pred
        timestamp_Vth_superposition_pred_list = []
        timestamp_Vth_pred_list = []
        AP_name_list = []
        for i in self.data:
            if 'AP' in i:
                AP_name_list.append(i)
                timestamp_Vth_superposition_pred_list.append(
                    self.data[i]['timestamp']['timestamp_Vth_superposition_pred'][0])
                timestamp_Vth_pred_list.append(self.data[i]['timestamp']['timestamp_Vth_pred'][0])
        self.data['All']['timestamp']['timestamp_Vth_superposition_pred'] = timestamp_Vth_superposition_pred_list
        self.data['All']['timestamp']['timestamp_Vth_pred'] = timestamp_Vth_pred_list

        # dV/dt_pred、<V>_pred
        pred_feature_name_list = []
        for i in self.data[AP_name_list[0]]['features']:
            if '_pred' in i:
                pred_feature_name_list.append(i)
        temp_dict = {}
        for i in pred_feature_name_list:
            temp_dict[i] = []
        for i in self.data:
            if 'AP' in i:
                for j in pred_feature_name_list:
                    temp_dict[j].append(self.data[i]['features'][j][0])
        for i in pred_feature_name_list:
            self.data['All']['features'][i] = temp_dict[i]

    def calculate_clicked(self):
        """计算FA和EV。FA的前提是设置Time window以及提取单个动作电位；而EV的前提是已经估计单个动作电位阈值"""
        # 1. 条件判断
        if not self.data:
            msg_box = QMessageBox(QMessageBox.Information, 'Message', 'Run first!')
            msg_box.exec()
            return 0
        # 3. 计算EV
        if 'Vth_est' in self.data['All']['features']:
            Vth_est = self.data['All']['features']['Vth_est']
            Vth_pred = self.data['All']['features']['Vth_pred']
            ev = explained_variance(Vth_est=Vth_est, Vth_pred=Vth_pred)
            self.lineEdit_ev.setText(str(ev))
        else:
            self.lineEdit_ev.setText(" ")
        # 2. 计算FA
        fa = self.FA
        if fa is np.nan:
            self.lineEdit_fa.setText(' ')
        else:
            self.lineEdit_fa.setText(str(fa))


    @property
    def FA(self):
        time_window = self.doubleSpinBox_time_window.value()
        data_keys = list(self.data.keys())
        condition = False
        for i in data_keys:
            if 'AP' in i:
                condition=True
                break
        if condition:
            """FA计算的前提条件：膜电压存在放电；用户已提取膜电压序列中全部动作电位并估计其放电阈值"""
            data_source, voltage_option, data, dt = data_source_check(self.main_window)
            voltage = get_voltage_from_data(data, data_source, voltage_option=voltage_option)
            spike, spike_count, spike_flag = spike_check(voltage)
            if not (spike & (spike_count > 0)):
                return np.nan
            AP_list = []
            for i in data_keys:
                if "AP" in i:
                    AP_list.append(i)
            if not len(AP_list) == spike_count:
                msg_box = QMessageBox(QMessageBox.Information, 'Message',
                                      'False alarm calculation requires extraction of all APs '
                                      'and estimation of their threshold voltages.')
                msg_box.exec()
                return np.nan
            if 'Vth_pred' not in self.data['All']['features']:
                msg_box = QMessageBox(QMessageBox.Information, 'Message',
                                      'Run first!')
                msg_box.exec()
                return np.nan
            timestamp_Vth_est = self.data['All']['timestamp']['timestamp_Vth_est']
            timestamp_Vth_pred = np.array(self.data['All']['timestamp']['timestamp_Vth_pred'])
            _,coin_spike_num = coincident_spike_count(time_window=time_window, time_threshold_predict=timestamp_Vth_pred,time_threshold_estimation=timestamp_Vth_est)
            return (len(timestamp_Vth_pred)-coin_spike_num)/spike_count


    def get_figure_set_origin(self):
        fig_1_1 = {
            '1': {'x': ('All', 'timestamp', 'timestamp_superposition'), 'y': ('All', 'voltage', 'V_superposition'),
                  'label': 'membrane voltage'},
            '2': {'x': ('All', 'timestamp', 'timestamp_Vth_superposition_pred'), 'y': ('All', 'features', 'Vth_pred'),
                  'label': 'predicted Vth', 'color': "red"},
            '3': {'x': ('All', 'timestamp', 'timestamp_Vth_superposition_est'), 'y': ('All', 'features', 'Vth_est'),
                  'label': 'estimated Vth', 'color': "green"}
        }
        fig_1_2 = {
            '1': {'x': ('All', 'timestamp', 'timestamp'), 'y': ('All', 'voltage', "voltage"),
                  'label': 'membrane voltage', 'color': 'black'},
            '2': {'x': ('All', 'timestamp', 'timestamp'), 'y': ('All', 'theta', 'theta'),
                  'label': 'theta', 'color': 'blue'},
            '3': {'x': ('All', 'timestamp', 'timestamp_Vth_est'), 'y': ('All', 'features', 'Vth_est'),
                  'label': 'estimated Vth', 'color': 'green'},
            '4': {'x': ('All', 'timestamp', 'timestamp_Vth_pred'), 'y': ('All', 'features', 'Vth_pred'),
                  'label': 'predicted Vth', 'color': 'red'}
        }
        fig_2_1 = {}
        fig_2_2 = {}
        self.figure_set_origin = {(1, 1): fig_1_1, (1, 2): fig_1_2, (2, 1): fig_2_1, (2, 2): fig_2_2}
        if self.main_window.figure_set_threshold_equation == None:
            self.main_window.figure_set_threshold_equation = self.figure_set_origin.copy()
            self.figure_set = self.main_window.figure_set_threshold_equation
        else:
            self.figure_set = self.main_window.figure_set_threshold_equation


def update_estimated_data(estimated_data):
    """
    将估计阈值数据中的“All”和每个”AP“数据进行更新。主要是将放电特征数据添加后缀以和预测阈值进行区分。
    """
    predicted_data = copy.deepcopy(estimated_data)
    # 'All' 'features'
    temp = list(predicted_data['All']['features'].keys())
    for i in temp:
        if 'ISI' in i or 'label' in i:
            pass
        else:
            predicted_data['All']['features'][i + '_est'] = predicted_data['All']['features'].pop(i)
    # 'All' 'timestamp'
    temp = list(predicted_data['All']['timestamp'].keys())
    for i in temp:
        if 'Vth' in i:
            predicted_data['All']['timestamp'][i + '_est'] = predicted_data['All']['timestamp'].pop(i)

    # 'AP'
    temp = list(predicted_data.keys())
    for i in temp:
        if i == 'All':
            pass
        elif 'AP' in i:
            update_AP_data(predicted_data[i])
    return predicted_data


def update_AP_data(estimated_AP_data):
    temp = list(estimated_AP_data['features'].keys())
    for i in temp:
        if 'ISI' in i:
            pass
        else:
            estimated_AP_data['features'][i + '_est'] = estimated_AP_data['features'].pop(i)
    temp = list(estimated_AP_data['timestamp'].keys())
    for i in temp:
        if 'Vth' in i:
            estimated_AP_data['timestamp'][i + '_est'] = estimated_AP_data['timestamp'].pop(i)


def add_theta_to_data(theta, theta_inf, data, v_theta_inf):
    """添加theta到data['All']以及单个动作电位中"""
    # "All"
    data['All']['theta'] = {'theta': theta, 'theta_inf': theta_inf, 'v_theta_inf': v_theta_inf}
    # single AP
    timestamp = data['All']['timestamp']['timestamp']
    for i in data:
        if "AP" in i:
            start = np.min(data[i]['timestamp']['timestamp'])
            stop = np.max(data[i]['timestamp']['timestamp'])
            start_index = float_equality_judgement(start, timestamp)
            stop_index = float_equality_judgement(stop, timestamp)
            data[i]['theta'] = {'theta': theta[start_index:stop_index + 1],
                                'theta_inf': theta_inf[start_index:stop_index + 1],
                                'v_theta_inf': v_theta_inf[start_index:stop_index + 1]}


def calculate_superposition_APs(data, voltage_option, data_source, dt):
    """计算叠加单个动作电位"""
    list_index_voltage_max = {}

    for i in data:
        if 'AP' in i:
            voltage = get_voltage_from_AP_data(AP_data=data, AP_name=i, data_source=data_source,
                                               voltage_option=voltage_option)
            index = list(voltage).index(max(voltage))
            list_index_voltage_max[i] = index
    store_ap_pre_length = {}
    store_ap_post_length = {}
    max_ap_pre_length = None
    max_ap_post_length = None
    for i in data:
        if 'AP' in i:
            voltage = get_voltage_from_AP_data(AP_data=data, AP_name=i, data_source=data_source,
                                               voltage_option=voltage_option)
            ap_pre_length = list_index_voltage_max[i] + 1
            ap_post_length = len(voltage) - ap_pre_length
            if max_ap_post_length is None:
                max_ap_pre_length = ap_pre_length
            else:
                if max_ap_pre_length < ap_pre_length:
                    max_ap_pre_length = ap_pre_length
            if max_ap_post_length is None:
                max_ap_post_length = ap_post_length
            else:
                if max_ap_post_length < ap_post_length:
                    max_ap_post_length = ap_post_length
            store_ap_pre_length[i] = ap_pre_length
            store_ap_post_length[i] = ap_post_length
    timestamp_superposition_list = []
    V_superposition_list = []
    for j in data:
        if 'AP' in j:
            voltage = get_voltage_from_AP_data(AP_data=data, AP_name=j, data_source=data_source,
                                               voltage_option=voltage_option)
            ap_voltage_complete = copy.deepcopy(voltage)
            pre = np.full((int(max_ap_pre_length - store_ap_pre_length[j]),), np.nan)
            post = np.full((int(max_ap_post_length - store_ap_post_length[j], )), np.nan)
            voltage_superposition = np.concatenate((pre, ap_voltage_complete, post))
            timestamp_superposition = np.linspace(0,
                                                  (len(voltage_superposition) - 1) * dt,
                                                  len(voltage_superposition))
            data[j]['voltage']['V_superposition'] = voltage_superposition
            data[j]['timestamp']['timestamp_superposition'] = timestamp_superposition
            timestamp_superposition_list.append(timestamp_superposition)
            V_superposition_list.append(voltage_superposition)
    data['All']['timestamp']['timestamp_superposition'] = timestamp_superposition_list
    data['All']['voltage']['V_superposition'] = V_superposition_list


def predict_spike_threshold(theta, timestamp, voltage):
    voltage = np.asarray(voltage)
    theta = np.asarray(theta)

    # 找出膜电压从下往上穿过阈值的位置
    crossings = np.where((voltage[:-1] <= theta[:-1]) & (voltage[1:] >= theta[1:]))[0] + 1
    peak_index = np.argmax(voltage)

    if len(crossings) > 0:
        pre_peak_crossings = crossings[crossings < peak_index]
        threshold_index = np.max(pre_peak_crossings)
        spike_threshold = voltage[threshold_index]
        time_spike_threshold = timestamp[threshold_index]
        return spike_threshold, time_spike_threshold

    return None, None
