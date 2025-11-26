# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'threshold_equation_method_workflow_2_panel.ui'
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
    QGroupBox, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem,
    QWidget)
import apprcc_rc

class Ui_workflow_2_panel(object):
    def setupUi(self, workflow_2_panel):
        if not workflow_2_panel.objectName():
            workflow_2_panel.setObjectName(u"workflow_2_panel")
        workflow_2_panel.resize(279, 758)
        workflow_2_panel.setStyleSheet(u"QGroupBox {\n"
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
        self.gridLayout = QGridLayout(workflow_2_panel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setContentsMargins(0, 3, 0, 0)
        self.pushButton_return = QPushButton(workflow_2_panel)
        self.pushButton_return.setObjectName(u"pushButton_return")
        icon = QIcon()
        icon.addFile(u":/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_return.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_return, 0, 0, 1, 2)

        self.groupBox_2 = QGroupBox(workflow_2_panel)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.spinBox_duration = QSpinBox(self.groupBox_2)
        self.spinBox_duration.setObjectName(u"spinBox_duration")
        self.spinBox_duration.setMaximum(10000000)
        self.spinBox_duration.setValue(200)

        self.gridLayout_3.addWidget(self.spinBox_duration, 0, 1, 1, 1)

        self.comboBox_ode_solver = QComboBox(self.groupBox_2)
        self.comboBox_ode_solver.addItem("")
        self.comboBox_ode_solver.addItem("")
        self.comboBox_ode_solver.setObjectName(u"comboBox_ode_solver")

        self.gridLayout_3.addWidget(self.comboBox_ode_solver, 3, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.doubleSpinBox_dt = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_dt.setObjectName(u"doubleSpinBox_dt")
        self.doubleSpinBox_dt.setDecimals(3)
        self.doubleSpinBox_dt.setValue(0.010000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_dt, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.pushButton_run = QPushButton(self.groupBox_2)
        self.pushButton_run.setObjectName(u"pushButton_run")

        self.gridLayout_3.addWidget(self.pushButton_run, 4, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 2)

        self.Feature_calculation = QGroupBox(workflow_2_panel)
        self.Feature_calculation.setObjectName(u"Feature_calculation")
        self.gridLayout_Feature_calculation_workflow_1 = QGridLayout(self.Feature_calculation)
        self.gridLayout_Feature_calculation_workflow_1.setSpacing(6)
        self.gridLayout_Feature_calculation_workflow_1.setObjectName(u"gridLayout_Feature_calculation_workflow_1")
        self.gridLayout_Feature_calculation_workflow_1.setContentsMargins(0, 9, 0, 0)
        self.pushButton_set_parameters = QPushButton(self.Feature_calculation)
        self.pushButton_set_parameters.setObjectName(u"pushButton_set_parameters")
        icon1 = QIcon()
        icon1.addFile(u":/set1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_set_parameters.setIcon(icon1)

        self.gridLayout_Feature_calculation_workflow_1.addWidget(self.pushButton_set_parameters, 0, 0, 1, 1)

        self.tableWidget_features = QTableWidget(self.Feature_calculation)
        self.tableWidget_features.setObjectName(u"tableWidget_features")

        self.gridLayout_Feature_calculation_workflow_1.addWidget(self.tableWidget_features, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.Feature_calculation, 4, 0, 1, 2)

        self.groupBox = QGroupBox(workflow_2_panel)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_set_stimulation = QPushButton(self.groupBox)
        self.pushButton_set_stimulation.setObjectName(u"pushButton_set_stimulation")

        self.gridLayout_2.addWidget(self.pushButton_set_stimulation, 1, 0, 1, 2)

        self.comboBox_IF_model = QComboBox(self.groupBox)
        self.comboBox_IF_model.addItem("")
        self.comboBox_IF_model.setObjectName(u"comboBox_IF_model")

        self.gridLayout_2.addWidget(self.comboBox_IF_model, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)

        self.groupBox_threshold_euqation = QGroupBox(workflow_2_panel)
        self.groupBox_threshold_euqation.setObjectName(u"groupBox_threshold_euqation")
        self.gridLayout_threshold_equation_workflow_1 = QGridLayout(self.groupBox_threshold_euqation)
        self.gridLayout_threshold_equation_workflow_1.setObjectName(u"gridLayout_threshold_equation_workflow_1")
        self.pushButton_config_threshold_params = QPushButton(self.groupBox_threshold_euqation)
        self.pushButton_config_threshold_params.setObjectName(u"pushButton_config_threshold_params")

        self.gridLayout_threshold_equation_workflow_1.addWidget(self.pushButton_config_threshold_params, 3, 0, 1, 2)

        self.comboBox_threshold_equation_option = QComboBox(self.groupBox_threshold_euqation)
        self.comboBox_threshold_equation_option.addItem("")
        self.comboBox_threshold_equation_option.addItem("")
        self.comboBox_threshold_equation_option.addItem("")
        self.comboBox_threshold_equation_option.setObjectName(u"comboBox_threshold_equation_option")

        self.gridLayout_threshold_equation_workflow_1.addWidget(self.comboBox_threshold_equation_option, 0, 1, 1, 1)

        self.webEngineView_threshold_equation = QWebEngineView(self.groupBox_threshold_euqation)
        self.webEngineView_threshold_equation.setObjectName(u"webEngineView_threshold_equation")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webEngineView_threshold_equation.sizePolicy().hasHeightForWidth())
        self.webEngineView_threshold_equation.setSizePolicy(sizePolicy)
        self.webEngineView_threshold_equation.setMinimumSize(QSize(0, 0))
        self.webEngineView_threshold_equation.setUrl(QUrl(u"about:blank"))

        self.gridLayout_threshold_equation_workflow_1.addWidget(self.webEngineView_threshold_equation, 2, 0, 1, 2)

        self.label_threshold_equation_option = QLabel(self.groupBox_threshold_euqation)
        self.label_threshold_equation_option.setObjectName(u"label_threshold_equation_option")

        self.gridLayout_threshold_equation_workflow_1.addWidget(self.label_threshold_equation_option, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_threshold_euqation, 2, 0, 1, 2)


        self.retranslateUi(workflow_2_panel)

        QMetaObject.connectSlotsByName(workflow_2_panel)
    # setupUi

    def retranslateUi(self, workflow_2_panel):
        workflow_2_panel.setWindowTitle(QCoreApplication.translate("workflow_2_panel", u"Workflow 1", None))
        self.pushButton_return.setText(QCoreApplication.translate("workflow_2_panel", u"Back", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("workflow_2_panel", u"Simulation control", None))
        self.comboBox_ode_solver.setItemText(0, QCoreApplication.translate("workflow_2_panel", u"Euler", None))
        self.comboBox_ode_solver.setItemText(1, QCoreApplication.translate("workflow_2_panel", u"Runge-Kutta 4", None))

        self.label_3.setText(QCoreApplication.translate("workflow_2_panel", u"ODE solver", None))
        self.label_2.setText(QCoreApplication.translate("workflow_2_panel", u"Duration (ms)", None))
        self.label_4.setText(QCoreApplication.translate("workflow_2_panel", u"dt (ms)", None))
        self.pushButton_run.setText(QCoreApplication.translate("workflow_2_panel", u"Run", None))
        self.Feature_calculation.setTitle(QCoreApplication.translate("workflow_2_panel", u"Feature calculation", None))
        self.pushButton_set_parameters.setText(QCoreApplication.translate("workflow_2_panel", u"Set parameters", None))
        self.groupBox.setTitle(QCoreApplication.translate("workflow_2_panel", u"IF model", None))
        self.label.setText(QCoreApplication.translate("workflow_2_panel", u"Name", None))
        self.pushButton_set_stimulation.setText(QCoreApplication.translate("workflow_2_panel", u"Set stimulation", None))
        self.comboBox_IF_model.setItemText(0, QCoreApplication.translate("workflow_2_panel", u"LIF model", None))

        self.groupBox_threshold_euqation.setTitle(QCoreApplication.translate("workflow_2_panel", u"Threshold equation", None))
        self.pushButton_config_threshold_params.setText(QCoreApplication.translate("workflow_2_panel", u"Configure equation parameters", None))
        self.comboBox_threshold_equation_option.setItemText(0, QCoreApplication.translate("workflow_2_panel", u"Form one", None))
        self.comboBox_threshold_equation_option.setItemText(1, QCoreApplication.translate("workflow_2_panel", u"Form two", None))
        self.comboBox_threshold_equation_option.setItemText(2, QCoreApplication.translate("workflow_2_panel", u"Form three", None))

        self.label_threshold_equation_option.setText(QCoreApplication.translate("workflow_2_panel", u"Equation option", None))
    # retranslateUi

