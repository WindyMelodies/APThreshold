# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configure_stimulation_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QLabel, QLayout, QPushButton,
    QSizePolicy, QSpinBox, QStackedWidget, QWidget)
import apprcc_rc

class Ui_configure_stimulation_window(object):
    def setupUi(self, configure_stimulation_window):
        if not configure_stimulation_window.objectName():
            configure_stimulation_window.setObjectName(u"configure_stimulation_window")
        configure_stimulation_window.resize(400, 300)
        icon = QIcon()
        icon.addFile(u":/APThrehold_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        configure_stimulation_window.setWindowIcon(icon)
        configure_stimulation_window.setStyleSheet(u"QTabWidget#tabWidget_main::tab-bar {\n"
"    alignment: left; /* \u5c06 Tab \u6807\u7b7e\u5bf9\u9f50\u5230\u5de6\u8fb9 */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: white; /* \u672a\u9009\u4e2d\u7684\u6807\u7b7e\u80cc\u666f\u989c\u8272\u4e3a\u767d\u8272 */\n"
"    height: 28px;\n"
"	/*font-family:Times New Roman ;*/\n"
"	font-weight: bold;\n"
"	/*font-size:15px;*/\n"
"    min-width: 165px;\n"
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
        self.gridLayout = QGridLayout(configure_stimulation_window)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.groupBox = QGroupBox(configure_stimulation_window)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(9, 9, 9, 9)
        self.stackedWidget = QStackedWidget(self.groupBox)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.page_DC = QWidget()
        self.page_DC.setObjectName(u"page_DC")
        self.gridLayout_2 = QGridLayout(self.page_DC)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.page_DC)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.label = QLabel(self.page_DC)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.doubleSpinBox_stop = QDoubleSpinBox(self.page_DC)
        self.doubleSpinBox_stop.setObjectName(u"doubleSpinBox_stop")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_stop.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_stop.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_stop.setDecimals(3)
        self.doubleSpinBox_stop.setMaximum(100000000.000000000000000)
        self.doubleSpinBox_stop.setValue(200.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_stop, 2, 1, 1, 1)

        self.label_7 = QLabel(self.page_DC)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.doubleSpinBox_start = QDoubleSpinBox(self.page_DC)
        self.doubleSpinBox_start.setObjectName(u"doubleSpinBox_start")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_start.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_start.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_start.setDecimals(3)
        self.doubleSpinBox_start.setMaximum(10000000.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_start, 1, 1, 1, 1)

        self.comboBox_type = QComboBox(self.page_DC)
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.setObjectName(u"comboBox_type")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_type.sizePolicy().hasHeightForWidth())
        self.comboBox_type.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.comboBox_type, 0, 1, 1, 1)

        self.label_9 = QLabel(self.page_DC)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)

        self.doubleSpinBox_amplitude_dc = QDoubleSpinBox(self.page_DC)
        self.doubleSpinBox_amplitude_dc.setObjectName(u"doubleSpinBox_amplitude_dc")

        self.gridLayout_2.addWidget(self.doubleSpinBox_amplitude_dc, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_DC)
        self.page_AC = QWidget()
        self.page_AC.setObjectName(u"page_AC")
        self.gridLayout_6 = QGridLayout(self.page_AC)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.doubleSpinBox_start_2 = QDoubleSpinBox(self.page_AC)
        self.doubleSpinBox_start_2.setObjectName(u"doubleSpinBox_start_2")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_start_2.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_start_2.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_start_2.setDecimals(3)
        self.doubleSpinBox_start_2.setMaximum(10000000.000000000000000)

        self.gridLayout_6.addWidget(self.doubleSpinBox_start_2, 1, 1, 1, 1)

        self.spinBox_frequency_ac = QSpinBox(self.page_AC)
        self.spinBox_frequency_ac.setObjectName(u"spinBox_frequency_ac")
        self.spinBox_frequency_ac.setMaximum(100000000)

        self.gridLayout_6.addWidget(self.spinBox_frequency_ac, 4, 1, 1, 1)

        self.comboBox_type_2 = QComboBox(self.page_AC)
        self.comboBox_type_2.addItem("")
        self.comboBox_type_2.addItem("")
        self.comboBox_type_2.addItem("")
        self.comboBox_type_2.addItem("")
        self.comboBox_type_2.addItem("")
        self.comboBox_type_2.setObjectName(u"comboBox_type_2")
        sizePolicy2.setHeightForWidth(self.comboBox_type_2.sizePolicy().hasHeightForWidth())
        self.comboBox_type_2.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.comboBox_type_2, 0, 1, 1, 1)

        self.label_10 = QLabel(self.page_AC)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_6.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_16 = QLabel(self.page_AC)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 1, 0, 1, 1)

        self.label_2 = QLabel(self.page_AC)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)

        self.doubleSpinBox_amplitude_ac = QDoubleSpinBox(self.page_AC)
        self.doubleSpinBox_amplitude_ac.setObjectName(u"doubleSpinBox_amplitude_ac")

        self.gridLayout_6.addWidget(self.doubleSpinBox_amplitude_ac, 3, 1, 1, 1)

        self.label_11 = QLabel(self.page_AC)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_6.addWidget(self.label_11, 4, 0, 1, 1)

        self.label_17 = QLabel(self.page_AC)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_6.addWidget(self.label_17, 2, 0, 1, 1)

        self.doubleSpinBox_stop_2 = QDoubleSpinBox(self.page_AC)
        self.doubleSpinBox_stop_2.setObjectName(u"doubleSpinBox_stop_2")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_stop_2.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_stop_2.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_stop_2.setDecimals(3)
        self.doubleSpinBox_stop_2.setMaximum(100000000.000000000000000)
        self.doubleSpinBox_stop_2.setValue(200.000000000000000)

        self.gridLayout_6.addWidget(self.doubleSpinBox_stop_2, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_AC)
        self.page_Ramp = QWidget()
        self.page_Ramp.setObjectName(u"page_Ramp")
        self.gridLayout_7 = QGridLayout(self.page_Ramp)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(6)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.page_Ramp)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_7.addWidget(self.label_18, 1, 0, 1, 1)

        self.doubleSpinBox_slope = QDoubleSpinBox(self.page_Ramp)
        self.doubleSpinBox_slope.setObjectName(u"doubleSpinBox_slope")

        self.gridLayout_7.addWidget(self.doubleSpinBox_slope, 3, 1, 1, 1)

        self.comboBox_type_3 = QComboBox(self.page_Ramp)
        self.comboBox_type_3.addItem("")
        self.comboBox_type_3.addItem("")
        self.comboBox_type_3.addItem("")
        self.comboBox_type_3.addItem("")
        self.comboBox_type_3.addItem("")
        self.comboBox_type_3.setObjectName(u"comboBox_type_3")
        sizePolicy2.setHeightForWidth(self.comboBox_type_3.sizePolicy().hasHeightForWidth())
        self.comboBox_type_3.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.comboBox_type_3, 0, 1, 1, 1)

        self.label_3 = QLabel(self.page_Ramp)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)

        self.doubleSpinBox_start_3 = QDoubleSpinBox(self.page_Ramp)
        self.doubleSpinBox_start_3.setObjectName(u"doubleSpinBox_start_3")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_start_3.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_start_3.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_start_3.setDecimals(3)
        self.doubleSpinBox_start_3.setMaximum(10000000.000000000000000)

        self.gridLayout_7.addWidget(self.doubleSpinBox_start_3, 1, 1, 1, 1)

        self.label_12 = QLabel(self.page_Ramp)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_7.addWidget(self.label_12, 3, 0, 1, 1)

        self.label_19 = QLabel(self.page_Ramp)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_7.addWidget(self.label_19, 2, 0, 1, 1)

        self.doubleSpinBox_stop_3 = QDoubleSpinBox(self.page_Ramp)
        self.doubleSpinBox_stop_3.setObjectName(u"doubleSpinBox_stop_3")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_stop_3.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_stop_3.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_stop_3.setDecimals(3)
        self.doubleSpinBox_stop_3.setMaximum(100000000.000000000000000)
        self.doubleSpinBox_stop_3.setValue(200.000000000000000)

        self.gridLayout_7.addWidget(self.doubleSpinBox_stop_3, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_Ramp)
        self.page_OU_process = QWidget()
        self.page_OU_process.setObjectName(u"page_OU_process")
        self.gridLayout_8 = QGridLayout(self.page_OU_process)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setVerticalSpacing(6)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.doubleSpinBox_start_4 = QDoubleSpinBox(self.page_OU_process)
        self.doubleSpinBox_start_4.setObjectName(u"doubleSpinBox_start_4")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_start_4.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_start_4.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_start_4.setDecimals(3)
        self.doubleSpinBox_start_4.setMaximum(10000000.000000000000000)

        self.gridLayout_8.addWidget(self.doubleSpinBox_start_4, 1, 1, 1, 1)

        self.label_4 = QLabel(self.page_OU_process)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_8.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_14 = QLabel(self.page_OU_process)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_8.addWidget(self.label_14, 4, 0, 1, 1)

        self.comboBox_type_4 = QComboBox(self.page_OU_process)
        self.comboBox_type_4.addItem("")
        self.comboBox_type_4.addItem("")
        self.comboBox_type_4.addItem("")
        self.comboBox_type_4.addItem("")
        self.comboBox_type_4.addItem("")
        self.comboBox_type_4.setObjectName(u"comboBox_type_4")
        sizePolicy2.setHeightForWidth(self.comboBox_type_4.sizePolicy().hasHeightForWidth())
        self.comboBox_type_4.setSizePolicy(sizePolicy2)

        self.gridLayout_8.addWidget(self.comboBox_type_4, 0, 1, 1, 1)

        self.doubleSpinBox_tau = QDoubleSpinBox(self.page_OU_process)
        self.doubleSpinBox_tau.setObjectName(u"doubleSpinBox_tau")

        self.gridLayout_8.addWidget(self.doubleSpinBox_tau, 4, 1, 1, 1)

        self.doubleSpinBox_miu = QDoubleSpinBox(self.page_OU_process)
        self.doubleSpinBox_miu.setObjectName(u"doubleSpinBox_miu")

        self.gridLayout_8.addWidget(self.doubleSpinBox_miu, 3, 1, 1, 1)

        self.label_13 = QLabel(self.page_OU_process)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_8.addWidget(self.label_13, 3, 0, 1, 1)

        self.label_15 = QLabel(self.page_OU_process)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_8.addWidget(self.label_15, 5, 0, 1, 1)

        self.doubleSpinBox_sigma = QDoubleSpinBox(self.page_OU_process)
        self.doubleSpinBox_sigma.setObjectName(u"doubleSpinBox_sigma")

        self.gridLayout_8.addWidget(self.doubleSpinBox_sigma, 5, 1, 1, 1)

        self.label_20 = QLabel(self.page_OU_process)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_8.addWidget(self.label_20, 1, 0, 1, 1)

        self.label_21 = QLabel(self.page_OU_process)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_8.addWidget(self.label_21, 2, 0, 1, 1)

        self.doubleSpinBox_stop_4 = QDoubleSpinBox(self.page_OU_process)
        self.doubleSpinBox_stop_4.setObjectName(u"doubleSpinBox_stop_4")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_stop_4.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_stop_4.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_stop_4.setDecimals(3)
        self.doubleSpinBox_stop_4.setMaximum(100000000.000000000000000)
        self.doubleSpinBox_stop_4.setValue(200.000000000000000)

        self.gridLayout_8.addWidget(self.doubleSpinBox_stop_4, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_OU_process)
        self.pagesynaptic_current = QWidget()
        self.pagesynaptic_current.setObjectName(u"pagesynaptic_current")
        self.gridLayout_3 = QGridLayout(self.pagesynaptic_current)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.pagesynaptic_current)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.comboBox_type_5 = QComboBox(self.pagesynaptic_current)
        self.comboBox_type_5.addItem("")
        self.comboBox_type_5.addItem("")
        self.comboBox_type_5.addItem("")
        self.comboBox_type_5.addItem("")
        self.comboBox_type_5.addItem("")
        self.comboBox_type_5.setObjectName(u"comboBox_type_5")
        sizePolicy2.setHeightForWidth(self.comboBox_type_5.sizePolicy().hasHeightForWidth())
        self.comboBox_type_5.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.comboBox_type_5, 0, 1, 1, 1)

        self.label_22 = QLabel(self.pagesynaptic_current)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 1, 0, 1, 1)

        self.doubleSpinBox_start_5 = QDoubleSpinBox(self.pagesynaptic_current)
        self.doubleSpinBox_start_5.setObjectName(u"doubleSpinBox_start_5")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_start_5.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_start_5.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_start_5.setDecimals(3)
        self.doubleSpinBox_start_5.setMaximum(10000000.000000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_start_5, 1, 1, 1, 1)

        self.label_23 = QLabel(self.pagesynaptic_current)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 2, 0, 1, 1)

        self.doubleSpinBox_stop_5 = QDoubleSpinBox(self.pagesynaptic_current)
        self.doubleSpinBox_stop_5.setObjectName(u"doubleSpinBox_stop_5")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_stop_5.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_stop_5.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_stop_5.setDecimals(3)
        self.doubleSpinBox_stop_5.setMaximum(100000000.000000000000000)
        self.doubleSpinBox_stop_5.setValue(200.000000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_stop_5, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.pagesynaptic_current)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 2)

        self.pushButton_OK = QPushButton(configure_stimulation_window)
        self.pushButton_OK.setObjectName(u"pushButton_OK")

        self.gridLayout.addWidget(self.pushButton_OK, 2, 0, 1, 1)

        self.pushButton_cancel = QPushButton(configure_stimulation_window)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.gridLayout.addWidget(self.pushButton_cancel, 2, 1, 1, 1)


        self.retranslateUi(configure_stimulation_window)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(configure_stimulation_window)
    # setupUi

    def retranslateUi(self, configure_stimulation_window):
        configure_stimulation_window.setWindowTitle(QCoreApplication.translate("configure_stimulation_window", u"Set stimulation", None))
        self.groupBox.setTitle(QCoreApplication.translate("configure_stimulation_window", u"Stimulation parameters", None))
        self.label_8.setText(QCoreApplication.translate("configure_stimulation_window", u"Stop (ms)", None))
        self.label.setText(QCoreApplication.translate("configure_stimulation_window", u"Type", None))
        self.label_7.setText(QCoreApplication.translate("configure_stimulation_window", u"Start (ms)", None))
        self.comboBox_type.setItemText(0, QCoreApplication.translate("configure_stimulation_window", u"Direct current", None))
        self.comboBox_type.setItemText(1, QCoreApplication.translate("configure_stimulation_window", u"Alternating current", None))
        self.comboBox_type.setItemText(2, QCoreApplication.translate("configure_stimulation_window", u"Ramp current", None))
        self.comboBox_type.setItemText(3, QCoreApplication.translate("configure_stimulation_window", u"OU process", None))
        self.comboBox_type.setItemText(4, QCoreApplication.translate("configure_stimulation_window", u"Synaptic current", None))

        self.label_9.setText(QCoreApplication.translate("configure_stimulation_window", u"Amplitude (\u03bcA/cm2)", None))
        self.comboBox_type_2.setItemText(0, QCoreApplication.translate("configure_stimulation_window", u"Direct current", None))
        self.comboBox_type_2.setItemText(1, QCoreApplication.translate("configure_stimulation_window", u"Alternating current", None))
        self.comboBox_type_2.setItemText(2, QCoreApplication.translate("configure_stimulation_window", u"Ramp current", None))
        self.comboBox_type_2.setItemText(3, QCoreApplication.translate("configure_stimulation_window", u"OU process", None))
        self.comboBox_type_2.setItemText(4, QCoreApplication.translate("configure_stimulation_window", u"Synaptic current", None))

        self.label_10.setText(QCoreApplication.translate("configure_stimulation_window", u"Amplitude (\u03bcA/cm2)", None))
        self.label_16.setText(QCoreApplication.translate("configure_stimulation_window", u"Start (ms)", None))
        self.label_2.setText(QCoreApplication.translate("configure_stimulation_window", u"Type", None))
        self.label_11.setText(QCoreApplication.translate("configure_stimulation_window", u"Frequency (Hz)", None))
        self.label_17.setText(QCoreApplication.translate("configure_stimulation_window", u"Stop (ms)", None))
        self.label_18.setText(QCoreApplication.translate("configure_stimulation_window", u"Start (ms)", None))
        self.comboBox_type_3.setItemText(0, QCoreApplication.translate("configure_stimulation_window", u"Direct current", None))
        self.comboBox_type_3.setItemText(1, QCoreApplication.translate("configure_stimulation_window", u"Alternating current", None))
        self.comboBox_type_3.setItemText(2, QCoreApplication.translate("configure_stimulation_window", u"Ramp current", None))
        self.comboBox_type_3.setItemText(3, QCoreApplication.translate("configure_stimulation_window", u"OU process", None))
        self.comboBox_type_3.setItemText(4, QCoreApplication.translate("configure_stimulation_window", u"Synaptic current", None))

        self.label_3.setText(QCoreApplication.translate("configure_stimulation_window", u"Type", None))
        self.label_12.setText(QCoreApplication.translate("configure_stimulation_window", u"Slope (mV/ms)", None))
        self.label_19.setText(QCoreApplication.translate("configure_stimulation_window", u"Stop (ms)", None))
        self.label_4.setText(QCoreApplication.translate("configure_stimulation_window", u"Type", None))
        self.label_14.setText(QCoreApplication.translate("configure_stimulation_window", u"\u03c4", None))
        self.comboBox_type_4.setItemText(0, QCoreApplication.translate("configure_stimulation_window", u"Direct current", None))
        self.comboBox_type_4.setItemText(1, QCoreApplication.translate("configure_stimulation_window", u"Alternating current", None))
        self.comboBox_type_4.setItemText(2, QCoreApplication.translate("configure_stimulation_window", u"Ramp current", None))
        self.comboBox_type_4.setItemText(3, QCoreApplication.translate("configure_stimulation_window", u"OU process", None))
        self.comboBox_type_4.setItemText(4, QCoreApplication.translate("configure_stimulation_window", u"Synaptic current", None))

        self.label_13.setText(QCoreApplication.translate("configure_stimulation_window", u"\u03bc", None))
        self.label_15.setText(QCoreApplication.translate("configure_stimulation_window", u"\u03c3", None))
        self.label_20.setText(QCoreApplication.translate("configure_stimulation_window", u"Start (ms)", None))
        self.label_21.setText(QCoreApplication.translate("configure_stimulation_window", u"Stop (ms)", None))
        self.label_5.setText(QCoreApplication.translate("configure_stimulation_window", u"Type", None))
        self.comboBox_type_5.setItemText(0, QCoreApplication.translate("configure_stimulation_window", u"Direct current", None))
        self.comboBox_type_5.setItemText(1, QCoreApplication.translate("configure_stimulation_window", u"Alternating current", None))
        self.comboBox_type_5.setItemText(2, QCoreApplication.translate("configure_stimulation_window", u"Ramp current", None))
        self.comboBox_type_5.setItemText(3, QCoreApplication.translate("configure_stimulation_window", u"OU process", None))
        self.comboBox_type_5.setItemText(4, QCoreApplication.translate("configure_stimulation_window", u"Synaptic current", None))

        self.label_22.setText(QCoreApplication.translate("configure_stimulation_window", u"Start (ms)", None))
        self.label_23.setText(QCoreApplication.translate("configure_stimulation_window", u"Stop (ms)", None))
        self.pushButton_OK.setText(QCoreApplication.translate("configure_stimulation_window", u"OK", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("configure_stimulation_window", u"Cancel", None))
    # retranslateUi

