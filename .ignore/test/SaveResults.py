import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QLabel, QSpinBox, QComboBox, \
    QDoubleSpinBox, QPushButton, QMessageBox, QTableWidgetItem, QAbstractItemView, QSplashScreen, QTabWidget, QToolBox, \
    QGroupBox, QHeaderView, QTreeView, QFileDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui.ui_sava_result_window import Ui_save_results
import pickle

with open(r"D:\ProgramingProject\python\Platform_Development_Yi_adaption\results\RampStimulation.pkl", 'rb') as f:
    dir_data = pickle.load(f)
    dir_data = dir_data['data']


class SaveResultsWindow(QWidget, Ui_save_results):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Name'])
        self.treeView.setModel(self.model)
        self.treeView.setSelectionMode(QTreeView.MultiSelection)
        # 创建树状结构的数据
        self.populate_tree(dir_data, self.model.invisibleRootItem())
        # # 搜索框
        # self.lineEdit_search.textChanged.connect(self.filter_tree)
        #
        # # 设置刷新按钮
        # self.pushButton_refresh.clicked.connect(self.refresh_tree)


    def populate_tree(self, data, parent_item):
        """根据字典数据创建树状视图"""
        for key, value in data.items():
            item = QStandardItem(key)
            parent_item.appendRow(item)
            if isinstance(value, dict):
                self.populate_tree(value, item)
            else:
                print(value)
                value_item = QStandardItem(value)
                item.appendRow(value_item)

    def filter_tree(self, text, dir_data):
        """根据搜索框的内容过滤树状视图"""
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['Name'])
        filtered_data = self.search_in_dict(dir_data, text)
        self.populate_tree(filtered_data, self.model.invisibleRootItem())

    def search_in_dict(self, data, search_text):
        """递归搜索字典，返回符合搜索条件的数据"""
        result = {}
        for key, value in data.items():
            if search_text.lower() in key.lower():
                result[key] = value
            elif isinstance(value, dict):
                nested_result = self.search_in_dict(value, search_text)
                if nested_result:
                    result[key] = nested_result
        return result

    def refresh_tree(self):
        """刷新树状结构数据"""
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['Name'])
        self.populate_tree(dir_data, self.model.invisibleRootItem())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SaveResultsWindow()
    w.show()
    app.exec()
