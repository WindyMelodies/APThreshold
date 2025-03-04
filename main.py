# -*- coding: UTF-8 -*
"""
Main module to initialize and run APThreshold
"""
import os
import sys
import logging
from matplotlib import pyplot as plt
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)

    # Configure matplotlib plot parameters
    plt.rcParams['font.size'] = 10
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    plt.rcParams['savefig.dpi'] = 400

    # Run APThreshold application
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
