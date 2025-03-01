# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculate_feature_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QGroupBox,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QTabWidget, QWidget)

class Ui_Form_paras_of_features(object):
    def setupUi(self, Form_paras_of_features):
        if not Form_paras_of_features.objectName():
            Form_paras_of_features.setObjectName(u"Form_paras_of_features")
        Form_paras_of_features.resize(434, 300)
        icon = QIcon()
        icon.addFile(u":/APThrehold_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_paras_of_features.setWindowIcon(icon)
        Form_paras_of_features.setStyleSheet(u"QWidget#Form_paras_of_features {background-color: #E4F4FE}")
        self.gridLayout = QGridLayout(Form_paras_of_features)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_save = QPushButton(Form_paras_of_features)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.gridLayout.addWidget(self.pushButton_save, 1, 0, 1, 1)

        self.pushButton_canel = QPushButton(Form_paras_of_features)
        self.pushButton_canel.setObjectName(u"pushButton_canel")

        self.gridLayout.addWidget(self.pushButton_canel, 1, 1, 1, 1)

        self.tabWidget = QTabWidget(Form_paras_of_features)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget#tabWidget_main::tab-bar {\n"
"    alignment: left; /* \u5c06 Tab \u6807\u7b7e\u5bf9\u9f50\u5230\u5de6\u8fb9 */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: white; /* \u672a\u9009\u4e2d\u7684\u6807\u7b7e\u80cc\u666f\u989c\u8272\u4e3a\u767d\u8272 */\n"
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
"    background-color: white; /* \u672a\u9009\u4e2d\u7684\u6807\u7b7e\u80cc\u666f\u989c\u8272\u4e3a\u767d\u8272 */\n"
"    color: bl"
                        "ack; /* \u672a\u9009\u4e2d\u7684\u6807\u7b7e\u6587\u5b57\u989c\u8272\u4e3a\u9ed1\u8272\uff08\u53ef\u9009\uff09 */\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.doubleSpinBox_time_average_Vm = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_time_average_Vm.setObjectName(u"doubleSpinBox_time_average_Vm")

        self.gridLayout_2.addWidget(self.doubleSpinBox_time_average_Vm, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 9)
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)

        self.doubleSpinBox_time_dvdt = QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_time_dvdt.setObjectName(u"doubleSpinBox_time_dvdt")

        self.gridLayout_4.addWidget(self.doubleSpinBox_time_dvdt, 1, 1, 1, 1)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 1, 2, 1, 1)

        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radioButton_average_dvdt = QRadioButton(self.groupBox)
        self.radioButton_average_dvdt.setObjectName(u"radioButton_average_dvdt")

        self.gridLayout_3.addWidget(self.radioButton_average_dvdt, 0, 0, 1, 1)

        self.radioButton_maximum = QRadioButton(self.groupBox)
        self.radioButton_maximum.setObjectName(u"radioButton_maximum")

        self.gridLayout_3.addWidget(self.radioButton_maximum, 2, 0, 1, 1)

        self.radioButton_slope_two_points = QRadioButton(self.groupBox)
        self.radioButton_slope_two_points.setObjectName(u"radioButton_slope_two_points")

        self.gridLayout_3.addWidget(self.radioButton_slope_two_points, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)


        self.retranslateUi(Form_paras_of_features)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form_paras_of_features)
    # setupUi

    def retranslateUi(self, Form_paras_of_features):
        Form_paras_of_features.setWindowTitle(QCoreApplication.translate("Form_paras_of_features", u"Set parameters", None))
        self.pushButton_save.setText(QCoreApplication.translate("Form_paras_of_features", u"Calculate", None))
        self.pushButton_canel.setText(QCoreApplication.translate("Form_paras_of_features", u"Canel", None))
        self.label_2.setText(QCoreApplication.translate("Form_paras_of_features", u"ms", None))
        self.label.setText(QCoreApplication.translate("Form_paras_of_features", u"Time period preceding each spike", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form_paras_of_features", u"<V>", None))
        self.label_3.setText(QCoreApplication.translate("Form_paras_of_features", u"Time period preceding each spike", None))
        self.label_4.setText(QCoreApplication.translate("Form_paras_of_features", u"ms", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form_paras_of_features", u"Options", None))
        self.radioButton_average_dvdt.setText(QCoreApplication.translate("Form_paras_of_features", u"Average of dVm/dt over a time period", None))
        self.radioButton_maximum.setText(QCoreApplication.translate("Form_paras_of_features", u"Maximum of dVm/dt during upstroke", None))
        self.radioButton_slope_two_points.setText(QCoreApplication.translate("Form_paras_of_features", u"Slope of Vm within a time period", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form_paras_of_features", u"dV/dt", None))
    # retranslateUi

