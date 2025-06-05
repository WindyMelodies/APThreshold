from PySide6.QtGui import QPixmap, QImage
from matplotlib import pyplot as plt
from io import BytesIO

from ui.configure_equation_parameters_workflow1 import ConfigureEquationParametersWindow
from ui.html_mathml import html_mathml_1, html_mathml_2, html_mathml_3
from ui.ui_threshold_euqation_method_main_window import Ui_threshold_euqation_method_main_window
from ui.ui_threshold_equation_method_workflow_1_panel import Ui_workflow_1_panel
from PySide6.QtWidgets import QWidget


class ThresholdEquationMethodMainWindow(QWidget, Ui_threshold_euqation_method_main_window):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ThresholdEquationMethodWorkflowOneWindow(QWidget, Ui_workflow_1_panel):

    def __init__(self, main_window):
        self.main_window = main_window
        super().__init__()
        self.configure_parameters_window = None
        self.setupUi(self)
        self.signal_slot()
        self.show_equation_form()

    def signal_slot(self):
        self.comboBox_threshold_equation_option_workflow_1.currentIndexChanged.connect(self.show_equation_form)
        self.webEngineView_threshold_equation_workflow_1.page().loadFinished.connect(self.adjust_height)
        self.pushButton_config_threshold_params_workflow_1.clicked.connect(self.show_configure_equation_params_window)

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
