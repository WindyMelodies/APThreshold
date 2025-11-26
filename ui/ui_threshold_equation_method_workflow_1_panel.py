# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'threshold_equation_method_workflow_1_panel.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)
import apprcc_rc

class Ui_workflow_1_panel(object):
    def setupUi(self, workflow_1_panel):
        if not workflow_1_panel.objectName():
            workflow_1_panel.setObjectName(u"workflow_1_panel")
        workflow_1_panel.resize(279, 597)
        workflow_1_panel.setStyleSheet(u"QGroupBox {\n"
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
        self.gridLayout = QGridLayout(workflow_1_panel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setContentsMargins(0, 3, 0, 0)
        self.Feature_calculation_workflow_1 = QGroupBox(workflow_1_panel)
        self.Feature_calculation_workflow_1.setObjectName(u"Feature_calculation_workflow_1")
        self.gridLayout_Feature_calculation_workflow_1 = QGridLayout(self.Feature_calculation_workflow_1)
        self.gridLayout_Feature_calculation_workflow_1.setSpacing(6)
        self.gridLayout_Feature_calculation_workflow_1.setObjectName(u"gridLayout_Feature_calculation_workflow_1")
        self.gridLayout_Feature_calculation_workflow_1.setContentsMargins(0, 9, 0, 0)
        self.pushButton_set_parameters_workflow_1 = QPushButton(self.Feature_calculation_workflow_1)
        self.pushButton_set_parameters_workflow_1.setObjectName(u"pushButton_set_parameters_workflow_1")
        icon = QIcon()
        icon.addFile(u":/set1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_set_parameters_workflow_1.setIcon(icon)

        self.gridLayout_Feature_calculation_workflow_1.addWidget(self.pushButton_set_parameters_workflow_1, 0, 0, 1, 1)

        self.tableWidget_features_workflow_1 = QTableWidget(self.Feature_calculation_workflow_1)
        self.tableWidget_features_workflow_1.setObjectName(u"tableWidget_features_workflow_1")

        self.gridLayout_Feature_calculation_workflow_1.addWidget(self.tableWidget_features_workflow_1, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.Feature_calculation_workflow_1, 3, 0, 1, 2)

        self.groupBox_threshold_euqation_workflow_1 = QGroupBox(workflow_1_panel)
        self.groupBox_threshold_euqation_workflow_1.setObjectName(u"groupBox_threshold_euqation_workflow_1")
        self.gridLayout_threshold_equation_workflow_1 = QGridLayout(self.groupBox_threshold_euqation_workflow_1)
        self.gridLayout_threshold_equation_workflow_1.setObjectName(u"gridLayout_threshold_equation_workflow_1")
        self.pushButton_config_threshold_params_workflow_1 = QPushButton(self.groupBox_threshold_euqation_workflow_1)
        self.pushButton_config_threshold_params_workflow_1.setObjectName(u"pushButton_config_threshold_params_workflow_1")

        self.gridLayout_threshold_equation_workflow_1.addWidget(self.pushButton_config_threshold_params_workflow_1, 3, 0, 1, 2)

        self.webEngineView_threshold_equation_workflow_1 = QWebEngineView(self.groupBox_threshold_euqation_workflow_1)
        self.webEngineView_threshold_equation_workflow_1.setObjectName(u"webEngineView_threshold_equation_workflow_1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webEngineView_threshold_equation_workflow_1.sizePolicy().hasHeightForWidth())
        self.webEngineView_threshold_equation_workflow_1.setSizePolicy(sizePolicy)
        self.webEngineView_threshold_equation_workflow_1.setMinimumSize(QSize(0, 0))
        self.webEngineView_threshold_equation_workflow_1.setUrl(QUrl(u"about:blank"))

        self.gridLayout_threshold_equation_workflow_1.addWidget(self.webEngineView_threshold_equation_workflow_1, 2, 0, 1, 2)

        self.pushButton_run_workflow_1 = QPushButton(self.groupBox_threshold_euqation_workflow_1)
        self.pushButton_run_workflow_1.setObjectName(u"pushButton_run_workflow_1")

        self.gridLayout_threshold_equation_workflow_1.addWidget(self.pushButton_run_workflow_1, 4, 0, 1, 2)

        self.comboBox_threshold_equation_option_workflow_1 = QComboBox(self.groupBox_threshold_euqation_workflow_1)
        self.comboBox_threshold_equation_option_workflow_1.addItem("")
        self.comboBox_threshold_equation_option_workflow_1.addItem("")
        self.comboBox_threshold_equation_option_workflow_1.addItem("")
        self.comboBox_threshold_equation_option_workflow_1.setObjectName(u"comboBox_threshold_equation_option_workflow_1")

        self.gridLayout_threshold_equation_workflow_1.addWidget(self.comboBox_threshold_equation_option_workflow_1, 0, 1, 1, 1)

        self.label_threshold_equation_option_workflow_1 = QLabel(self.groupBox_threshold_euqation_workflow_1)
        self.label_threshold_equation_option_workflow_1.setObjectName(u"label_threshold_equation_option_workflow_1")

        self.gridLayout_threshold_equation_workflow_1.addWidget(self.label_threshold_equation_option_workflow_1, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_threshold_euqation_workflow_1, 1, 0, 1, 2)

        self.groupBox = QGroupBox(workflow_1_panel)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_ev = QLineEdit(self.groupBox)
        self.lineEdit_ev.setObjectName(u"lineEdit_ev")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_ev.sizePolicy().hasHeightForWidth())
        self.lineEdit_ev.setSizePolicy(sizePolicy1)
        self.lineEdit_ev.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_ev, 2, 1, 1, 1)

        self.lineEdit_fa = QLineEdit(self.groupBox)
        self.lineEdit_fa.setObjectName(u"lineEdit_fa")
        sizePolicy1.setHeightForWidth(self.lineEdit_fa.sizePolicy().hasHeightForWidth())
        self.lineEdit_fa.setSizePolicy(sizePolicy1)
        self.lineEdit_fa.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_fa, 1, 1, 1, 1)

        self.doubleSpinBox_time_window = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_time_window.setObjectName(u"doubleSpinBox_time_window")
        self.doubleSpinBox_time_window.setValue(0.840000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_time_window, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.pushButton_calculate = QPushButton(self.groupBox)
        self.pushButton_calculate.setObjectName(u"pushButton_calculate")

        self.gridLayout_2.addWidget(self.pushButton_calculate, 3, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 2)

        self.pushButton_back_to_home_workflow_1 = QPushButton(workflow_1_panel)
        self.pushButton_back_to_home_workflow_1.setObjectName(u"pushButton_back_to_home_workflow_1")
        icon1 = QIcon()
        icon1.addFile(u":/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_back_to_home_workflow_1.setIcon(icon1)

        self.gridLayout.addWidget(self.pushButton_back_to_home_workflow_1, 0, 0, 1, 2)


        self.retranslateUi(workflow_1_panel)

        QMetaObject.connectSlotsByName(workflow_1_panel)
    # setupUi

    def retranslateUi(self, workflow_1_panel):
        workflow_1_panel.setWindowTitle(QCoreApplication.translate("workflow_1_panel", u"Workflow 1", None))
        self.Feature_calculation_workflow_1.setTitle(QCoreApplication.translate("workflow_1_panel", u"Feature calculation", None))
        self.pushButton_set_parameters_workflow_1.setText(QCoreApplication.translate("workflow_1_panel", u"Set parameters", None))
        self.groupBox_threshold_euqation_workflow_1.setTitle(QCoreApplication.translate("workflow_1_panel", u"Vth prediction", None))
        self.pushButton_config_threshold_params_workflow_1.setText(QCoreApplication.translate("workflow_1_panel", u"Configure equation parameters", None))
        self.pushButton_run_workflow_1.setText(QCoreApplication.translate("workflow_1_panel", u"Run", None))
        self.comboBox_threshold_equation_option_workflow_1.setItemText(0, QCoreApplication.translate("workflow_1_panel", u"Form one", None))
        self.comboBox_threshold_equation_option_workflow_1.setItemText(1, QCoreApplication.translate("workflow_1_panel", u"Form two", None))
        self.comboBox_threshold_equation_option_workflow_1.setItemText(2, QCoreApplication.translate("workflow_1_panel", u"Form three", None))

        self.label_threshold_equation_option_workflow_1.setText(QCoreApplication.translate("workflow_1_panel", u"Equation option", None))
        self.groupBox.setTitle(QCoreApplication.translate("workflow_1_panel", u"Prediction performance", None))
        self.label_2.setText(QCoreApplication.translate("workflow_1_panel", u"False alarms", None))
        self.label.setText(QCoreApplication.translate("workflow_1_panel", u"Time window \u03c3 (ms)", None))
        self.label_3.setText(QCoreApplication.translate("workflow_1_panel", u"Explained variance", None))
        self.pushButton_calculate.setText(QCoreApplication.translate("workflow_1_panel", u"Calculate", None))
        self.pushButton_back_to_home_workflow_1.setText(QCoreApplication.translate("workflow_1_panel", u"Back", None))
    # retranslateUi

