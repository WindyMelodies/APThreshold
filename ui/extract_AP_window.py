"""Class for extracting """
from ui import Ui_Form_extract_AP
from PySide6.QtWidgets import QWidget
from PySide6 import QtCore


class ExtractAPWindow(QWidget, Ui_Form_extract_AP):
    """
    Extract a single action potential (AP) data either from simulation data or experimental recordings
    """

    def __init__(self, name, mainwindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(name)
        self.setObjectName(name)
        self.name = name
        self.mainwindow = mainwindow
        self.init_ui()
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.setGeometry(QtCore.QRect(400,300,248,125))

    def init_ui(self):
        self.doubleSpinBox_start.setMaximum(1000000000)
        self.doubleSpinBox_stop.setMaximum(1000000000)
        self.pushButton_canel_extract_ap.clicked.connect(self.slot_cancel_clicked)
        self.pushButton_save_extract_ap.clicked.connect(self.SlotSaveClicked)
        # Display the start and stop time of the AP if it exists in the main window
        if self.name in self.mainwindow.AP:
            start = self.mainwindow.AP[self.name]['start']
            stop = self.mainwindow.AP[self.name]['stop']
            self.doubleSpinBox_start.setValue(start)
            self.doubleSpinBox_stop.setValue(stop)

    def slot_cancel_clicked(self):
        self.deleteLater()
        self.mainwindow.names_AP_window.pop(self.name)

    def SlotSaveClicked(self):
        """
        Save the start and stop times of the AP to the main window's AP dictionary.
        """
        self.mainwindow.AP[self.name] = {}
        self.mainwindow.AP[self.name]['start'] = self.doubleSpinBox_start.value()
        self.mainwindow.AP[self.name]['stop'] = self.doubleSpinBox_stop.value()
        self.deleteLater()
        self.mainwindow.names_AP_window.pop(self.name)

    def closeEvent(self, event):
        super().closeEvent(event)
        self.mainwindow.pos_APWindow = self.geometry()


