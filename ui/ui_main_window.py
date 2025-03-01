# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDoubleSpinBox,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QToolBox, QVBoxLayout, QWidget)
import ui.apprcc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1266, 882)
        icon = QIcon()
        icon.addFile(u":/APThrehold_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionSave_datas = QAction(MainWindow)
        self.actionSave_datas.setObjectName(u"actionSave_datas")
        icon1 = QIcon()
        icon1.addFile(u":/\u65b0\u524d\u7f00/save_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_datas.setIcon(icon1)
        self.actionode_option = QAction(MainWindow)
        self.actionode_option.setObjectName(u"actionode_option")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_centralwidget = QGridLayout(self.centralwidget)
        self.gridLayout_centralwidget.setObjectName(u"gridLayout_centralwidget")
        self.gridLayout_centralwidget.setContentsMargins(0, 2, 0, 0)
        self.tabWidget_main = QTabWidget(self.centralwidget)
        self.tabWidget_main.setObjectName(u"tabWidget_main")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_main.sizePolicy().hasHeightForWidth())
        self.tabWidget_main.setSizePolicy(sizePolicy)
        self.tabWidget_main.setMinimumSize(QSize(500, 500))
        self.tabWidget_main.setStyleSheet(u"QTabWidget#tabWidget_main::tab-bar {\n"
"    alignment: left; /* \u5c06 Tab \u6807\u7b7e\u5bf9\u9f50\u5230\u5de6\u8fb9 */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: white; /* \u672a\u9009\u4e2d\u7684\u6807\u7b7e\u80cc\u666f\u989c\u8272\u4e3a\u767d\u8272 */\n"
"    height: 28px;\n"
"	/*font-family:Times New Roman ;*/\n"
"	font-weight: bold;\n"
"	/*font-size:15px;*/\n"
"    min-width: 145px;\n"
"    margin-right: 5px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u9009\u4e2d\u7684\u6807\u7b7e\u80cc\u666f\u989c\u8272\u4e3a lightblue */\n"
"QTabBar::tab:selected {\n"
"    background-color: lightblue; /* \u9009\u4e2d\u7684\u6807\u7b7e\u80cc\u666f\u989c\u8272\u4e3a lightblue */\n"
"    color: black; /* \u9009\u4e2d\u7684\u6807\u7b7e\u6587\u5b57\u989c\u8272\u4e3a\u9ed1\u8272\uff08\u53ef\u9009\uff09 */\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u672a\u9009\u4e2d\u7684\u6807\u7b7e\u80cc\u666f\u989c\u8272\u4e3a\u767d\u8272 */\n"
"QTabBar::tab:!selected {\n"
"    background-color:"
                        " white; /* \u672a\u9009\u4e2d\u7684\u6807\u7b7e\u80cc\u666f\u989c\u8272\u4e3a\u767d\u8272 */\n"
"    color: black; /* \u672a\u9009\u4e2d\u7684\u6807\u7b7e\u6587\u5b57\u989c\u8272\u4e3a\u9ed1\u8272\uff08\u53ef\u9009\uff09 */\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 2px solid #829aa0; /* \u8bbe\u7f6e2px\u7684\u8fb9\u6846\u989c\u8272 */\n"
"    border-radius: 5px;        /* \u8bbe\u7f6e\u5706\u89d2 */\n"
"    margin-top: 10px;          /* \u6807\u9898\u4e0e\u5185\u5bb9\u7684\u8ddd\u79bb */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;  /* \u6807\u9898\u7684\u6765\u6e90 */\n"
"    subcontrol-position: top left; /* \u6807\u9898\u4f4d\u7f6e */\n"
"    padding: 0 3px;  /* \u4e3a\u6807\u9898\u6dfb\u52a0\u5de6\u53f3\u5185\u8fb9\u8ddd */\n"
" \n"
"    color: black;             /* \u6807\u9898\u7684\u6587\u5b57\u989c\u8272 */\n"
"    font-weight: bold;          /* \u6807\u9898\u7684\u52a0\u7c97 */\n"
"}\n"
"\n"
"")
        self.tabWidget_main.setTabPosition(QTabWidget.North)
        self.tabWidget_main.setTabShape(QTabWidget.Rounded)
        self.tabWidget_main.setUsesScrollButtons(False)
        self.tab_aquire_ap = QWidget()
        self.tab_aquire_ap.setObjectName(u"tab_aquire_ap")
        self.gridLayout_6 = QGridLayout(self.tab_aquire_ap)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(9, 9, 9, 9)
        self.toolBox_aquire_ap = QToolBox(self.tab_aquire_ap)
        self.toolBox_aquire_ap.setObjectName(u"toolBox_aquire_ap")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolBox_aquire_ap.sizePolicy().hasHeightForWidth())
        self.toolBox_aquire_ap.setSizePolicy(sizePolicy1)
        self.toolBox_aquire_ap.setMinimumSize(QSize(300, 0))
        self.toolBox_aquire_ap.setStyleSheet(u"QToolBoxButton {min-height: 25px;}\n"
"QToolBox::tab {\n"
"    background-color: #414656;  /* Tab background color */\n"
"    color: white;  /* Tab text color */\n"
"    font-size: 12px;  /* Adjust font size */\n"
"    padding: 5px;  /* Padding around the text */\n"
"    height: 40px;  /* Set the minimum height of the tab */\n"
"	\n"
"}\n"
"")
        self.page_simulation = QWidget()
        self.page_simulation.setObjectName(u"page_simulation")
        self.page_simulation.setGeometry(QRect(0, 0, 300, 747))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.page_simulation.sizePolicy().hasHeightForWidth())
        self.page_simulation.setSizePolicy(sizePolicy2)
        self.gridLayout_12 = QGridLayout(self.page_simulation)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_simulation = QWidget(self.page_simulation)
        self.horizontalWidget_simulation.setObjectName(u"horizontalWidget_simulation")
        self.horizontalLayout_horizontalWidget_simulation = QHBoxLayout(self.horizontalWidget_simulation)
        self.horizontalLayout_horizontalWidget_simulation.setSpacing(0)
        self.horizontalLayout_horizontalWidget_simulation.setObjectName(u"horizontalLayout_horizontalWidget_simulation")
        self.horizontalLayout_horizontalWidget_simulation.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_horizontalWidget_simulation.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_model = QVBoxLayout()
        self.verticalLayout_model.setObjectName(u"verticalLayout_model")
        self.verticalLayout_model.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.groupBox_neuron_model = QGroupBox(self.horizontalWidget_simulation)
        self.groupBox_neuron_model.setObjectName(u"groupBox_neuron_model")
        self.gridLayout_4 = QGridLayout(self.groupBox_neuron_model)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_neuron_model)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.comboBox_model = QComboBox(self.groupBox_neuron_model)
        self.comboBox_model.setObjectName(u"comboBox_model")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_model.sizePolicy().hasHeightForWidth())
        self.comboBox_model.setSizePolicy(sizePolicy3)
        self.comboBox_model.setMinimumSize(QSize(85, 0))
        self.comboBox_model.setEditable(True)

        self.horizontalLayout_2.addWidget(self.comboBox_model)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_model.addWidget(self.groupBox_neuron_model)

        self.groupBox_input = QGroupBox(self.horizontalWidget_simulation)
        self.groupBox_input.setObjectName(u"groupBox_input")
        self.groupBox_input.setStyleSheet(u"")
        self.verticalLayout_input = QVBoxLayout(self.groupBox_input)
        self.verticalLayout_input.setObjectName(u"verticalLayout_input")
        self.horizontalLayout_add_stimulus = QHBoxLayout()
        self.horizontalLayout_add_stimulus.setObjectName(u"horizontalLayout_add_stimulus")
        self.label_add_stimulus = QLabel(self.groupBox_input)
        self.label_add_stimulus.setObjectName(u"label_add_stimulus")

        self.horizontalLayout_add_stimulus.addWidget(self.label_add_stimulus)

        self.pushButton_add_stim = QPushButton(self.groupBox_input)
        self.pushButton_add_stim.setObjectName(u"pushButton_add_stim")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_add_stim.sizePolicy().hasHeightForWidth())
        self.pushButton_add_stim.setSizePolicy(sizePolicy4)
        self.pushButton_add_stim.setMinimumSize(QSize(40, 0))
        self.pushButton_add_stim.setMaximumSize(QSize(23, 23))
        self.pushButton_add_stim.setMouseTracking(True)

        self.horizontalLayout_add_stimulus.addWidget(self.pushButton_add_stim)


        self.verticalLayout_input.addLayout(self.horizontalLayout_add_stimulus)

        self.tabWidget_stimulus = QTabWidget(self.groupBox_input)
        self.tabWidget_stimulus.setObjectName(u"tabWidget_stimulus")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tabWidget_stimulus.sizePolicy().hasHeightForWidth())
        self.tabWidget_stimulus.setSizePolicy(sizePolicy5)
        self.tabWidget_stimulus.setStyleSheet(u"QTabBar::tab {\n"
"  background-color: #ffffff; /* \u4f7f\u7528\u5341\u516d\u8fdb\u5236\u989c\u8272\u7801\u8bbe\u7f6e\u80cc\u666f\u989c\u8272 */\n"
"font-weight: ;\n"
"}\n"
"QTabBar::tab {height: 23px;min-width: 0px;margin-right: 5px;padding-left: 5px;padding-right: 5px;font-weight:normal ;}")
        self.tab_stim1 = QWidget()
        self.tab_stim1.setObjectName(u"tab_stim1")
        self.gridLayout_tab_stim1 = QGridLayout(self.tab_stim1)
        self.gridLayout_tab_stim1.setObjectName(u"gridLayout_tab_stim1")
        self.gridLayout_tab_stim1.setContentsMargins(9, 9, 9, 0)
        self.tabWidget_stimulus.addTab(self.tab_stim1, "")

        self.verticalLayout_input.addWidget(self.tabWidget_stimulus)


        self.verticalLayout_model.addWidget(self.groupBox_input)

        self.horizontalLayout_Input = QHBoxLayout()
        self.horizontalLayout_Input.setObjectName(u"horizontalLayout_Input")

        self.verticalLayout_model.addLayout(self.horizontalLayout_Input)

        self.groupBox_solving_ode = QGroupBox(self.horizontalWidget_simulation)
        self.groupBox_solving_ode.setObjectName(u"groupBox_solving_ode")
        self.gridLayout_8 = QGridLayout(self.groupBox_solving_ode)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_dt = QHBoxLayout()
        self.horizontalLayout_dt.setObjectName(u"horizontalLayout_dt")
        self.label_dt = QLabel(self.groupBox_solving_ode)
        self.label_dt.setObjectName(u"label_dt")

        self.horizontalLayout_dt.addWidget(self.label_dt)

        self.doubleSpinBox_dt = QDoubleSpinBox(self.groupBox_solving_ode)
        self.doubleSpinBox_dt.setObjectName(u"doubleSpinBox_dt")
        self.doubleSpinBox_dt.setDecimals(3)
        self.doubleSpinBox_dt.setValue(0.001000000000000)

        self.horizontalLayout_dt.addWidget(self.doubleSpinBox_dt)


        self.gridLayout_8.addLayout(self.horizontalLayout_dt, 2, 0, 1, 1)

        self.horizontalLayout_ode_option = QHBoxLayout()
        self.horizontalLayout_ode_option.setObjectName(u"horizontalLayout_ode_option")
        self.label_ode_option = QLabel(self.groupBox_solving_ode)
        self.label_ode_option.setObjectName(u"label_ode_option")

        self.horizontalLayout_ode_option.addWidget(self.label_ode_option)

        self.comboBox_ode_option = QComboBox(self.groupBox_solving_ode)
        self.comboBox_ode_option.addItem("")
        self.comboBox_ode_option.addItem("")
        self.comboBox_ode_option.addItem("")
        self.comboBox_ode_option.setObjectName(u"comboBox_ode_option")

        self.horizontalLayout_ode_option.addWidget(self.comboBox_ode_option)


        self.gridLayout_8.addLayout(self.horizontalLayout_ode_option, 1, 0, 1, 1)

        self.horizontalLayout_timeline = QHBoxLayout()
        self.horizontalLayout_timeline.setObjectName(u"horizontalLayout_timeline")
        self.label_timeline = QLabel(self.groupBox_solving_ode)
        self.label_timeline.setObjectName(u"label_timeline")

        self.horizontalLayout_timeline.addWidget(self.label_timeline)

        self.spinBox_timeline = QSpinBox(self.groupBox_solving_ode)
        self.spinBox_timeline.setObjectName(u"spinBox_timeline")
        self.spinBox_timeline.setMaximum(1000000000)
        self.spinBox_timeline.setValue(200)

        self.horizontalLayout_timeline.addWidget(self.spinBox_timeline)


        self.gridLayout_8.addLayout(self.horizontalLayout_timeline, 0, 0, 1, 1)

        self.pushButton_simulation_run = QPushButton(self.groupBox_solving_ode)
        self.pushButton_simulation_run.setObjectName(u"pushButton_simulation_run")

        self.gridLayout_8.addWidget(self.pushButton_simulation_run, 3, 0, 1, 1)


        self.verticalLayout_model.addWidget(self.groupBox_solving_ode)


        self.horizontalLayout_horizontalWidget_simulation.addLayout(self.verticalLayout_model)


        self.gridLayout_12.addWidget(self.horizontalWidget_simulation, 0, 0, 1, 1)

        self.toolBox_aquire_ap.addItem(self.page_simulation, u"Model simulation")
        self.page_experimental = QWidget()
        self.page_experimental.setObjectName(u"page_experimental")
        self.page_experimental.setGeometry(QRect(0, 0, 300, 747))
        self.gridLayout_5 = QGridLayout(self.page_experimental)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_physiological_datas = QGridLayout()
        self.gridLayout_physiological_datas.setObjectName(u"gridLayout_physiological_datas")

        self.gridLayout_5.addLayout(self.gridLayout_physiological_datas, 0, 0, 1, 1)

        self.toolBox_aquire_ap.addItem(self.page_experimental, u"Experimental recording ")

        self.gridLayout_6.addWidget(self.toolBox_aquire_ap, 0, 0, 1, 1)

        self.widget_plot_AP_main = QWidget(self.tab_aquire_ap)
        self.widget_plot_AP_main.setObjectName(u"widget_plot_AP_main")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_plot_AP_main.sizePolicy().hasHeightForWidth())
        self.widget_plot_AP_main.setSizePolicy(sizePolicy6)
        self.widget_plot_AP_main.setMinimumSize(QSize(550, 0))
        self.gridLayout = QGridLayout(self.widget_plot_AP_main)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_AP_fig = QGridLayout()
        self.gridLayout_AP_fig.setObjectName(u"gridLayout_AP_fig")
        self.gridLayout_AP_fig.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_AP_fig.setHorizontalSpacing(6)
        self.gridLayout_AP_fig.setContentsMargins(0, 0, 0, 0)
        self.groupBox_extarct_aps = QGroupBox(self.widget_plot_AP_main)
        self.groupBox_extarct_aps.setObjectName(u"groupBox_extarct_aps")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(20)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.groupBox_extarct_aps.sizePolicy().hasHeightForWidth())
        self.groupBox_extarct_aps.setSizePolicy(sizePolicy7)
        self.horizontalLayout_ = QHBoxLayout(self.groupBox_extarct_aps)
        self.horizontalLayout_.setObjectName(u"horizontalLayout_")
        self.horizontalLayout_.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_aps_pushbutton = QVBoxLayout()
        self.verticalLayout_aps_pushbutton.setSpacing(0)
        self.verticalLayout_aps_pushbutton.setObjectName(u"verticalLayout_aps_pushbutton")
        self.pushButton_add_ap = QPushButton(self.groupBox_extarct_aps)
        self.pushButton_add_ap.setObjectName(u"pushButton_add_ap")
        sizePolicy4.setHeightForWidth(self.pushButton_add_ap.sizePolicy().hasHeightForWidth())
        self.pushButton_add_ap.setSizePolicy(sizePolicy4)
        self.pushButton_add_ap.setMinimumSize(QSize(40, 0))
        self.pushButton_add_ap.setMaximumSize(QSize(23, 23))
        self.pushButton_add_ap.setMouseTracking(True)
        self.pushButton_add_ap.setFocusPolicy(Qt.NoFocus)
        self.pushButton_add_ap.setCheckable(False)

        self.verticalLayout_aps_pushbutton.addWidget(self.pushButton_add_ap)

        self.pushButton_subtract_ap = QPushButton(self.groupBox_extarct_aps)
        self.pushButton_subtract_ap.setObjectName(u"pushButton_subtract_ap")
        sizePolicy4.setHeightForWidth(self.pushButton_subtract_ap.sizePolicy().hasHeightForWidth())
        self.pushButton_subtract_ap.setSizePolicy(sizePolicy4)
        self.pushButton_subtract_ap.setMinimumSize(QSize(40, 0))
        self.pushButton_subtract_ap.setMaximumSize(QSize(23, 23))
        self.pushButton_subtract_ap.setMouseTracking(True)
        self.pushButton_subtract_ap.setCheckable(True)
        self.pushButton_subtract_ap.setChecked(False)
        self.pushButton_subtract_ap.setAutoExclusive(False)

        self.verticalLayout_aps_pushbutton.addWidget(self.pushButton_subtract_ap)


        self.horizontalLayout_.addLayout(self.verticalLayout_aps_pushbutton)

        self.scrollArea_extract_aps = QScrollArea(self.groupBox_extarct_aps)
        self.scrollArea_extract_aps.setObjectName(u"scrollArea_extract_aps")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.scrollArea_extract_aps.sizePolicy().hasHeightForWidth())
        self.scrollArea_extract_aps.setSizePolicy(sizePolicy8)
        self.scrollArea_extract_aps.setMaximumSize(QSize(16777215, 50))
        self.scrollArea_extract_aps.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_extract_aps.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_extract_aps.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_extract_aps.setWidgetResizable(True)
        self.scrollAreaWidgetContents_aps = QWidget()
        self.scrollAreaWidgetContents_aps.setObjectName(u"scrollAreaWidgetContents_aps")
        self.scrollAreaWidgetContents_aps.setGeometry(QRect(0, 0, 739, 48))
        self.horizontalLayout_aps = QHBoxLayout(self.scrollAreaWidgetContents_aps)
        self.horizontalLayout_aps.setObjectName(u"horizontalLayout_aps")
        self.horizontalLayout_aps.setContentsMargins(0, 0, 0, 0)
        self.comboBox_voltage_option = QComboBox(self.scrollAreaWidgetContents_aps)
        self.comboBox_voltage_option.setObjectName(u"comboBox_voltage_option")

        self.horizontalLayout_aps.addWidget(self.comboBox_voltage_option)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_aps.addItem(self.horizontalSpacer)

        self.scrollArea_extract_aps.setWidget(self.scrollAreaWidgetContents_aps)

        self.horizontalLayout_.addWidget(self.scrollArea_extract_aps)


        self.gridLayout_AP_fig.addWidget(self.groupBox_extarct_aps, 0, 3, 1, 1)

        self.groupBox_set_axes_AP = QGroupBox(self.widget_plot_AP_main)
        self.groupBox_set_axes_AP.setObjectName(u"groupBox_set_axes_AP")
        sizePolicy2.setHeightForWidth(self.groupBox_set_axes_AP.sizePolicy().hasHeightForWidth())
        self.groupBox_set_axes_AP.setSizePolicy(sizePolicy2)
        self.groupBox_set_axes_AP.setMaximumSize(QSize(65, 16777215))
        self.gridLayout_9 = QGridLayout(self.groupBox_set_axes_AP)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(4, 2, 4, 2)
        self.pushButton_setplot_AP = QPushButton(self.groupBox_set_axes_AP)
        self.pushButton_setplot_AP.setObjectName(u"pushButton_setplot_AP")
        sizePolicy4.setHeightForWidth(self.pushButton_setplot_AP.sizePolicy().hasHeightForWidth())
        self.pushButton_setplot_AP.setSizePolicy(sizePolicy4)
        self.pushButton_setplot_AP.setMinimumSize(QSize(0, 0))
        self.pushButton_setplot_AP.setMaximumSize(QSize(16777215, 32))
        icon2 = QIcon()
        icon2.addFile(u":/set_setting_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_setplot_AP.setIcon(icon2)
        self.pushButton_setplot_AP.setIconSize(QSize(20, 20))

        self.gridLayout_9.addWidget(self.pushButton_setplot_AP, 0, 0, 1, 1)


        self.gridLayout_AP_fig.addWidget(self.groupBox_set_axes_AP, 0, 1, 1, 1)

        self.GroupBox_export_results_2 = QGroupBox(self.widget_plot_AP_main)
        self.GroupBox_export_results_2.setObjectName(u"GroupBox_export_results_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(1)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.GroupBox_export_results_2.sizePolicy().hasHeightForWidth())
        self.GroupBox_export_results_2.setSizePolicy(sizePolicy9)
        self.GroupBox_export_results_2.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_14 = QGridLayout(self.GroupBox_export_results_2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.pushButton_save_data_APs = QPushButton(self.GroupBox_export_results_2)
        self.pushButton_save_data_APs.setObjectName(u"pushButton_save_data_APs")
        sizePolicy4.setHeightForWidth(self.pushButton_save_data_APs.sizePolicy().hasHeightForWidth())
        self.pushButton_save_data_APs.setSizePolicy(sizePolicy4)
        self.pushButton_save_data_APs.setMinimumSize(QSize(0, 0))
        self.pushButton_save_data_APs.setMaximumSize(QSize(40, 32))
        icon3 = QIcon()
        icon3.addFile(u":/8678769_save_fill_data_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save_data_APs.setIcon(icon3)
        self.pushButton_save_data_APs.setIconSize(QSize(24, 24))

        self.gridLayout_14.addWidget(self.pushButton_save_data_APs, 0, 0, 1, 1)


        self.gridLayout_AP_fig.addWidget(self.GroupBox_export_results_2, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_AP_fig, 0, 0, 1, 1)

        self.widget_fig_AP = QWidget(self.widget_plot_AP_main)
        self.widget_fig_AP.setObjectName(u"widget_fig_AP")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.widget_fig_AP.sizePolicy().hasHeightForWidth())
        self.widget_fig_AP.setSizePolicy(sizePolicy10)
        self.widget_fig_AP.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.widget_fig_AP, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_plot_AP_main, 0, 1, 1, 1)

        self.tabWidget_main.addTab(self.tab_aquire_ap, "")
        self.tab_Vth = QWidget()
        self.tab_Vth.setObjectName(u"tab_Vth")
        self.gridLayout_11 = QGridLayout(self.tab_Vth)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.toolBox_calculate_spike_threshold = QToolBox(self.tab_Vth)
        self.toolBox_calculate_spike_threshold.setObjectName(u"toolBox_calculate_spike_threshold")
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.toolBox_calculate_spike_threshold.sizePolicy().hasHeightForWidth())
        self.toolBox_calculate_spike_threshold.setSizePolicy(sizePolicy11)
        self.toolBox_calculate_spike_threshold.setMinimumSize(QSize(300, 0))
        self.toolBox_calculate_spike_threshold.setMaximumSize(QSize(300, 16777215))
        self.toolBox_calculate_spike_threshold.setStyleSheet(u"QToolBoxButton {min-height: 25px;}\n"
"QToolBox::tab {\n"
"        background-color: #414656;  /* Tab background color */\n"
"        color: white;  /* Tab text color */\n"
"        font-size: ;  /* Font size */\n"
"        font-weight: ;  /* Bold font */\n"
"        padding: 5px;  /* Padding around the text */\n"
"    }\n"
"    ")
        self.page_method_curvature = QWidget()
        self.page_method_curvature.setObjectName(u"page_method_curvature")
        self.page_method_curvature.setGeometry(QRect(0, 0, 300, 747))
        sizePolicy11.setHeightForWidth(self.page_method_curvature.sizePolicy().hasHeightForWidth())
        self.page_method_curvature.setSizePolicy(sizePolicy11)
        self.page_method_curvature.setMinimumSize(QSize(300, 0))
        self.page_method_curvature.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.page_method_curvature)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_settings_curvature_method = QGroupBox(self.page_method_curvature)
        self.groupBox_settings_curvature_method.setObjectName(u"groupBox_settings_curvature_method")
        self.gridLayout_settings_curvature_method = QGridLayout(self.groupBox_settings_curvature_method)
        self.gridLayout_settings_curvature_method.setObjectName(u"gridLayout_settings_curvature_method")
        self.label_method_curvature = QLabel(self.groupBox_settings_curvature_method)
        self.label_method_curvature.setObjectName(u"label_method_curvature")

        self.gridLayout_settings_curvature_method.addWidget(self.label_method_curvature, 0, 0, 1, 1)

        self.label_kth_curvature = QLabel(self.groupBox_settings_curvature_method)
        self.label_kth_curvature.setObjectName(u"label_kth_curvature")

        self.gridLayout_settings_curvature_method.addWidget(self.label_kth_curvature, 1, 0, 1, 1)

        self.doubleSpinBox_kth_curvature = QDoubleSpinBox(self.groupBox_settings_curvature_method)
        self.doubleSpinBox_kth_curvature.setObjectName(u"doubleSpinBox_kth_curvature")
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_kth_curvature.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_kth_curvature.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_kth_curvature.setValue(20.000000000000000)

        self.gridLayout_settings_curvature_method.addWidget(self.doubleSpinBox_kth_curvature, 1, 1, 1, 1)

        self.comboBox_method_curvature = QComboBox(self.groupBox_settings_curvature_method)
        self.comboBox_method_curvature.addItem("")
        self.comboBox_method_curvature.addItem("")
        self.comboBox_method_curvature.addItem("")
        self.comboBox_method_curvature.addItem("")
        self.comboBox_method_curvature.addItem("")
        self.comboBox_method_curvature.setObjectName(u"comboBox_method_curvature")
        sizePolicy3.setHeightForWidth(self.comboBox_method_curvature.sizePolicy().hasHeightForWidth())
        self.comboBox_method_curvature.setSizePolicy(sizePolicy3)
        self.comboBox_method_curvature.setMinimumSize(QSize(0, 0))
        self.comboBox_method_curvature.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_settings_curvature_method.addWidget(self.comboBox_method_curvature, 0, 1, 1, 1)

        self.pushButton_run_curvature = QPushButton(self.groupBox_settings_curvature_method)
        self.pushButton_run_curvature.setObjectName(u"pushButton_run_curvature")

        self.gridLayout_settings_curvature_method.addWidget(self.pushButton_run_curvature, 2, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox_settings_curvature_method, 0, 0, 1, 1)

        self.Features = QGroupBox(self.page_method_curvature)
        self.Features.setObjectName(u"Features")
        self.gridLayout_Features_main = QGridLayout(self.Features)
        self.gridLayout_Features_main.setSpacing(6)
        self.gridLayout_Features_main.setObjectName(u"gridLayout_Features_main")
        self.gridLayout_Features_main.setContentsMargins(0, 9, 0, 0)
        self.tableWidget_features = QTableWidget(self.Features)
        self.tableWidget_features.setObjectName(u"tableWidget_features")

        self.gridLayout_Features_main.addWidget(self.tableWidget_features, 1, 0, 1, 1)

        self.pushButton_set_parameters_features = QPushButton(self.Features)
        self.pushButton_set_parameters_features.setObjectName(u"pushButton_set_parameters_features")
        icon4 = QIcon()
        icon4.addFile(u":/set1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_set_parameters_features.setIcon(icon4)

        self.gridLayout_Features_main.addWidget(self.pushButton_set_parameters_features, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.Features, 2, 0, 1, 2)

        self.toolBox_calculate_spike_threshold.addItem(self.page_method_curvature, u"Waveform curvature-based method")
        self.page_method_ramp = QWidget()
        self.page_method_ramp.setObjectName(u"page_method_ramp")
        self.page_method_ramp.setGeometry(QRect(0, 0, 300, 747))
        self.toolBox_calculate_spike_threshold.addItem(self.page_method_ramp, u"Ramp stimulation-based method")

        self.gridLayout_11.addWidget(self.toolBox_calculate_spike_threshold, 0, 0, 1, 1)

        self.widget_plot_Vth = QWidget(self.tab_Vth)
        self.widget_plot_Vth.setObjectName(u"widget_plot_Vth")
        sizePolicy2.setHeightForWidth(self.widget_plot_Vth.sizePolicy().hasHeightForWidth())
        self.widget_plot_Vth.setSizePolicy(sizePolicy2)
        self.widget_plot_Vth.setMinimumSize(QSize(0, 0))
        self.gridLayout_13 = QGridLayout(self.widget_plot_Vth)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.groupBox_set_axes_Vth = QGroupBox(self.widget_plot_Vth)
        self.groupBox_set_axes_Vth.setObjectName(u"groupBox_set_axes_Vth")
        sizePolicy9.setHeightForWidth(self.groupBox_set_axes_Vth.sizePolicy().hasHeightForWidth())
        self.groupBox_set_axes_Vth.setSizePolicy(sizePolicy9)
        self.groupBox_set_axes_Vth.setMinimumSize(QSize(56, 68))
        self.groupBox_set_axes_Vth.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_10 = QGridLayout(self.groupBox_set_axes_Vth)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(4, 2, 4, 2)
        self.pushButton_setplot_Vth = QPushButton(self.groupBox_set_axes_Vth)
        self.pushButton_setplot_Vth.setObjectName(u"pushButton_setplot_Vth")
        sizePolicy4.setHeightForWidth(self.pushButton_setplot_Vth.sizePolicy().hasHeightForWidth())
        self.pushButton_setplot_Vth.setSizePolicy(sizePolicy4)
        self.pushButton_setplot_Vth.setMinimumSize(QSize(44, 32))
        self.pushButton_setplot_Vth.setMaximumSize(QSize(40, 32))
        self.pushButton_setplot_Vth.setIcon(icon2)
        self.pushButton_setplot_Vth.setIconSize(QSize(20, 20))

        self.gridLayout_10.addWidget(self.pushButton_setplot_Vth, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_set_axes_Vth)

        self.GroupBox_export_results = QGroupBox(self.widget_plot_Vth)
        self.GroupBox_export_results.setObjectName(u"GroupBox_export_results")
        sizePolicy9.setHeightForWidth(self.GroupBox_export_results.sizePolicy().hasHeightForWidth())
        self.GroupBox_export_results.setSizePolicy(sizePolicy9)
        self.GroupBox_export_results.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_3 = QGridLayout(self.GroupBox_export_results)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_save_data_Vth = QPushButton(self.GroupBox_export_results)
        self.pushButton_save_data_Vth.setObjectName(u"pushButton_save_data_Vth")
        sizePolicy4.setHeightForWidth(self.pushButton_save_data_Vth.sizePolicy().hasHeightForWidth())
        self.pushButton_save_data_Vth.setSizePolicy(sizePolicy4)
        self.pushButton_save_data_Vth.setMinimumSize(QSize(0, 0))
        self.pushButton_save_data_Vth.setMaximumSize(QSize(40, 32))
        self.pushButton_save_data_Vth.setIcon(icon3)
        self.pushButton_save_data_Vth.setIconSize(QSize(24, 24))

        self.gridLayout_3.addWidget(self.pushButton_save_data_Vth, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.GroupBox_export_results)

        self.groupBox_Vth = QGroupBox(self.widget_plot_Vth)
        self.groupBox_Vth.setObjectName(u"groupBox_Vth")
        sizePolicy7.setHeightForWidth(self.groupBox_Vth.sizePolicy().hasHeightForWidth())
        self.groupBox_Vth.setSizePolicy(sizePolicy7)
        self.gridLayout_Vth = QGridLayout(self.groupBox_Vth)
        self.gridLayout_Vth.setObjectName(u"gridLayout_Vth")
        self.gridLayout_Vth.setVerticalSpacing(2)
        self.gridLayout_Vth.setContentsMargins(-1, 2, -1, 2)
        self.lineEdit_minimum_Vth = QLineEdit(self.groupBox_Vth)
        self.lineEdit_minimum_Vth.setObjectName(u"lineEdit_minimum_Vth")
        self.lineEdit_minimum_Vth.setReadOnly(True)

        self.gridLayout_Vth.addWidget(self.lineEdit_minimum_Vth, 0, 1, 1, 1)

        self.lineEdit_mean_Vth = QLineEdit(self.groupBox_Vth)
        self.lineEdit_mean_Vth.setObjectName(u"lineEdit_mean_Vth")
        self.lineEdit_mean_Vth.setReadOnly(True)

        self.gridLayout_Vth.addWidget(self.lineEdit_mean_Vth, 0, 5, 1, 1)

        self.label_SD_Vth = QLabel(self.groupBox_Vth)
        self.label_SD_Vth.setObjectName(u"label_SD_Vth")

        self.gridLayout_Vth.addWidget(self.label_SD_Vth, 0, 6, 1, 1)

        self.label_minimum_Vth = QLabel(self.groupBox_Vth)
        self.label_minimum_Vth.setObjectName(u"label_minimum_Vth")

        self.gridLayout_Vth.addWidget(self.label_minimum_Vth, 0, 0, 1, 1)

        self.label_mean_Vth = QLabel(self.groupBox_Vth)
        self.label_mean_Vth.setObjectName(u"label_mean_Vth")

        self.gridLayout_Vth.addWidget(self.label_mean_Vth, 0, 4, 1, 1)

        self.lineEdit_maximum_Vth = QLineEdit(self.groupBox_Vth)
        self.lineEdit_maximum_Vth.setObjectName(u"lineEdit_maximum_Vth")
        self.lineEdit_maximum_Vth.setReadOnly(True)

        self.gridLayout_Vth.addWidget(self.lineEdit_maximum_Vth, 0, 3, 1, 1)

        self.lineEdit_SD_Vth = QLineEdit(self.groupBox_Vth)
        self.lineEdit_SD_Vth.setObjectName(u"lineEdit_SD_Vth")
        self.lineEdit_SD_Vth.setReadOnly(True)

        self.gridLayout_Vth.addWidget(self.lineEdit_SD_Vth, 0, 7, 1, 1)

        self.label_maximum_Vth = QLabel(self.groupBox_Vth)
        self.label_maximum_Vth.setObjectName(u"label_maximum_Vth")

        self.gridLayout_Vth.addWidget(self.label_maximum_Vth, 0, 2, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_Vth)


        self.gridLayout_13.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.widget_fig_Vth = QWidget(self.widget_plot_Vth)
        self.widget_fig_Vth.setObjectName(u"widget_fig_Vth")
        sizePolicy10.setHeightForWidth(self.widget_fig_Vth.sizePolicy().hasHeightForWidth())
        self.widget_fig_Vth.setSizePolicy(sizePolicy10)

        self.gridLayout_13.addWidget(self.widget_fig_Vth, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.widget_plot_Vth, 0, 1, 1, 1)

        self.tabWidget_main.addTab(self.tab_Vth, "")

        self.gridLayout_centralwidget.addWidget(self.tabWidget_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget_main.setCurrentIndex(0)
        self.toolBox_aquire_ap.setCurrentIndex(0)
        self.tabWidget_stimulus.setCurrentIndex(0)
        self.toolBox_calculate_spike_threshold.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"APThreshold", None))
        self.actionSave_datas.setText(QCoreApplication.translate("MainWindow", u"Save data", None))
        self.actionode_option.setText(QCoreApplication.translate("MainWindow", u"ode_option", None))
        self.groupBox_neuron_model.setTitle(QCoreApplication.translate("MainWindow", u"Biophysical model", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Name</p></body></html>", None))
        self.groupBox_input.setTitle(QCoreApplication.translate("MainWindow", u"Stimulation", None))
        self.label_add_stimulus.setText(QCoreApplication.translate("MainWindow", u"Add stimulus", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_add_stim.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u523a\u6fc0\u7535\u6d41", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_add_stim.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(tooltip)
        self.tabWidget_stimulus.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.tabWidget_stimulus.setTabText(self.tabWidget_stimulus.indexOf(self.tab_stim1), QCoreApplication.translate("MainWindow", u"stim1", None))
        self.groupBox_solving_ode.setTitle(QCoreApplication.translate("MainWindow", u"Simulation control", None))
        self.label_dt.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>dt (ms)</p></body></html>", None))
        self.label_ode_option.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>ODE solver</p></body></html>", None))
        self.comboBox_ode_option.setItemText(0, QCoreApplication.translate("MainWindow", u"Odeint", None))
        self.comboBox_ode_option.setItemText(1, QCoreApplication.translate("MainWindow", u"Euler", None))
        self.comboBox_ode_option.setItemText(2, QCoreApplication.translate("MainWindow", u"Runge-Kutta 45", None))

        self.label_timeline.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Duration (ms)</p></body></html>", None))
        self.pushButton_simulation_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
#if QT_CONFIG(shortcut)
        self.pushButton_simulation_run.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Return", None))
#endif // QT_CONFIG(shortcut)
        self.toolBox_aquire_ap.setItemText(self.toolBox_aquire_ap.indexOf(self.page_simulation), QCoreApplication.translate("MainWindow", u"Model simulation", None))
        self.toolBox_aquire_ap.setItemText(self.toolBox_aquire_ap.indexOf(self.page_experimental), QCoreApplication.translate("MainWindow", u"Experimental recording ", None))
        self.groupBox_extarct_aps.setTitle(QCoreApplication.translate("MainWindow", u"Extract APs", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_add_ap.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u523a\u6fc0\u7535\u6d41", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_add_ap.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_subtract_ap.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u523a\u6fc0\u7535\u6d41", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_subtract_ap.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.groupBox_set_axes_AP.setTitle(QCoreApplication.translate("MainWindow", u"Set axes", None))
        self.pushButton_setplot_AP.setText("")
        self.GroupBox_export_results_2.setTitle(QCoreApplication.translate("MainWindow", u"Save data", None))
        self.pushButton_save_data_APs.setText("")
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_aquire_ap), QCoreApplication.translate("MainWindow", u"Action Potential", None))
#if QT_CONFIG(tooltip)
        self.page_method_curvature.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.page_method_curvature.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.page_method_curvature.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.groupBox_settings_curvature_method.setTitle(QCoreApplication.translate("MainWindow", u"Vth estimation", None))
#if QT_CONFIG(tooltip)
        self.label_method_curvature.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#67d1ff;\">Method to calculate the spike threshold</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_method_curvature.setText(QCoreApplication.translate("MainWindow", u"Option", None))
        self.label_kth_curvature.setText(QCoreApplication.translate("MainWindow", u"Kth", None))
        self.comboBox_method_curvature.setItemText(0, QCoreApplication.translate("MainWindow", u"First derivative method", None))
        self.comboBox_method_curvature.setItemText(1, QCoreApplication.translate("MainWindow", u"Second derivative method", None))
        self.comboBox_method_curvature.setItemText(2, QCoreApplication.translate("MainWindow", u"Third derivative method", None))
        self.comboBox_method_curvature.setItemText(3, QCoreApplication.translate("MainWindow", u"Maximum slope method on phase Space", None))
        self.comboBox_method_curvature.setItemText(4, QCoreApplication.translate("MainWindow", u"Maximum second derivative method on phase space", None))

        self.pushButton_run_curvature.setText(QCoreApplication.translate("MainWindow", u"Run", None))
#if QT_CONFIG(shortcut)
        self.pushButton_run_curvature.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Return", None))
#endif // QT_CONFIG(shortcut)
        self.Features.setTitle(QCoreApplication.translate("MainWindow", u"Feature calculation", None))
        self.pushButton_set_parameters_features.setText(QCoreApplication.translate("MainWindow", u"Set parameters", None))
        self.toolBox_calculate_spike_threshold.setItemText(self.toolBox_calculate_spike_threshold.indexOf(self.page_method_curvature), QCoreApplication.translate("MainWindow", u"Waveform curvature-based method", None))
        self.toolBox_calculate_spike_threshold.setItemText(self.toolBox_calculate_spike_threshold.indexOf(self.page_method_ramp), QCoreApplication.translate("MainWindow", u"Ramp stimulation-based method", None))
        self.groupBox_set_axes_Vth.setTitle(QCoreApplication.translate("MainWindow", u"Set axes", None))
        self.pushButton_setplot_Vth.setText("")
        self.GroupBox_export_results.setTitle(QCoreApplication.translate("MainWindow", u"Save data", None))
        self.pushButton_save_data_Vth.setText("")
        self.groupBox_Vth.setTitle(QCoreApplication.translate("MainWindow", u"Vth info", None))
        self.label_SD_Vth.setText(QCoreApplication.translate("MainWindow", u"s.t.d", None))
        self.label_minimum_Vth.setText(QCoreApplication.translate("MainWindow", u"Minimum", None))
        self.label_mean_Vth.setText(QCoreApplication.translate("MainWindow", u"Mean", None))
        self.label_maximum_Vth.setText(QCoreApplication.translate("MainWindow", u"Maximum", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_Vth), QCoreApplication.translate("MainWindow", u"Spike Threshold", None))
    # retranslateUi

