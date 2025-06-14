"""
A window class for customizing visualization settings in the 'Spike threshold' tab.
This window is triggered when the 'Set Plot' button is clicked.
"""

import copy
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QWidget, QPushButton, QTextBrowser, QSizePolicy
from .set_axis_window_Vth import SetAxisWindowVth
from .ui_set_fig_window_Vth import Ui_setwidget_spike_threshold
from utils.plotting import Plotting


class SetFigWindowVth(QWidget, Ui_setwidget_spike_threshold):
    """
    This class provides a customizable plotting interface that opens when the "Set Plot" button is clicked on the spike
    threshold interface. It offers the following functionalities:
        1、Select x-axis and y-axis data using SetAxisWindow.
        2、Provide options of marking threshold points or region.
        3、Add, delete, and modify plot settings.
    """

    def __init__(self, main_window, data_operation_module):
        super().__init__()
        # Parameter passing and variable creation
        self.names = None
        self.plotting = None
        self.main_window = main_window
        self.data_operation_module = data_operation_module
        self.figure_set = self.data_operation_module.figure_set
        # Initialize the user interface (UI)
        self.setupUi(self)
        self.set_ui()
        self.add_plot_button_and_browser()
        self.init_ratio_button()
        self.set_slot_func()

    def set_ui(self):
        self.pushButton_clear_figure_1_1.setCheckable(True)
        self.pushButton_clear_figure_1_2.setCheckable(True)
        self.pushButton_clear_figure_2_1.setCheckable(True)
        self.pushButton_clear_figure_2_2.setCheckable(True)
        self.names = {'scrollAreaWidgetContents_figure_1_1': self.scrollAreaWidgetContents_figure_1_1,
                      'scrollAreaWidgetContents_figure_1_2': self.scrollAreaWidgetContents_figure_1_2,
                      'scrollAreaWidgetContents_figure_2_1': self.scrollAreaWidgetContents_figure_2_1,
                      'scrollAreaWidgetContents_figure_2_2': self.scrollAreaWidgetContents_figure_2_2,
                      'scrollArea_figure_1_1': self.scrollArea_figure_1_1,
                      'scrollArea_figure_2_2': self.scrollArea_figure_2_2,
                      'scrollArea_figure_2_1': self.scrollArea_figure_2_1,
                      'scrollArea_figure_1_2': self.scrollArea_figure_1_2,
                      'gridLayout_figure_1_1': self.gridLayout_figure_1_1,
                      'gridLayout_figure_1_2': self.gridLayout_figure_1_2,
                      'gridLayout_figure_2_1': self.gridLayout_figure_2_1,
                      'gridLayout_figure_2_2': self.gridLayout_figure_2_2,
                      'pushButton_add_plot_figure_1_1': self.pushButton_add_plot_figure_1_1,
                      'pushButton_clear_figure_1_1': self.pushButton_clear_figure_1_1,
                      'pushButton_add_plot_figure_1_2': self.pushButton_add_plot_figure_1_2,
                      'pushButton_clear_figure_1_2': self.pushButton_clear_figure_1_2,
                      'pushButton_add_plot_figure_2_1': self.pushButton_add_plot_figure_2_1,
                      'pushButton_clear_figure_2_1': self.pushButton_clear_figure_2_1,
                      'pushButton_add_plot_figure_2_2': self.pushButton_add_plot_figure_2_2,
                      'pushButton_clear_figure_2_2': self.pushButton_clear_figure_2_2,
                      'radioButton_threshold_points_figure_1_1': self.radioButton_threshold_points_figure_1_1,
                      'radioButton_threshold_points_figure_1_2': self.radioButton_threshold_points_figure_1_2,
                      'radioButton_threshold_points_figure_2_1': self.radioButton_threshold_points_figure_2_1,
                      'radioButton_threshold_points_figure_2_2': self.radioButton_threshold_points_figure_2_2,
                      'radioButton_threshold_range_figure_1_1': self.radioButton_threshold_range_figure_1_1,
                      'radioButton_threshold_range_figure_1_2': self.radioButton_threshold_range_figure_1_2,
                      'radioButton_threshold_range_figure_2_1': self.radioButton_threshold_range_figure_2_1,
                      'radioButton_threshold_range_figure_2_2': self.radioButton_threshold_range_figure_2_2}

    def set_slot_func(self):
        self.pushButton_reset.clicked.connect(self.reset)
        self.pushButton_apply.clicked.connect(self.apply)
        axes = [(1, 1), (1, 2), (2, 1), (2, 2)]
        for i in axes:
            self.names['pushButton_clear_figure_{}_{}'.format(i[0], i[1])].toggled.connect(
                lambda a=1, b=i[0], c=i[1]: self.slot_clear_toggled(a=b, b=c))
            self.names['pushButton_add_plot_figure_{}_{}'.format(i[0], i[1])].clicked.connect(
                lambda c=1, a=i[0], b=i[1]: self.AddPlot(a=a, b=b))
            self.names['radioButton_threshold_range_figure_{}_{}'.format(i[0], i[1])].toggled.connect(
                lambda c=1, a=i[0], b=i[1]: self.change_figure_set_threshold_range(a=a, b=b))
            self.names['radioButton_threshold_points_figure_{}_{}'.format(i[0], i[1])].toggled.connect(
                lambda c=1, a=i[0], b=i[1]: self.change_figure_set_threshold_points(a=a, b=b))

    def change_figure_set_threshold_range(self, a, b):
        if self.names['radioButton_threshold_range_figure_{}_{}'.format(a, b)].isChecked():
            self.figure_set[(a, b)]['Vth_range'] = True
        else:
            self.figure_set[(a, b)].pop('Vth_range')

    def change_figure_set_threshold_points(self, a, b):
        if self.names['radioButton_threshold_points_figure_{}_{}'.format(a, b)].isChecked():
            self.figure_set[(a, b)]['Vth_points'] = True
        else:
            self.figure_set[(a, b)].pop('Vth_points')

    def init_ratio_button(self):
        axes = [(1, 1), (1, 2), (2, 1), (2, 2)]
        for i in axes:
            for j in self.figure_set[i]:
                if j == 'Vth_points':
                    if self.figure_set[i][j]:
                        self.names['radioButton_threshold_points_figure_{}_{}'.format(i[0], i[1])].setChecked(True)
                elif j == 'Vth_range':
                    if self.figure_set[i][j]:
                        self.names['radioButton_threshold_range_figure_{}_{}'.format(i[0], i[1])].setChecked(True)

    def add_plot_button_and_browser(self):
        """
        Initializes the window based on figure_set and displays relevant information.
            1. Adds plot buttons
            2. Adds a text browser to display plot information.
        """
        axes = [(1, 1), (1, 2), (2, 1), (2, 2)]
        for i in axes:
            for j in self.figure_set[i]:
                if j != 'Vth_points' and j != 'Vth_range':

                    self.names['pushButton_fig_{}_{}_plot_{}'.format(i[0], i[1], j)] = QPushButton(
                        self.names['scrollAreaWidgetContents_figure_{}_{}'.format(i[0], i[1])])
                    self.names['pushButton_fig_{}_{}_plot_{}'.format(i[0], i[1], j)].setObjectName(
                        'pushButton_fig_{}_{}_plot_{}'.format(i[0], i[1], j))
                    self.names['pushButton_fig_{}_{}_plot_{}'.format(i[0], i[1], j)].setText('plot_{}'.format(j))

                    self.names['pushButton_fig_{}_{}_plot_{}'.format(i[0], i[1], j)].clicked.connect(
                        lambda d=1, a=i[0], b=i[1], c=int(j): self.show_axis_window(a=a, b=b, c=c))
                    self.names['gridLayout_figure_{}_{}'.format(i[0], i[1])].addWidget(
                        self.names['pushButton_fig_{}_{}_plot_{}'.format(i[0], i[1], j)], int(j), 0, 1, 1)
                    sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)

                    self.names['textBrowser_fig_{}_{}_plot_{}'.format(i[0], i[1], j)] = QTextBrowser(
                        self.names['scrollAreaWidgetContents_figure_{}_{}'.format(i[0], i[1])])
                    self.names['textBrowser_fig_{}_{}_plot_{}'.format(i[0], i[1], j)].setObjectName(
                        'textBrowser_fig_{}_{}_plot_{}'.format(i[0], i[1], j))
                    self.names['gridLayout_figure_{}_{}'.format(i[0], i[1])].addWidget(
                        self.names['textBrowser_fig_{}_{}_plot_{}'.format(i[0], i[1], j)], int(j), 1, 1, 1)
                    sizePolicy.setHeightForWidth(self.names['textBrowser_fig_{}_{}_plot_{}'.format(i[0], i[1],
                                                                                                   j)].sizePolicy().hasHeightForWidth())
                    self.text_browser_add_text(self.names['textBrowser_fig_{}_{}_plot_{}'.format(i[0], i[1], j)],
                                               a=i[0], b=i[1], c=int(j))

    def text_browser_add_text(self, TextBrowser, a, b, c):
        """
        Update the text in the TextBrowser widget to display the x and y data information for its corresponding plot

        a (int): The x-coordinate of figure position.
        b (int): The y-coordinate of figure position.
        c (int): The plot number.
        """
        TextBrowser.clear()
        x_sub = self.figure_set[(a, b)]['{}'.format(c)]['x']
        y_sub = self.figure_set[(a, b)]['{}'.format(c)]['y']

        text1 = 'x:' + str(x_sub)
        text2 = 'y:' + str(y_sub)

        TextBrowser.append(text1)
        TextBrowser.append(text2)


    def reset(self):
        """Reset the plot settings to the initial configuration and add the plot buttons and text browsers again."""

        self.data_operation_module.figure_set = copy.deepcopy(self.data_operation_module.figure_set_origin)
        self.figure_set = self.data_operation_module.figure_set

        axes = [(1, 1), (1, 2), (2, 1), (2, 2)]

        for i in axes:

            list_item = list(range(self.names['gridLayout_figure_{}_{}'.format(i[0], i[1])].count()))
            list_item.reverse()
            for j in list_item:
                item = self.names['gridLayout_figure_{}_{}'.format(i[0], i[1])].itemAt(j)
                if item.widget():
                    item.widget().deleteLater()
                else:
                    self.names['gridLayout_figure_{}_{}'.format(i[0], i[1])].removeItem(item)
        self.add_plot_button_and_browser()

    def apply(self):
        """Apply the current figure settings and draw plot"""
        self.plotting = Plotting(data=self.data_operation_module.data, figure_set=self.data_operation_module.figure_set,
                                 axes=self.main_window.names['axes_Vth'])
        self.main_window.names['Canvas_Vth'].draw()
        self.main_window.names_window.pop('SetFigWindow_Vth')
        self.deleteLater()

    def slot_clear_toggled(self, a, b):
        list_pushbutton = self.names['scrollArea_figure_{}_{}'.format(a, b)].findChildren(QPushButton)
        list_pushbutton_names = []
        for i in list_pushbutton:
            list_pushbutton_names.append(i.objectName())
        for j in range(len(list_pushbutton_names)):
            list_pushbutton_names[j] = int(list_pushbutton_names[j][24:])
        if self.names['pushButton_clear_figure_{}_{}'.format(a, b)].isChecked():
            for i in list_pushbutton_names:
                self.names['pushButton_fig_{}_{}_plot_{}'.format(a, b, i)].clicked.disconnect()
                self.names['pushButton_fig_{}_{}_plot_{}'.format(a, b, i)].clicked.connect(
                    lambda d=1, a=a, b=b, c=i: self.delete_widgets(a, b, c))
        else:
            for i in list_pushbutton_names:
                self.names['pushButton_fig_{}_{}_plot_{}'.format(a, b, i)].clicked.disconnect()
                self.names['pushButton_fig_{}_{}_plot_{}'.format(a, b, i)].clicked.connect(
                    lambda d=1, a=a, b=b, c=i: self.show_axis_window(a=a, b=b, c=c))

    def delete_widgets(self, a, b, c):
        self.names['pushButton_fig_{}_{}_plot_{}'.format(a, b, c)].deleteLater()
        self.names['textBrowser_fig_{}_{}_plot_{}'.format(a, b, c)].deleteLater()
        self.names.pop('pushButton_fig_{}_{}_plot_{}'.format(a, b, c))
        self.names.pop('textBrowser_fig_{}_{}_plot_{}'.format(a, b, c))
        if str(c) in self.data_operation_module.figure_set[(a, b)]:
            self.data_operation_module.figure_set[(a, b)].pop(str(c))

    def AddPlot(self, a, b):
        if self.names['pushButton_clear_figure_{}_{}'.format(a, b)].isChecked():
            self.names['pushButton_clear_figure_{}_{}'.format(a, b)].toggle()
        list_pushbutton = self.names['scrollArea_figure_{}_{}'.format(a, b)].findChildren(QPushButton)
        list_pushbutton_names = []
        for i in list_pushbutton:
            list_pushbutton_names.append(i.objectName())
        for j in range(len(list_pushbutton_names)):
            list_pushbutton_names[j] = int(list_pushbutton_names[j][24:])

        if list_pushbutton_names == []:
            num = 1
        else:
            num = max(list_pushbutton_names) + 1
        button_name = 'pushButton_fig_{}_{}_plot_{}'.format(a, b, num)
        textBrowser_name = 'textBrowser_fig_{}_{}_plot_{}'.format(a, b, num)
        self.names[button_name] = QPushButton(self.names['scrollAreaWidgetContents_figure_{}_{}'.format(a, b)])
        self.names[button_name].setObjectName(button_name)
        self.names[button_name].setText('plot_{}'.format(num))
        self.names[button_name].clicked.connect(lambda d=1, a=a, b=b, c=num: self.show_axis_window(a=a, b=b, c=c))
        self.names['gridLayout_figure_{}_{}'.format(a, b)].addWidget(self.names[button_name], num, 0, 1, 1)

        self.names[textBrowser_name] = QTextBrowser(self.names['scrollAreaWidgetContents_figure_{}_{}'.format(a, b)])
        self.names[textBrowser_name].setObjectName(textBrowser_name)
        self.names['gridLayout_figure_{}_{}'.format(a, b)].addWidget(self.names[textBrowser_name], num, 1, 1, 1)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.names[textBrowser_name].sizePolicy().hasHeightForWidth())

    def show_axis_window(self, a, b, c):
        self.names['AxisWindow_Figure_{}_{}_{}'.format(a, b, c)] = SetAxisWindowVth(SetFigWindow=self,
                                                                                    data_operation_module=self.data_operation_module,
                                                                                    a=a,
                                                                                    b=b, c=c)
        self.names['AxisWindow_Figure_{}_{}_{}'.format(a, b, c)].show()

    def closeEvent(self, event: QCloseEvent) -> None:
        super().closeEvent(event)
        if 'SetFigWindow_Vth' in self.main_window.names_window:
            self.main_window.names_window.pop('SetFigWindow_Vth')
        self.deleteLater()
