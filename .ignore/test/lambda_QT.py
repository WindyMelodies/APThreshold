import sys

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
    QFileDialog, QTextEdit, QStatusBar, QLabel, QComboBox, QToolBar, QHBoxLayout
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from utils.custom_navigation_toolbar import CustomNavigationToolbar as NavigationToolbar
from matplotlib.figure import Figure


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.layout = QHBoxLayout(self)
        self.button = QPushButton(text='abc')
        self.layout.addWidget(self.button)
        self.button.clicked.connect(lambda d=1, a=1, b=1, c=1: self.slot_func(a=a, b=b, c=c))

    def slot_func(self, a, b, c):
        print(a, b, c)


app = QApplication(sys.argv)
a = Window()
a.show()
print(a.__name__)
app.exec()
