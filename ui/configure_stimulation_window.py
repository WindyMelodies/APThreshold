import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui.ui_configure_stimulation_window import Ui_configure_stimulation_window


class ConfigureStimulationWindow(QWidget, Ui_configure_stimulation_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBox_type_list = [self.comboBox_type, self.comboBox_type_2, self.comboBox_type_3, self.comboBox_type_4,
                                   self.comboBox_type_5]
        self.doubleSpinBox_start_list = [self.doubleSpinBox_start, self.doubleSpinBox_start_2,
                                         self.doubleSpinBox_start_3, self.doubleSpinBox_start_4,
                                         self.doubleSpinBox_start_5]
        self.doubleSpinBox_stop_list = [self.doubleSpinBox_stop, self.doubleSpinBox_stop_2, self.doubleSpinBox_stop_3,
                                        self.doubleSpinBox_stop_4, self.doubleSpinBox_stop_5]

        self.signal_slot()

    def signal_slot(self):
        for i in self.comboBox_type_list:
            i.currentIndexChanged.connect(self.slot_currentIndexChanged)

        for i in self.doubleSpinBox_start_list:
            i.valueChanged.connect(self.slot_valueChanged_start)

        for i in self.doubleSpinBox_stop_list:
            i.valueChanged.connect(self.slot_valueChanged_stop)

    def slot_currentIndexChanged(self):
        sender = self.sender()
        index = sender.currentIndex()
        self.stackedWidget.setCurrentIndex(index)
        for i in self.comboBox_type_list:
            i.setCurrentIndex(index)

    def slot_valueChanged_start(self):
        sender = self.sender()
        value = sender.value()
        for i in self.doubleSpinBox_start_list:
            i.setValue(value)

    def slot_valueChanged_stop(self):
        sender = self.sender()
        value = sender.value()
        for i in self.doubleSpinBox_stop_list:
            i.setValue(value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ConfigureStimulationWindow()
    w.show()
    app.exec()
