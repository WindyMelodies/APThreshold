import sys

import h5py
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QWidget, QPushButton, QLabel
from PySide6.QtCore import Slot
from pynwb import NWBHDF5IO
import matplotlib.pyplot as plt


class NWBViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('NWB Viewer')
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.label = QLabel('No file_path selected', self)
        self.layout.addWidget(self.label)

        self.openButton = QPushButton('Open NWB File', self)
        self.openButton.clicked.connect(self.openFileDialog)
        self.layout.addWidget(self.openButton)

        self.plotButton = QPushButton('Plot Data', self)
        self.plotButton.clicked.connect(self.plotData)
        self.layout.addWidget(self.plotButton)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    @Slot()
    def plotData(self):
        if hasattr(self, 'nwbFilePath'):
            try:
                with h5py.File(self.nwbFilePath, 'r') as f:
                    print(f)
                    if 'nwb_version' not in f.attrs:
                        self.label.setText('Not a valid NWB file_path: Missing NWB version')
                        return
            except Exception as e:
                self.label.setText(f'Failed to read file_path: {e}')
                return

            with NWBHDF5IO(self.nwbFilePath, 'r') as io:
                nwbfile = io.read()
                data = nwbfile.get_acquisition('data')  # Assuming 'data' is the name of the acquisition
                timestamps = data.timestamps[:]
                values = data.data_I[:]

                plt.figure()
                plt.plot(timestamps, values)
                plt.xlabel('Time (s)')
                plt.ylabel('Value')
                plt.title('NWB Data Plot')
                plt.show()
        else:
            self.label.setText('No file_path selected')

    @Slot()
    def openFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "Open NWB File", "", "NWB Files (*.nwb);;All Files (*)",
                                                  options=options)
        if fileName:
            self.label.setText(fileName)
            self.nwbFilePath = fileName
            print(f"Selected NWB file_path: {fileName}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = NWBViewer()
    viewer.show()
    sys.exit(app.exec())
