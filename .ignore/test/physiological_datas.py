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

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Single Neuron Data Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        self.channel_selector = QComboBox()
        self.channel_selector.addItems([f"Channel {i+1}" for i in range(8)])
        self.channel_selector.currentIndexChanged.connect(self.update_plot)

        button = QPushButton('Load Data')
        button.clicked.connect(self.load_data)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.channel_selector)
        layout.addWidget(self.text_edit)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.data = None
        self.sampling_rate = 10000

    def load_data(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Data File", "", "Data Files (*.dat);;All Files (*)", options=options)
        if file_name:
            self.data = self.read_data(file_name)
            self.update_plot()

    def read_data(self, file_name):
        # 数据格式和参数
        data_type = np.int16  # 数据类型为short integer（2 bytes）
        num_channels = 8  # 总通道数
        sampling_rate = 10000  # 采样率，10000 Hz

        # 读取二进制文件
        data = np.fromfile(file_name, dtype=data_type)
        num_samples = data.size // num_channels
        data = data.reshape((num_samples, num_channels))

        # 显示原始数据前几行
        raw_data_str = '\n'.join(['\t'.join(map(str, data[i, :])) for i in range(min(10, num_samples))])
        self.text_edit.setText(raw_data_str)

        # 更新状态栏信息
        self.statusBar.showMessage(f"Loaded {file_name} - Samples: {num_samples}, Channels: {num_channels}")

        return data

    def update_plot(self):
        if self.data is None:
            return

        selected_channel = self.channel_selector.currentIndex()
        channel_data = self.data[:, selected_channel]
        num_samples = channel_data.size
        time = np.arange(num_samples) / self.sampling_rate

        # 绘制数据
        self.canvas.axes.clear()
        self.canvas.axes.plot(time, channel_data)
        self.canvas.axes.set_xlabel('Time (s)')
        self.canvas.axes.set_ylabel('Voltage (mV)')
        self.canvas.axes.set_title(f'Channel {selected_channel + 1}')
        self.canvas.draw()

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())
