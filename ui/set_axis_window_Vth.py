"""Class for customize the coordinate axes of one plot. Besides, it provides some visualization options specific to
spike threshold dynamics analysis, including linear fitting and spike threshold point and region display"""
import logging
from ui_set_axis_window_Vth import Ui_widget_Axis_Vth
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QCloseEvent


class SetAxisWindowVth(QWidget, Ui_widget_Axis_Vth):
    def __init__(self, SetFigWindow, data_operation_module, a, b, c):
        super().__init__()

        self.setupUi(self)
        self.data_operation_module = data_operation_module
        self.datas = data_operation_module.data
        self.SetFigWindow = SetFigWindow
        self.a = a
        self.b = b
        self.c = c

        self.SetSlotFunc()

        self.init_ui()

        if str(c) in self.data_operation_module.figure_set[(a, b)]:
            if 'Linear_fitting' in self.data_operation_module.figure_set[(a, b)][str(c)]:
                self.radioButton_linear_fitting.setChecked(True)

    def init_ui(self):

        self.UpdateCombobox(self.comboBox_X_axis, datas=self.datas)
        self.UpdateCombobox(self.comboBox_Y_axis, datas=self.datas)
        if '{}'.format(self.c) in self.data_operation_module.figure_set[(self.a, self.b)]:
            # Initialize user interface based on existing figure settings in figure_set
            x = self.data_operation_module.figure_set[(self.a, self.b)]['{}'.format(self.c)]['x'][0]
            x_main = self.data_operation_module.figure_set[(self.a, self.b)]['{}'.format(self.c)]['x'][1]
            x_sub = self.data_operation_module.figure_set[(self.a, self.b)]['{}'.format(self.c)]['x'][2]
            y = self.data_operation_module.figure_set[(self.a, self.b)]['{}'.format(self.c)]['y'][0]
            y_main = self.data_operation_module.figure_set[(self.a, self.b)]['{}'.format(self.c)]['y'][1]
            y_sub = self.data_operation_module.figure_set[(self.a, self.b)]['{}'.format(self.c)]['y'][2]
            label = self.data_operation_module.figure_set[(self.a, self.b)]['{}'.format(self.c)]['label']

            item_list_X = []
            for i in range(self.comboBox_X_axis.count()):
                item_list_X.append(self.comboBox_X_axis.itemText(i))
            index_X = item_list_X.index(x)
            self.comboBox_X_axis.setCurrentIndex(index_X)

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

            item_list_Y = []
            for i in range(self.comboBox_Y_axis.count()):
                item_list_Y.append(self.comboBox_Y_axis.itemText(i))
            index_Y = item_list_Y.index(y)
            self.comboBox_Y_axis.setCurrentIndex(index_Y)

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
            # Initialize user interface
            item_list_X = []
            for i in range(self.comboBox_X_axis.count()):
                item_list_X.append(self.comboBox_X_axis.itemText(i))
            index_X = item_list_X.index('All')
            self.comboBox_X_axis.setCurrentIndex(index_X)

            item_list_Y = []
            for i in range(self.comboBox_Y_axis.count()):
                item_list_Y.append(self.comboBox_Y_axis.itemText(i))
            index_Y = item_list_Y.index('All')
            self.comboBox_Y_axis.setCurrentIndex(index_Y)

    def SetSlotFunc(self):
        self.comboBox_X_axis_main.currentIndexChanged.connect(self.UpdateSubXDatas)
        self.comboBox_Y_axis_main.currentIndexChanged.connect(self.UpdateSubYDatas)
        self.radioButton_linear_fitting.toggled.connect(self.cancel_fitting)
        self.comboBox_X_axis.currentIndexChanged.connect(self.UpdateMainXDatas)
        self.comboBox_Y_axis.currentIndexChanged.connect(self.UpdateMainYDatas)
        self.pushButton_Save.clicked.connect(self.save)
        self.pushButton_Cancel.clicked.connect(self.SlotCancelClicked)

    def cancel_fitting(self):
        if not self.radioButton_linear_fitting.isChecked():
            if 'Linear_fitting' in self.data_operation_module.figure_set[(self.a, self.b)][str(self.c)]:
                self.data_operation_module.figure_set[(self.a, self.b)][str(self.c)].pop('Linear_fitting')

    def SlotCancelClicked(self):
        self.close()
        self.deleteLater()

    def UpdateMainXDatas(self):
        self.comboBox_X_axis_main.clear()
        X_value = self.comboBox_X_axis.currentText()
        for i in self.datas[X_value]:
            self.comboBox_X_axis_main.addItem(i)

    def UpdateMainYDatas(self):
        self.comboBox_Y_axis_main.clear()
        Y_value = self.comboBox_Y_axis.currentText()
        for i in self.datas[Y_value]:
            self.comboBox_Y_axis_main.addItem(i)

    def UpdateSubXDatas(self):

        self.comboBox_X_axis_sub.clear()
        x_value = self.comboBox_X_axis.currentText()
        X_main_value = self.comboBox_X_axis_main.currentText()
        if X_main_value == '':
            pass
        else:
            for i in self.datas[x_value][X_main_value]:
                if i == 'label':
                    pass
                else:
                    self.comboBox_X_axis_sub.addItem(i)

    def UpdateSubYDatas(self):
        self.comboBox_Y_axis_sub.clear()
        y_value = self.comboBox_Y_axis.currentText()
        Y_main_value = self.comboBox_Y_axis_main.currentText()
        if Y_main_value == '':
            pass
        else:
            for i in self.datas[y_value][Y_main_value]:
                if i == 'label':
                    pass
                else:
                    self.comboBox_Y_axis_sub.addItem(i)

    def UpdateCombobox(self, combobox, datas):
        for i in datas:
            combobox.addItem(i)

    def save(self):
        """
        Save the current visualization settings and displays them in text browser
        """
        x = self.comboBox_X_axis.currentText()
        y = self.comboBox_Y_axis.currentText()
        x_main = self.comboBox_X_axis_main.currentText()
        x_sub = self.comboBox_X_axis_sub.currentText()
        y_main = self.comboBox_Y_axis_main.currentText()
        y_sub = self.comboBox_Y_axis_sub.currentText()
        label = self.lineEdit_label.text()
        text1 = 'x:' + x_sub
        text2 = 'y:' + y_sub
        text3 = 'label:' + label
        text4 = None
        if self.radioButton_linear_fitting.isChecked():
            self.data_operation_module.figure_set[(self.a, self.b)]['{}'.format(self.c)] = {'x': (x, x_main, x_sub),
                                                                                            'y': (y, y_main, y_sub),
                                                                                            'label': label,
                                                                                            'Linear_fitting': True}
            text4 = 'Linear fitting'

        else:
            self.data_operation_module.figure_set[(self.a, self.b)]['{}'.format(self.c)] = {'x': (x, x_main, x_sub),
                                                                                            'y': (y, y_main, y_sub),
                                                                                            'label': label}

        textBrowser_name = 'textBrowser_fig_{}_{}_plot_{}'.format(self.a, self.b, self.c)
        self.SetFigWindow.names[textBrowser_name].clear()
        self.SetFigWindow.names[textBrowser_name].append(text1)
        self.SetFigWindow.names[textBrowser_name].append(text2)
        self.SetFigWindow.names[textBrowser_name].append(text3)
        if text4:
            self.SetFigWindow.names[textBrowser_name].append(text4)
        self.close()
        self.deleteLater()

    def closeEvent(self, event: QCloseEvent) -> None:
        super().closeEvent(event)
        self.deleteLater()
