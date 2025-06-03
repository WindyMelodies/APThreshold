from ui.ui_threshold_euqation_method_main_window import Ui_threshold_euqation_method_main_window
from ui.ui_threshold_equation_method_workflow_1_panel import Ui_workflow_1_panel
from PySide6.QtWidgets import QWidget


class ThresholdEquationMethodMainWindow(QWidget, Ui_threshold_euqation_method_main_window):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ThresholdEquationMethodWorkflowOneWindow(QWidget, Ui_workflow_1_panel):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
