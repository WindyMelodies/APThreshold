# -*- coding: UTF-8 -*
"""
Main module to initialize and run APThreshold
"""
import os
import sys
import logging
from matplotlib import pyplot as plt
from PySide6.QtWidgets import QApplication, QStyleFactory
from ui.main_window import MainWindow

# os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.path.join(sys.prefix, "Lib", "site-packages", "PySide6",  "plugins", "platforms")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # Configure matplotlib plot parameters
    plt.rcParams['font.size'] = 10
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    plt.rcParams['savefig.dpi'] = 400

    # Run APThreshold application
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("windowsvista"))
    w = MainWindow()
    w.show()

    a = 3
    if a == 1:
        w.comboBox_model.setCurrentIndex(4)
        w.names['doubleSpinBox_stim1_stop'].setValue(200)
        w.names['doubleSpinBox_stim1_amplitude'].setValue(10)
        # OU噪声刺激HH模型生成不规则放电序列
        w.spinBox_timeline.setValue(200)
        w.doubleSpinBox_dt.setValue(0.01)
        w.pushButton_simulation_run.click()
        w.pushButton_auto_extrac_APs.click()
        w.pushButton_run_curvature.click()
        w.threshold_equation_main_window.pushButton_workflow_1.click()
        w.threshold_equation_workflow_1_panel.pushButton_config_threshold_params_workflow_1.click()
        w.threshold_equation_workflow_1_panel.configure_parameters_window.pushButton_OK.click()
    elif a == 2:
        w.comboBox_model.setCurrentIndex(4)
        stop = 200
        tab_name = 'stim1'

        w.names['comboBox_' + tab_name].setCurrentIndex(3)
        w.names['doubleSpinBox_stim1_stop'].setValue(stop)
        w.names['doubleSpinBox_' + tab_name + '_mu'].setValue(10)
        w.names['doubleSpinBox_' + tab_name + '_theta'].setValue(3)
        w.names['doubleSpinBox_' + tab_name + '_sigma'].setValue(5)

        # OU噪声刺激HH模型生成不规则放电序列

        w.spinBox_timeline.setValue(stop)
        w.doubleSpinBox_dt.setValue(0.01)
        w.comboBox_ode_option.setCurrentIndex(1)
        w.pushButton_simulation_run.click()
        w.pushButton_auto_extrac_APs.click()
        # w.pushButton_run_curvature.click()
        # w.threshold_equation_main_window.pushButton_workflow_1.click()
        # w.threshold_equation_workflow_1_panel.pushButton_config_threshold_params_workflow_1.click()

    app.exec()
