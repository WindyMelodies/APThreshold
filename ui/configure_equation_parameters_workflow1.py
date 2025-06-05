import logging

import matplotlib.pyplot as plt
import numpy as np
from PySide6.QtWidgets import QWidget, QButtonGroup, QMessageBox
from ui.ui_Configure_parameters_winodw_workflow1 import Ui_ConfigureEquationParametersWindow
from utils.condition_check import data_exists_check, data_source_check, spike_check
from utils.curvature_based_method import calculate_all_ISI, peak_time
from utils.objective_function import calculate_gama_factor_reverse, calculate_firing_rate, predict_spike_count, \
    coincident_spike_count
from utils.threshold_equation import FormDynamics, solve_threshold_model_euler
import cma

from utils.tools import get_voltage_from_data, get_timestamp_from_data, round_timestamp


class ConfigureEquationParametersWindow(QWidget, Ui_ConfigureEquationParametersWindow):

    def __init__(self, equation_index, equation_option_combobox, main_window):
        self.main_window = main_window
        self.group_checkbox_dynamics = None
        self.param_info_equation_dynamics = None
        self.param_info_equation = None
        self.equation_index = equation_index
        self.equation_option_combobox = equation_option_combobox
        self.fixed_checkbox_group_dynamics_equation = []
        super().__init__()
        self.setupUi(self)
        self.init_ui()
        self.signal_slot()

    def signal_slot(self):
        self.pushButton_canel.clicked.connect(self.close)
        self.pushButton_run.clicked.connect(self.fit_equation_parameters)

    def fit_equation_parameters(self):
        threshold_equation = None
        time_threshold_estimation = None
        objective_function = None
        kwargs_threshold_equation = None
        kwargs_objective_function = None
        kwargs = None
        # 预先获取数据：timestamp，voltage，估计放电阈值，ISIs
        if data_exists_check(main_window=self.main_window):
            data_source, voltage_option, data, dt = data_source_check(self.main_window)
            voltage = np.array(get_voltage_from_data(data=data, data_source=data_source,
                                                     voltage_option=voltage_option))
            timestamp = np.array(get_timestamp_from_data(data=data))
            spike, spike_count, spike_flag = spike_check(voltage)
            # ISI calculation
            if spike:
                if spike_count >= 2:
                    list_voltage_max, list_voltage_max_moment, list_index_voltage_max = peak_time(
                        spike_flag=spike_flag,
                        voltage=voltage,
                        timestamp=timestamp)

                    ISIs, _ = calculate_all_ISI(
                        list_voltage_max_moment=list_voltage_max_moment,
                        list_voltage_max=list_voltage_max)
                else:
                    msg_box = QMessageBox(QMessageBox.Information, 'Message', 'Spike number is less than two!')
                    msg_box.exec()
                    return 0
            else:
                msg_box = QMessageBox(QMessageBox.Information, 'Message', 'No action potential!')
                msg_box.exec()
                return 0
            # Check if spike onset is detected using waveform curvature-based method
            if self.main_window.CurvatureSpikeThreshold:
                time_threshold_estimation = self.main_window.CurvatureSpikeThreshold.data['All']['timestamp'][
                    'timestamp_Vth']
                estimated_spike_threshold = self.main_window.CurvatureSpikeThreshold.data['All']['features'][
                    'Vth']

        else:
            msg_box = QMessageBox(QMessageBox.Information, 'Message', 'No spike data!')
            msg_box.exec()
            return 0

        # 获取拟合参数信息
        if (self.stackedWidget_equation_parameters.currentIndex() + 1) == 1:
            self.update_equation_dynamics_param_info()
            self.param_info_equation = self.param_info_equation_dynamics
            threshold_equation = FormDynamics
            kwargs_threshold_equation = {'ThresholdEquation': threshold_equation}

        # 获取目标函数信息
        objective_function_option = self.comboBox_objective_function.currentIndex() + 1
        if objective_function_option == 1:
            time_window_sigma = float(self.doubleSpinBox_time_window_gama_factor.value())
            objective_function = calculate_gama_factor_reverse
            kwargs_objective_function = {"timestamp": timestamp, "voltage": voltage,
                                         "time_threshold_estimation": time_threshold_estimation,
                                         "ISIs": ISIs, "time_window_sigma": time_window_sigma}

        # 开始拟合参数
        optimization_algorithm_option = self.comboBox_algorithm.currentIndex() + 1
        kwargs = kwargs_threshold_equation | kwargs_objective_function
        if optimization_algorithm_option == 1:
            x0 = np.zeros((len(self.param_info_equation),))
            num = 0
            bounds = [[], []]
            for i in self.param_info_equation:
                x0[num] = (self.param_info_equation[i]['bounds'][0] + self.param_info_equation[i]['bounds'][1]) / 2
                num += 1
                bounds[0].append(self.param_info_equation[i]['bounds'][0])
                bounds[1].append(self.param_info_equation[i]['bounds'][1])
            es = cma.CMAEvolutionStrategy(x0=x0, sigma0=0.5, inopts={'bounds': bounds})  # 带边界约束的CMA-ES优化
            es.optimize(objective_function, args=[kwargs])
            es.result_pretty()
            result = es.result
            best_solution = result[0]  # 最优解
            # 更新最优解至fixed value
            fixed_value_button_group = [self.doubleSpinBox_tao_theta_dynamics_fixed,
                                        self.doubleSpinBox_alpha_dynamics_fixed, self.doubleSpinBox_ka_dynamics_fixed,
                                        self.doubleSpinBox_ki_dynamics_fixed, self.doubleSpinBox_Vi_dynamics_fixed,
                                        self.doubleSpinBox_VT_dynamics_fixed]
            for i in range(len(fixed_value_button_group)):
                fixed_value_button_group[i].setValue(best_solution[i])
            # for result visualization
            for i in range(len(threshold_equation.params_name)):
                kwargs[threshold_equation.params_name[i]] = best_solution[i]
        self.checkBox_fixed_dynamics.setChecked(True)
        self.result_visualization(estimated_spike_threshold=estimated_spike_threshold, **kwargs)

    def result_visualization(self, estimated_spike_threshold, **kwargs):
        axes = self.main_window.names['axes_Vth']
        ax_1 = axes[(1, 1)]
        ax_2 = axes[(1, 2)]
        ax_3 = axes[(2, 1)]
        ax_1.cla()
        ax_2.cla()
        ax_3.cla()
        timestamp = kwargs['timestamp']
        voltage = kwargs['voltage']
        time_threshold_estimation = kwargs['time_threshold_estimation']
        time_window_sigma = kwargs['time_window_sigma']
        ThresholdEquation = kwargs['ThresholdEquation']
        ISIs = kwargs['ISIs']
        dt = timestamp[1] - timestamp[0]
        # solve threshold equation
        theta = solve_threshold_model_euler(dt=dt, ThresholEquation=ThresholdEquation, **kwargs)
        # calculate firing rate
        r_rec = calculate_firing_rate(ISIs=ISIs)
        time_threshold_predict, threshold_predict = predict_spike_count(voltage=voltage, timestamp=timestamp,
                                                                        theta=theta)
        time_threshold_predict = np.array(time_threshold_predict)
        threshold_predict = np.array(threshold_predict)
        coincident_predict_index, coincident_spike_num = coincident_spike_count(
            time_threshold_predict=time_threshold_predict, time_threshold_estimation=time_threshold_estimation,
            time_window=time_window_sigma)
        logging.info("预测放电次数为{}".format(len(time_threshold_predict)))
        logging.info(f"重合放电次数为{coincident_spike_num}")
        N_rec = len(time_threshold_estimation)
        N_coinc = coincident_spike_num
        N_pred = len(time_threshold_predict)

        ax_1.plot(timestamp, voltage, color="black", zorder=1)
        ax_1.plot(timestamp, theta, color="red", zorder=2)

        ax_1.scatter(time_threshold_predict, threshold_predict, color="blue",
                     zorder=3, label=f'Predicted spike:{len(threshold_predict)}')

        ax_1.scatter(time_threshold_predict[coincident_predict_index], threshold_predict[coincident_predict_index],
                     color="green",
                     zorder=4, label=f'Coincident spike: {N_coinc}')

        ax_1.scatter(time_threshold_estimation, estimated_spike_threshold, color="purple", zorder=5,
                     label=f'Estimated spike: {len(estimated_spike_threshold)}')
        y_max = max(voltage)
        y_min = min(voltage)
        for i in time_threshold_predict:
            ax_1.fill_between([i, i + time_window_sigma], y_min, y_max, color="grey", zorder=0)
            ax_1.fill_between([i - time_window_sigma, i], y_min, y_max, color="grey", zorder=0)
        ax_1.set_xlabel('Time (ms)')
        ax_1.set_ylabel('Voltage (mV)')
        ax_1.legend()

        # 绘制阈值稳态曲线
        start = int(np.min(voltage))
        stop = int(np.max(voltage))
        x_lim = (start, stop)
        x = np.linspace(start, stop, 1 + 100 * (stop - start))
        theta_inf = ThresholdEquation.theta_inf(v=x, **kwargs)
        kwargs['alpha'] = 0
        kwargs['ka'] = 4.62

        kwargs['ki'] = -7.15

        kwargs['Vi'] = -56.31
        kwargs['VT'] = -72.17

        theta_inf_bio = ThresholdEquation.theta_inf(v=x, **kwargs)
        y = theta_inf
        ax_2.plot(x, y, label='fit', zorder=2)
        ax_2.plot(x, theta_inf_bio, label='bio', zorder=2)
        ax_2.plot(x, x, color='black')
        ax_2.set_xlim(x_lim)
        ax_2.set_xlabel('Voltage (ms)')
        ax_2.set_ylabel('Steady state theta (mV)')
        ax_2.legend()
        # theta_Vm

        ax_3.plot(voltage, theta)
        ax_3.plot(theta, theta, color='grey')
        ax_3.set_xlabel('Voltage (ms)')
        ax_3.set_ylabel('Theta (mV)')
        self.main_window.names['Canvas_Vth'].draw()

    def update_equation_dynamics_param_info(self):

        self.param_info_equation_dynamics = {
            'tau_theta': {"fit_option": False, "bounds": [], "fixed_value": 0.0},
            'alpha': {"fit_option": False, "bounds": [], "fixed_value": 0.0},
            'ka': {"fit_option": False, "bounds": [], "fixed_value": 0.0},
            'ki': {"fit_option": False, "bounds": [], "fixed_value": 0.0},
            'Vi': {"fit_option": False, "bounds": [], "fixed_value": 0.0},
            'VT': {"fit_option": False, "bounds": [], "fixed_value": 0.0}
        }

        if self.checkBox_fixed_dynamics.isChecked():
            self.param_info_equation_dynamics['tau_theta']['fit_option'] = False
            self.param_info_equation_dynamics['tau_theta'][
                'fixed_value'] = self.doubleSpinBox_tao_theta_dynamics_fixed.value()
            self.param_info_equation_dynamics['alpha']['fit_option'] = False
            self.param_info_equation_dynamics['alpha'][
                'fixed_value'] = self.doubleSpinBox_alpha_dynamics_fixed.value()
            self.param_info_equation_dynamics['ka']['fit_option'] = False
            self.param_info_equation_dynamics['ka'][
                'fixed_value'] = self.doubleSpinBox_ka_dynamics_fixed.value()
            self.param_info_equation_dynamics['ki']['fit_option'] = False
            self.param_info_equation_dynamics['ki'][
                'fixed_value'] = self.doubleSpinBox_ki_dynamics_fixed.value()
            self.param_info_equation_dynamics['Vi']['fit_option'] = False
            self.param_info_equation_dynamics['Vi'][
                'fixed_value'] = self.doubleSpinBox_Vi_dynamics_fixed.value()
            self.param_info_equation_dynamics['VT']['fit_option'] = False
            self.param_info_equation_dynamics['VT'][
                'fixed_value'] = self.doubleSpinBox_VT_dynamics_fixed.value()

        else:
            self.param_info_equation_dynamics['tau_theta']['fit_option'] = True
            self.param_info_equation_dynamics['tau_theta'][
                'bounds'] = [self.doubleSpinBox_tao_theta_dynamics_min.value(),
                             self.doubleSpinBox_tao_theta_dynamics_max.value()]

            self.param_info_equation_dynamics['alpha']['fit_option'] = True
            self.param_info_equation_dynamics['alpha'][
                'bounds'] = [self.doubleSpinBox_alpha_dynamics_min.value(),
                             self.doubleSpinBox_alpha_dynamics_max.value()]

            self.param_info_equation_dynamics['ka']['fit_option'] = True
            self.param_info_equation_dynamics['ka'][
                'bounds'] = [self.doubleSpinBox_ka_dynamics_min.value(),
                             self.doubleSpinBox_ka_dynamics_max.value()]

            self.param_info_equation_dynamics['ki']['fit_option'] = True
            self.param_info_equation_dynamics['ki'][
                'bounds'] = [self.doubleSpinBox_ki_dynamics_min.value(),
                             self.doubleSpinBox_ki_dynamics_max.value()]

            self.param_info_equation_dynamics['Vi']['fit_option'] = True
            self.param_info_equation_dynamics['Vi'][
                'bounds'] = [self.doubleSpinBox_Vi_dynamics_min.value(),
                             self.doubleSpinBox_Vi_dynamics_max.value()]

            self.param_info_equation_dynamics['VT']['fit_option'] = True
            self.param_info_equation_dynamics['VT'][
                'bounds'] = [self.doubleSpinBox_VT_dynamics_min.value(),
                             self.doubleSpinBox_VT_dynamics_max.value()]

    def init_ui(self):
        # 恢复上次回话状态 todo

        # 根据公式选项更新参数面板
        if self.equation_index == 1:
            self.stackedWidget_equation_parameters.setCurrentIndex(0)
        elif self.equation_index == 2:
            pass
        elif self.equation_index == 3:
            pass
        self.group_checkbox_dynamics = QButtonGroup(self)
        self.group_checkbox_dynamics.setExclusive(True)
        self.group_checkbox_dynamics.addButton(self.checkBox_fixed_dynamics)
        self.group_checkbox_dynamics.addButton(self.checkBox_fit_dynamics)
        for checkbox in self.group_checkbox_dynamics.buttons():
            checkbox.stateChanged.connect(self.check_if_fit_params)

    def check_if_fit_params(self):
        if self.equation_index == 1:
            if self.checkBox_fixed_dynamics.isChecked():
                self.pushButton_run.setEnabled(False)
                self.pushButton_terminate.setEnabled(False)
            else:
                self.pushButton_run.setEnabled(True)
                self.pushButton_terminate.setEnabled(True)

    def close(self):
        self.equation_option_combobox.setEnabled(True)
        super().close()

    def closeEvent(self, event):
        self.equation_option_combobox.setEnabled(True)
        super().closeEvent(event)
