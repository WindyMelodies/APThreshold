import logging
import pickle
import sys

import traceback

import matplotlib.pyplot as plt
import numpy as np
from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import QWidget, QButtonGroup, QMessageBox
from ui.ui_Configure_parameters_winodw_workflow1 import Ui_ConfigureEquationParametersWindow
from utils.condition_check import data_exists_check, data_source_check, spike_check
from utils.curvature_based_method import calculate_all_ISI, peak_time
from utils.exceptions import OptimizationInterruptedException
from utils.objective_function import calculate_gama_factor_reverse, calculate_firing_rate, predict_spike_count, \
    coincident_spike_count
from utils.threshold_equation import FormOne, solve_threshold_model_euler, FormTwo, FormThree
import cma
from utils.tools import get_voltage_from_data, get_timestamp_from_data, round_timestamp


class ConfigureEquationParametersWindow(QWidget, Ui_ConfigureEquationParametersWindow):

    def __init__(self, equation_index, equation_option_combobox, main_window):
        """param_info_equation_dynamics, param_info_equation都是用于存储拟合参数配置信息"""
        self.best_solution = None       # for test
        self.optimizer_thread = None
        self.main_window = main_window
        self.group_checkbox_dynamics = None
        self.threshold_equation_name = None
        self.param_info_equation_dynamics = None
        self.param_info_equation_origin = None
        self.param_info_equation_rectifier = None
        self.param_info_equation = None  # 参数说明：后续仅会将各个阈值公式的参数赋值给此参数，并不会有任何改动。
        self.params_name = None
        self.params_res = {}
        self.fixed_parameter_values = None
        self.equation_index = equation_index
        self.equation_option_combobox = equation_option_combobox
        self.fixed_checkbox_group_dynamics_equation = []
        self.signal_emitter = SignalEmitter()
        # 初始化标准输出重定向器
        self.stdout_redirector = StreamRedirector()
        # 保存原始的 sys.stdout，以便之后恢复
        self._original_stdout = sys.stdout
        self.optimizer_thread = OptimizerThread(signal_emitter=self.signal_emitter, object=self)
        super().__init__()
        self.setupUi(self)
        self.init_ui()
        self.signal_slot()
        self.pushButton_terminate.setEnabled(False)

    def signal_slot(self):
        self.pushButton_canel.clicked.connect(self.close)
        self.pushButton_run.clicked.connect(self.optimize_equation_params)
        self.signal_emitter.update_signal.connect(self.append_log)
        self.signal_emitter.finish_signal.connect(self.append_log)
        # 将重定向器的 text_written 信号连接到 append_log 方法
        self.stdout_redirector.text_written.connect(self.append_log)
        self.optimizer_thread.finished.connect(self.on_optimization_finished)
        self.pushButton_terminate.clicked.connect(self.stop_optimization)
        self.pushButton_OK.clicked.connect(self.ok_clicked)
        self.comboBox_algorithm.currentIndexChanged.connect(self.algorithm_panel_change)


    def optimize_equation_params(self):
        # print("*"*4,"开始拟合阈值公式参数","*"*4)
        self.pushButton_run.setEnabled(False)  # 禁用运行按钮
        self.pushButton_terminate.setEnabled(True)  # 启用终止按钮

        self.plainTextEdit_optimization.clear()
        self.plainTextEdit_optimization.appendPlainText("Fitting equation parameters...")
        # 在开始优化前，重定向 sys.stdout到自定义流
        sys.stdout = self.stdout_redirector
        self.optimizer_thread.start()
        # print("*"*4,"最优化完成","*"*4)

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
                msg_box = QMessageBox(QMessageBox.Information, 'Message',
                                      'No estimated threshold voltage for optimization!')
                msg_box.exec()
                return 0

        else:
            msg_box = QMessageBox(QMessageBox.Information, 'Message', 'No spike data!')
            msg_box.exec()
            return 0

        # 获取拟合参数信息
        if (self.stackedWidget_equation_parameters.currentIndex() + 1) == 1:
            self.update_equation_dynamics_param_info()
            self.param_info_equation = self.param_info_equation_dynamics
            threshold_equation = FormOne
        elif (self.stackedWidget_equation_parameters.currentIndex() + 1) == 2:
            self.update_equation_origin_param_info()
            self.param_info_equation = self.param_info_equation_origin
            threshold_equation = FormTwo
        elif (self.stackedWidget_equation_parameters.currentIndex() + 1) == 3:
            self.update_equation_rectifier_param_info()
            self.param_info_equation = self.param_info_equation_rectifier
            threshold_equation = FormThree
        equation_name = threshold_equation.__name__
        kwargs_threshold_equation = {'ThresholdEquation': threshold_equation}
        self.params_name = threshold_equation.params_name
        # 获取目标函数信息
        objective_function_option = self.comboBox_objective_function.currentIndex() + 1
        if objective_function_option == 1:
            time_window_sigma = float(self.doubleSpinBox_time_window_gama_factor.value())
            objective_function = calculate_gama_factor_reverse
            kwargs_objective_function = {"timestamp": timestamp, "voltage": voltage,
                                         "time_threshold_estimation": time_threshold_estimation,
                                         "ISIs": ISIs, "time_window_sigma": time_window_sigma}

        # 开始拟合参数
        kwargs = kwargs_threshold_equation | kwargs_objective_function
        kwargs["optimizer_thread"] = self.optimizer_thread
        optimization_algorithm_option = self.comboBox_algorithm.currentIndex() + 1

        try:
            if optimization_algorithm_option == 1:
                x0 = np.zeros((len(self.param_info_equation),))
                num = 0
                bounds = [[], []]
                for i in self.param_info_equation:
                    x0[num] = (self.param_info_equation[i]['bounds'][0] + self.param_info_equation[i]['bounds'][
                        1]) / 2
                    num += 1
                    bounds[0].append(self.param_info_equation[i]['bounds'][0])
                    bounds[1].append(self.param_info_equation[i]['bounds'][1])
                es = cma.CMAEvolutionStrategy(x0=x0, sigma0=0.5, inopts={'bounds': bounds})  # 带边界约束的CMA-ES优化
                es.optimize(objective_function, args=[kwargs])
                es.result_pretty()
                result = es.result
                best_solution = result[0]  # 最优解
                self.best_solution = best_solution
                self.signal_emitter.finish_signal.emit(f"best solution = {best_solution}")

            self.update_fixed_value_button(equation_name=equation_name, best_solution=best_solution)
            # for result visualization
            for i in range(len(threshold_equation.params_name)):
                kwargs[threshold_equation.params_name[i]] = best_solution[i]
                # self.checkBox_fixed_dynamics.setChecked(True)
            # self.result_visualization(estimated_spike_threshold=estimated_spike_threshold, **kwargs)
        except OptimizationInterruptedException as e:
            # 捕获用户中断异常
            self.signal_emitter.finish_signal.emit(f"{e}")
        except Exception as e:
            # 捕获其他未知异常并报告
            traceback_str = traceback.format_exc()
            print(traceback_str)  # 控制台打印
            self.signal_emitter.finish_signal.emit(traceback_str)  # 通过信号传递完整traceback信息
            # self.signal_emitter.finish_signal.emit(f"{e}")

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
        theta_inf = np.zeros_like(x)
        if ThresholdEquation.__name__ == 'FormThree':
            for i in range(len(x)):
                theta_inf[i] = ThresholdEquation.theta_inf(x[i], **kwargs)
        else:
            theta_inf = ThresholdEquation.theta_inf(v=x, **kwargs)
        kwargs['alpha'] = 0
        kwargs['ka'] = 8.25

        kwargs['ki'] = -7.15

        kwargs['Vi'] = -56.31
        kwargs['VT'] = -72.17
        theta_inf_bio = np.zeros_like(x)
        if ThresholdEquation.__name__ == 'FormThree':
            for i in range(len(x)):
                theta_inf_bio[i] = ThresholdEquation.theta_inf(x[i], **kwargs)
        else:
            theta_inf_bio = ThresholdEquation.theta_inf(v=x, **kwargs)
        y = theta_inf
        ax_2.plot(x, y, label='fit', zorder=2)
        ax_2.plot(x, theta_inf_bio, label='bio', zorder=2)
        ax_2.plot(x, x, color='black')
        ax_2.set_xlim(x_lim)
        ax_2.set_xlabel('Voltage (mV)')
        ax_2.set_ylabel('Steady state theta (mV)')
        ax_2.legend()
        # theta_Vm

        ax_3.plot(voltage, theta)
        ax_3.plot(theta, theta, color='grey')
        ax_3.set_xlabel('Voltage (mV)')
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

    def update_equation_origin_param_info(self):
        self.param_info_equation_origin = {
            'tau_theta': {"fit_option": False, "bounds": [], "fixed_value": 0.0},
            'ka': {"fit_option": False, "bounds": [], "fixed_value": 0.0},
            'ki': {"fit_option": False, "bounds": [], "fixed_value": 0.0},
            'Vi': {"fit_option": False, "bounds": [], "fixed_value": 0.0},
            'VT': {"fit_option": False, "bounds": [], "fixed_value": 0.0}
        }

        if self.checkBox_fixed_origin.isChecked():
            self.param_info_equation_origin['tau_theta']['fit_option'] = False
            self.param_info_equation_origin['tau_theta'][
                'fixed_value'] = self.doubleSpinBox_tao_theta_dynamics_fixed.value()
            self.param_info_equation_origin['ka']['fit_option'] = False
            self.param_info_equation_origin['ka'][
                'fixed_value'] = self.doubleSpinBox_ka_origin_fixed.value()
            self.param_info_equation_origin['ki']['fit_option'] = False
            self.param_info_equation_origin['ki'][
                'fixed_value'] = self.doubleSpinBox_ki_origin_fixed.value()
            self.param_info_equation_origin['Vi']['fit_option'] = False
            self.param_info_equation_origin['Vi'][
                'fixed_value'] = self.doubleSpinBox_Vi_origin_fixed.value()
            self.param_info_equation_origin['VT']['fit_option'] = False
            self.param_info_equation_origin['VT'][
                'fixed_value'] = self.doubleSpinBox_VT_origin_fixed.value()

        else:
            self.param_info_equation_origin['tau_theta']['fit_option'] = True
            self.param_info_equation_origin['tau_theta'][
                'bounds'] = [self.doubleSpinBox_tao_theta_origin_min.value(),
                             self.doubleSpinBox_tao_theta_origin_max.value()]

            self.param_info_equation_origin['ka']['fit_option'] = True
            self.param_info_equation_origin['ka'][
                'bounds'] = [self.doubleSpinBox_ka_origin_min.value(),
                             self.doubleSpinBox_ka_origin_max.value()]

            self.param_info_equation_origin['ki']['fit_option'] = True
            self.param_info_equation_origin['ki'][
                'bounds'] = [self.doubleSpinBox_ki_origin_min.value(),
                             self.doubleSpinBox_ki_origin_max.value()]

            self.param_info_equation_origin['Vi']['fit_option'] = True
            self.param_info_equation_origin['Vi'][
                'bounds'] = [self.doubleSpinBox_Vi_origin_min.value(),
                             self.doubleSpinBox_Vi_origin_max.value()]

            self.param_info_equation_origin['VT']['fit_option'] = True
            self.param_info_equation_origin['VT'][
                'bounds'] = [self.doubleSpinBox_VT_origin_min.value(),
                             self.doubleSpinBox_VT_origin_max.value()]

    def update_equation_rectifier_param_info(self):
        self.param_info_equation_rectifier = {
            'tau_theta': {"fit_option": False, "bounds": [], "fixed_value": 0.0},
            'alpha': {"fit_option": False, "bounds": [], "fixed_value": 0.0},
            'Vi': {"fit_option": False, "bounds": [], "fixed_value": 0.0},
            'VT': {"fit_option": False, "bounds": [], "fixed_value": 0.0}
        }

        if self.checkBox_fixed_rectifier.isChecked():
            self.param_info_equation_rectifier['tau_theta']['fit_option'] = False
            self.param_info_equation_rectifier['tau_theta'][
                'fixed_value'] = self.doubleSpinBox_tao_theta_rectifier_fixed.value()
            self.param_info_equation_rectifier['alpha']['fit_option'] = False
            self.param_info_equation_rectifier['alpha'][
                'fixed_value'] = self.doubleSpinBox_alpha_rectifier_fixed.value()
            self.param_info_equation_rectifier['Vi']['fit_option'] = False
            self.param_info_equation_rectifier['Vi'][
                'fixed_value'] = self.doubleSpinBox_Vi_rectifier_fixed.value()
            self.param_info_equation_rectifier['VT']['fit_option'] = False
            self.param_info_equation_rectifier['VT'][
                'fixed_value'] = self.doubleSpinBox_VT_rectifier_fixed.value()

        else:
            self.param_info_equation_rectifier['tau_theta']['fit_option'] = True
            self.param_info_equation_rectifier['tau_theta'][
                'bounds'] = [self.doubleSpinBox_tao_theta_rectifier_min.value(),
                             self.doubleSpinBox_tao_theta_rectifier_max.value()]
            self.param_info_equation_rectifier['alpha']['fit_option'] = True
            self.param_info_equation_rectifier['alpha'][
                'bounds'] = [self.doubleSpinBox_alpha_rectifier_min.value(),
                             self.doubleSpinBox_alpha_rectifier_max.value()]

            self.param_info_equation_rectifier['Vi']['fit_option'] = True
            self.param_info_equation_rectifier['Vi'][
                'bounds'] = [self.doubleSpinBox_Vi_rectifier_min.value(),
                             self.doubleSpinBox_Vi_rectifier_max.value()]

            self.param_info_equation_rectifier['VT']['fit_option'] = True
            self.param_info_equation_rectifier['VT'][
                'bounds'] = [self.doubleSpinBox_VT_rectifier_min.value(),
                             self.doubleSpinBox_VT_rectifier_max.value()]

    def update_fixed_value_button(self, equation_name, best_solution):
        # 更新最优解至fixed value
        if equation_name == 'FormOne':
            fixed_value_button_group = [self.doubleSpinBox_tao_theta_dynamics_fixed,
                                        self.doubleSpinBox_alpha_dynamics_fixed,
                                        self.doubleSpinBox_ka_dynamics_fixed,
                                        self.doubleSpinBox_ki_dynamics_fixed, self.doubleSpinBox_Vi_dynamics_fixed,
                                        self.doubleSpinBox_VT_dynamics_fixed]
        elif equation_name == 'FormTwo':
            fixed_value_button_group = [self.doubleSpinBox_tao_theta_origin_fixed,
                                        self.doubleSpinBox_ka_origin_fixed,
                                        self.doubleSpinBox_ki_origin_fixed, self.doubleSpinBox_Vi_origin_fixed,
                                        self.doubleSpinBox_VT_origin_fixed]
        elif equation_name == 'FormThree':
            fixed_value_button_group = [self.doubleSpinBox_tao_theta_rectifier_fixed,
                                        self.doubleSpinBox_alpha_rectifier_fixed,
                                        self.doubleSpinBox_Vi_rectifier_fixed,
                                        self.doubleSpinBox_VT_rectifier_fixed]
        for i in range(len(fixed_value_button_group)):
            fixed_value_button_group[i].setValue(best_solution[i])

    def init_ui(self):
        # 恢复上次回话状态 todo

        # 根据公式选项更新参数面板
        if self.equation_index == 1:
            self.stackedWidget_equation_parameters.setCurrentIndex(0)
            self.threshold_equation_name = "FormOne"
        elif self.equation_index == 2:
            self.stackedWidget_equation_parameters.setCurrentIndex(1)
            self.threshold_equation_name = "FormTwo"
        elif self.equation_index == 3:
            self.stackedWidget_equation_parameters.setCurrentIndex(2)
            self.threshold_equation_name = "FormThree"
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
            else:
                self.pushButton_run.setEnabled(True)
    def algorithm_panel_change(self):
        index = self.comboBox_algorithm.currentIndex()
        self.stackedWidget_optimization_algorithm.setCurrentIndex(index)


    def close(self):
        self.equation_option_combobox.setEnabled(True)
        super().close()

    def closeEvent(self, event):
        self.equation_option_combobox.setEnabled(True)
        super().closeEvent(event)

    def append_log(self, message):
        if 'ka' in message:
            pass
        self.plainTextEdit_optimization.appendPlainText(message)

    def on_optimization_finished(self):
        print("最优化完成")
        # 优化线程结束后调用此方法
        self.plainTextEdit_optimization.appendPlainText("Optimization finished or stopped.")  # 更新状态标签
        self.pushButton_run.setEnabled(True)  # 重新启用按钮
        self.pushButton_terminate.setEnabled(False)

        # 恢复 sys.stdout 到其原始状态
        sys.stdout = self._original_stdout
        # 确保线程对象被清理
        # self.optimizer_thread = None # QThread 会自动管理其生命周期，通常不需要手动设置为 None

    def stop_optimization(self):
        print("停止最优化")
        if self.optimizer_thread and self.optimizer_thread.isRunning():
            self.plainTextEdit_optimization.appendPlainText("Requesting optimization interruption...")
            self.pushButton_terminate.setEnabled(False)  # 禁用终止按钮，避免重复点击
            self.optimizer_thread.requestInterruption()  # 向线程发送中断请求
            # 这里requestInterruption() 是非阻塞的，线程不会立即停止
        if not self.optimizer_thread.isRunning():
            self.pushButton_run.setEnabled(False)
            self.pushButton_terminate.setEnabled(True)
            # 恢复 sys.stdout 到其原始状态
        sys.stdout = self._original_stdout

    def ok_clicked(self):
        # 1. 拟合参数最优结果传递
        """
        这里点击OK可能有两种情况，第一种是拟合阈值公式参数，第二种是用户直接设置阈值公式参数。
        这里不准备在OK按钮点击之后，传递单个动作电位数据及阈值稳态值等数据，而是在主界面中点击Run按钮，再生成数据。
        """
        # (1) 判断MethodBasedOnCurvature对象中单个
        pass
        # 2. 最优化参数部分数据进行传递
        if (self.stackedWidget_equation_parameters.currentIndex() + 1) == 1:
            self.get_equation_param_value_dynamics()
        self.close()

    def get_equation_param_value_dynamics(self):
        self.params_res = {}
        self.params_res["tau_theta"] = self.doubleSpinBox_tao_theta_dynamics_fixed.value()
        self.params_res["alpha"] = self.doubleSpinBox_alpha_dynamics_fixed.value()
        self.params_res['ka'] = self.doubleSpinBox_ka_dynamics_fixed.value()
        self.params_res['ki'] = self.doubleSpinBox_ki_dynamics_fixed.value()
        self.params_res['Vi'] = self.doubleSpinBox_Vi_dynamics_fixed.value()
        self.params_res['VT'] = self.doubleSpinBox_VT_dynamics_fixed.value()


# 自定义信号类
class SignalEmitter(QObject):
    update_signal = Signal(str)
    finish_signal = Signal(str)


# 优化线程类
class OptimizerThread(QThread):
    def __init__(self, signal_emitter, object):
        super().__init__()
        self.signal_emitter = signal_emitter
        self.object = object

    def run(self):
        theta_value = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]
        # theta_value = [1.0]
        res = {}
        for i in range(len(theta_value)):
            res[str(theta_value[i])] = {}
            theta = theta_value[i]
            print(theta)
            self.object.doubleSpinBox_time_window_gama_factor.setValue(
                theta)
            for j in range(30):
                patch_name = 'patch' + str(j + 1)
                self.object.fit_equation_parameters()
                best_solution = self.object.best_solution
                res[str(theta_value[i])][patch_name] = {"best_solution":best_solution}
        with open("fitting_result.pkl", 'wb') as f:
            pickle.dump(res,f)
        # self.object.fit_equation_parameters()


# 用于重定向标准输出的类
class StreamRedirector(QObject):
    # 定义一个信号，当有文本写入时发射，携带写入的文本
    text_written = Signal(str)

    def write(self, text):
        # 当有文本写入时，发射 text_written 信号
        self.text_written.emit(str(text))
        # 确保文本也能被实际的标准输出处理
        sys.__stdout__.write(str(text))

    def flush(self):
        # flush 方法是文件类对象所必需的
        sys.__stdout__.flush()
