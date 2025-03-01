import pickle
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QPushButton, QWidget, QFileDialog, \
    QLineEdit
from PySide6.QtGui import QStandardItemModel, QStandardItem
import sys
import json


def read_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


dir_data = read_pickle(
    r"D:\ProgramingProject\python\Platform_Development_Yi_adaption\results\RampStimulation.pkl")
dir_data = dir_data['data']
dir_data = {
    'k=1.0': {'timestamp': {'timestamp': np.array([0.0000e+00, 1.0000e-03, 2.0000e-03, ..., 9.9998e+01, 9.9999e+01,
                                                   1.0000e+02]), 'timestamp_Vth': 25.825},
              'voltage': {'Vm': np.array([-67.97472776, -67.9786562, -67.98257188, ..., -69.61170302,
                                          -69.61170302, -69.61170302])},
              'state': {'n': np.array([0.15589198, 0.15589197, 0.15589195, ..., 0.13938085, 0.13938085,
                                       0.13938085])}}}
print(dir_data)


class TreeViewApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tree View with Search")

        # 设置主窗口
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # 创建 QTreeView 和模型
        self.tree_view = QTreeView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Name'])
        self.tree_view.setModel(self.model)
        self.tree_view.setSelectionMode(QTreeView.MultiSelection)

        # 搜索框
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search...")
        self.search_box.textChanged.connect(self.filter_tree)

        # 创建树状结构的数据
        self.populate_tree(dir_data, self.model.invisibleRootItem())

        # 添加刷新按钮
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh_tree)

        # 添加保存按钮
        self.save_button = QPushButton("Save Selected")
        self.save_button.clicked.connect(self.save_selected_data)

        # 布局管理
        self.layout.addWidget(self.search_box)  # 添加搜索框到界面
        self.layout.addWidget(self.tree_view)
        self.layout.addWidget(self.refresh_button)
        self.layout.addWidget(self.save_button)

    def populate_tree(self, data, parent_item):
        """根据字典数据创建树状视图"""
        for key, value in data.items():
            if key != 'label':
                item = QStandardItem(key)
                parent_item.appendRow(item)
                if isinstance(value, dict):
                    self.populate_tree(value, item)
            # else:
            #     value_item = QStandardItem(value)
            #     item.appendRow(value_item)

    def refresh_tree(self):
        """刷新树状结构数据"""
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['Name'])
        self.populate_tree(dir_data, self.model.invisibleRootItem())

    def filter_tree(self, text):
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

    def save_selected_data(self):
        """保存用户选中的数据"""

        selected_indexes = self.tree_view.selectedIndexes()
        print(selected_indexes)
        selected_data = {}

        for index in selected_indexes:
            item = self.model.itemFromIndex(index)

            print('item', item)
            self.extract_selected_data(item, selected_data)

        save_file_path, _ = QFileDialog.getSaveFileName(self, "Save Selected Data", "", "JSON Files (*.json)")
        if save_file_path:
            with open(save_file_path, 'w') as file:
                json.dump(selected_data, file, indent=4)
            print(f"Selected data saved to: {save_file_path}")

    def extract_selected_data(self, item, selected_data):
        """递归提取选中的数据"""
        if not item.hasChildren():
            selected_data[item.text()] = item.parent().text() if item.parent() else item.text()
        else:
            child_data = {}
            for row in range(item.rowCount()):
                child_item = item.child(row)
                self.extract_selected_data(child_item, child_data)
            selected_data[item.text()] = child_data


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TreeViewApp()
    window.show()
    sys.exit(app.exec())
