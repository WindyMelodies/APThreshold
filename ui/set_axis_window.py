"""Class for customize the coordinate axes of one plot"""
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QWidget
from .ui_set_axis_window import Ui_widget_Axis_AP


class SetAxisWindow(QWidget, Ui_widget_Axis_AP):

    def __init__(self, SetFigWindow, a, b, c):
        super().__init__()
        self.setupUi(self)
        self.set_slot_func()
        self.SetFigWindow = SetFigWindow
        self.a = a
        self.b = b
        self.c = c
        self.data_operation_module = self.SetFigWindow.data_operation_module
        self.init_ui()

    def init_ui(self):
        for i in self.data_operation_module.data:
            self.comboBox_X_axis_main.addItem(i)
            self.comboBox_Y_axis_main.addItem(i)
        self.update_sub_x_data()
        self.update_sub_y_data()

        if '{}'.format(self.c) in self.data_operation_module.figure_set[(self.a, self.b)]:
            x_main = self.data_operation_module.figure_set[(self.a, self.b)]['{}'.format(self.c)]['x'][0]
            x_sub = self.data_operation_module.figure_set[(self.a, self.b)]['{}'.format(self.c)]['x'][1]
            y_main = self.data_operation_module.figure_set[(self.a, self.b)]['{}'.format(self.c)]['y'][0]
            y_sub = self.data_operation_module.figure_set[(self.a, self.b)]['{}'.format(self.c)]['y'][1]
            label = self.data_operation_module.figure_set[(self.a, self.b)]['{}'.format(self.c)]['label']

            item_list_X_main = []
            for i in range(self.comboBox_X_axis_main.count()):
                item_list_X_main.append(self.comboBox_X_axis_main.itemText(i))
            index_X_main = item_list_X_main.index(x_main)
            self.comboBox_X_axis_main.setCurrentIndex(index_X_main)

            item_list_X_sub = []
            for i in range(self.comboBox_X_axis_sub.count()):
                item_list_X_sub.append(self.comboBox_X_axis_sub.itemText(i))
            index_X_sub = item_list_X_sub.index(x_sub)
            self.comboBox_X_axis_sub.setCurrentIndex(index_X_sub)

            item_list_Y_main = []
            for i in range(self.comboBox_Y_axis_main.count()):
                item_list_Y_main.append(self.comboBox_Y_axis_main.itemText(i))
            index_Y_main = item_list_Y_main.index(y_main)
            self.comboBox_Y_axis_main.setCurrentIndex(index_Y_main)

            item_list_Y_sub = []
            for i in range(self.comboBox_Y_axis_sub.count()):
                item_list_Y_sub.append(self.comboBox_Y_axis_sub.itemText(i))
            index_Y_sub = item_list_Y_sub.index(y_sub)
            self.comboBox_Y_axis_sub.setCurrentIndex(index_Y_sub)

            self.lineEdit_label.setText(label)
        else:
            try:
                item_list_X_main = []
                for i in range(self.comboBox_X_axis_main.count()):
                    item_list_X_main.append(self.comboBox_X_axis_main.itemText(i))
                index_X_main = item_list_X_main.index('timeline')
                self.comboBox_X_axis_main.setCurrentIndex(index_X_main)

                item_list_X_sub = []
                for i in range(self.comboBox_X_axis_sub.count()):
                    item_list_X_sub.append(self.comboBox_X_axis_sub.itemText(i))
                index_X_sub = item_list_X_sub.index('t')
                self.comboBox_X_axis_sub.setCurrentIndex(index_X_sub)
                self.lineEdit_label.setText(self.comboBox_Y_axis_sub.currentText())
            except:
                pass

    def update_sub_x_data(self):
        self.comboBox_X_axis_sub.clear()
        X_main_value = self.comboBox_X_axis_main.currentText()
        for i in self.data_operation_module.data[X_main_value]:
            if i == 'label':
                pass
            else:
                self.comboBox_X_axis_sub.addItem(i)

    def update_sub_y_data(self):
        self.comboBox_Y_axis_sub.clear()
        Y_main_value = self.comboBox_Y_axis_main.currentText()
        for i in self.data_operation_module.data[Y_main_value]:
            if i == 'label':
                pass
            else:
                self.comboBox_Y_axis_sub.addItem(i)

    def set_slot_func(self):
        """Connect the user interface elements to their respective slots."""
        self.pushButton_Cancel.clicked.connect(self.slot_cancel_clicked)
        self.comboBox_X_axis_main.currentIndexChanged.connect(self.update_sub_x_data)
        self.comboBox_Y_axis_main.currentIndexChanged.connect(self.update_sub_y_data)
        self.pushButton_Save.clicked.connect(self.slot_save_clicked)

    def slot_cancel_clicked(self):
        self.close()
        self.deleteLater()

    def slot_save_clicked(self):
        """Handle the save button click event and update the figure settings."""
        x_main = self.comboBox_X_axis_main.currentText()
        x_sub = self.comboBox_X_axis_sub.currentText()
        y_main = self.comboBox_Y_axis_main.currentText()
        y_sub = self.comboBox_Y_axis_sub.currentText()
        label = self.lineEdit_label.text()
        self.data_operation_module.figure_set[(self.a, self.b)]['{}'.format(self.c)] = {'x': (x_main, x_sub),
                                                                                        'y': (y_main, y_sub),
                                                                                        'label': label}
        textBrowser_name = 'textBrowser_fig_{}_{}_plot_{}'.format(self.a, self.b, self.c)
        self.SetFigWindow.names[textBrowser_name].clear()
        x_length = len(self.data_operation_module.data[x_main][x_sub])
        y_length = len(self.data_operation_module.data[y_main][y_sub])
        text1 = 'x:' + x_sub + '  ' + 'length:' + '{}'.format(x_length)
        text2 = 'y:' + y_sub + '  ' + 'length:' + '{}'.format(y_length)
        text3 = 'label:' + label
        self.SetFigWindow.names[textBrowser_name].append(text1)
        self.SetFigWindow.names[textBrowser_name].append(text2)
        self.SetFigWindow.names[textBrowser_name].append(text3)
        self.close()
        self.deleteLater()

    def closeEvent(self, event: QCloseEvent) -> None:
        super().closeEvent(event)
        self.deleteLater()
