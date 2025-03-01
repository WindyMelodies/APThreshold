# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ramp_based_method_window.ui'
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
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)
import ui.apprcc_rc

class Ui_RampMethodWindow(object):
    def setupUi(self, RampMethodWindow):
        if not RampMethodWindow.objectName():
            RampMethodWindow.setObjectName(u"RampMethodWindow")
        RampMethodWindow.resize(300, 825)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RampMethodWindow.sizePolicy().hasHeightForWidth())
        RampMethodWindow.setSizePolicy(sizePolicy)
        RampMethodWindow.setMinimumSize(QSize(300, 0))
        RampMethodWindow.setMaximumSize(QSize(300, 16777215))
        self.gridLayout_ramp_method_window = QGridLayout(RampMethodWindow)
        self.gridLayout_ramp_method_window.setObjectName(u"gridLayout_ramp_method_window")
        self.gridLayout_ramp_method_window.setVerticalSpacing(0)
        self.gridLayout_ramp_method_window.setContentsMargins(0, 0, 0, 0)
        self.groupBox_ramp_stimulation_method_set_paras = QGroupBox(RampMethodWindow)
        self.groupBox_ramp_stimulation_method_set_paras.setObjectName(u"groupBox_ramp_stimulation_method_set_paras")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_ramp_stimulation_method_set_paras.sizePolicy().hasHeightForWidth())
        self.groupBox_ramp_stimulation_method_set_paras.setSizePolicy(sizePolicy1)
        self.gridLayout_Vth_quantification_ramp = QGridLayout(self.groupBox_ramp_stimulation_method_set_paras)
        self.gridLayout_Vth_quantification_ramp.setObjectName(u"gridLayout_Vth_quantification_ramp")
        self.gridLayout_Vth_quantification_ramp.setContentsMargins(9, -1, -1, -1)
        self.label_model_ramp = QLabel(self.groupBox_ramp_stimulation_method_set_paras)
        self.label_model_ramp.setObjectName(u"label_model_ramp")

        self.gridLayout_Vth_quantification_ramp.addWidget(self.label_model_ramp, 0, 0, 1, 1)

        self.comboBox_stimulus_name_ramp = QComboBox(self.groupBox_ramp_stimulation_method_set_paras)
        self.comboBox_stimulus_name_ramp.setObjectName(u"comboBox_stimulus_name_ramp")

        self.gridLayout_Vth_quantification_ramp.addWidget(self.comboBox_stimulus_name_ramp, 2, 1, 1, 1)

        self.label_voltage_ramp = QLabel(self.groupBox_ramp_stimulation_method_set_paras)
        self.label_voltage_ramp.setObjectName(u"label_voltage_ramp")

        self.gridLayout_Vth_quantification_ramp.addWidget(self.label_voltage_ramp, 1, 0, 1, 1)

        self.doubleSpinBox_precision_ramp = QDoubleSpinBox(self.groupBox_ramp_stimulation_method_set_paras)
        self.doubleSpinBox_precision_ramp.setObjectName(u"doubleSpinBox_precision_ramp")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_precision_ramp.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_precision_ramp.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_precision_ramp.setMinimumSize(QSize(0, 0))
        self.doubleSpinBox_precision_ramp.setMaximumSize(QSize(16777215, 16777215))
        self.doubleSpinBox_precision_ramp.setValue(0.030000000000000)

        self.gridLayout_Vth_quantification_ramp.addWidget(self.doubleSpinBox_precision_ramp, 4, 1, 1, 1)

        self.comboBox_model_ramp = QComboBox(self.groupBox_ramp_stimulation_method_set_paras)
        self.comboBox_model_ramp.setObjectName(u"comboBox_model_ramp")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_model_ramp.sizePolicy().hasHeightForWidth())
        self.comboBox_model_ramp.setSizePolicy(sizePolicy3)
        self.comboBox_model_ramp.setMinimumSize(QSize(150, 0))
        self.comboBox_model_ramp.setMaximumSize(QSize(185, 16777215))

        self.gridLayout_Vth_quantification_ramp.addWidget(self.comboBox_model_ramp, 0, 1, 1, 1)

        self.lineEdit_k_ramp = QLineEdit(self.groupBox_ramp_stimulation_method_set_paras)
        self.lineEdit_k_ramp.setObjectName(u"lineEdit_k_ramp")
        sizePolicy2.setHeightForWidth(self.lineEdit_k_ramp.sizePolicy().hasHeightForWidth())
        self.lineEdit_k_ramp.setSizePolicy(sizePolicy2)

        self.gridLayout_Vth_quantification_ramp.addWidget(self.lineEdit_k_ramp, 3, 1, 1, 1)

        self.label_precision_ramp = QLabel(self.groupBox_ramp_stimulation_method_set_paras)
        self.label_precision_ramp.setObjectName(u"label_precision_ramp")

        self.gridLayout_Vth_quantification_ramp.addWidget(self.label_precision_ramp, 4, 0, 1, 1)

        self.comboBox_voltage_ramp = QComboBox(self.groupBox_ramp_stimulation_method_set_paras)
        self.comboBox_voltage_ramp.setObjectName(u"comboBox_voltage_ramp")

        self.gridLayout_Vth_quantification_ramp.addWidget(self.comboBox_voltage_ramp, 1, 1, 1, 1)

        self.label_stimulus_name_ramp = QLabel(self.groupBox_ramp_stimulation_method_set_paras)
        self.label_stimulus_name_ramp.setObjectName(u"label_stimulus_name_ramp")

        self.gridLayout_Vth_quantification_ramp.addWidget(self.label_stimulus_name_ramp, 2, 0, 1, 1)

        self.label_k_ramp = QLabel(self.groupBox_ramp_stimulation_method_set_paras)
        self.label_k_ramp.setObjectName(u"label_k_ramp")

        self.gridLayout_Vth_quantification_ramp.addWidget(self.label_k_ramp, 3, 0, 1, 1)


        self.gridLayout_ramp_method_window.addWidget(self.groupBox_ramp_stimulation_method_set_paras, 0, 0, 1, 1)

        self.groupBox_ramp_method_simulation = QGroupBox(RampMethodWindow)
        self.groupBox_ramp_method_simulation.setObjectName(u"groupBox_ramp_method_simulation")
        sizePolicy1.setHeightForWidth(self.groupBox_ramp_method_simulation.sizePolicy().hasHeightForWidth())
        self.groupBox_ramp_method_simulation.setSizePolicy(sizePolicy1)
        self.gridLayout_simulation_control_ramp = QGridLayout(self.groupBox_ramp_method_simulation)
        self.gridLayout_simulation_control_ramp.setObjectName(u"gridLayout_simulation_control_ramp")
        self.doubleSpinBox_ramp_timeline = QDoubleSpinBox(self.groupBox_ramp_method_simulation)
        self.doubleSpinBox_ramp_timeline.setObjectName(u"doubleSpinBox_ramp_timeline")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_ramp_timeline.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_ramp_timeline.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_ramp_timeline.setMaximum(100000000.000000000000000)
        self.doubleSpinBox_ramp_timeline.setValue(100.000000000000000)

        self.gridLayout_simulation_control_ramp.addWidget(self.doubleSpinBox_ramp_timeline, 1, 1, 1, 1)

        self.label_dt_ramp = QLabel(self.groupBox_ramp_method_simulation)
        self.label_dt_ramp.setObjectName(u"label_dt_ramp")

        self.gridLayout_simulation_control_ramp.addWidget(self.label_dt_ramp, 3, 0, 1, 1)

        self.label_timeline_ramp = QLabel(self.groupBox_ramp_method_simulation)
        self.label_timeline_ramp.setObjectName(u"label_timeline_ramp")

        self.gridLayout_simulation_control_ramp.addWidget(self.label_timeline_ramp, 1, 0, 1, 1)

        self.doubleSpinBox_dt_ramp = QDoubleSpinBox(self.groupBox_ramp_method_simulation)
        self.doubleSpinBox_dt_ramp.setObjectName(u"doubleSpinBox_dt_ramp")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_dt_ramp.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_dt_ramp.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_dt_ramp.setDecimals(3)
        self.doubleSpinBox_dt_ramp.setValue(0.001000000000000)

        self.gridLayout_simulation_control_ramp.addWidget(self.doubleSpinBox_dt_ramp, 3, 1, 1, 1)

        self.comboBox_ramp_ode_option = QComboBox(self.groupBox_ramp_method_simulation)
        self.comboBox_ramp_ode_option.addItem("")
        self.comboBox_ramp_ode_option.setObjectName(u"comboBox_ramp_ode_option")

        self.gridLayout_simulation_control_ramp.addWidget(self.comboBox_ramp_ode_option, 2, 1, 1, 1)

        self.label_ramp_ode_option = QLabel(self.groupBox_ramp_method_simulation)
        self.label_ramp_ode_option.setObjectName(u"label_ramp_ode_option")

        self.gridLayout_simulation_control_ramp.addWidget(self.label_ramp_ode_option, 2, 0, 1, 1)

        self.pushButton_run_ramp = QPushButton(self.groupBox_ramp_method_simulation)
        self.pushButton_run_ramp.setObjectName(u"pushButton_run_ramp")

        self.gridLayout_simulation_control_ramp.addWidget(self.pushButton_run_ramp, 4, 0, 1, 2)


        self.gridLayout_ramp_method_window.addWidget(self.groupBox_ramp_method_simulation, 1, 0, 1, 1)

        self.groupBox_features_ramp = QGroupBox(RampMethodWindow)
        self.groupBox_features_ramp.setObjectName(u"groupBox_features_ramp")
        sizePolicy1.setHeightForWidth(self.groupBox_features_ramp.sizePolicy().hasHeightForWidth())
        self.groupBox_features_ramp.setSizePolicy(sizePolicy1)
        self.gridLayout_ramp_features = QGridLayout(self.groupBox_features_ramp)
        self.gridLayout_ramp_features.setObjectName(u"gridLayout_ramp_features")
        self.gridLayout_ramp_features.setContentsMargins(0, -1, 0, 0)
        self.tableWidget_features_ramp = QTableWidget(self.groupBox_features_ramp)
        self.tableWidget_features_ramp.setObjectName(u"tableWidget_features_ramp")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget_features_ramp.sizePolicy().hasHeightForWidth())
        self.tableWidget_features_ramp.setSizePolicy(sizePolicy4)

        self.gridLayout_ramp_features.addWidget(self.tableWidget_features_ramp, 1, 0, 1, 1)

        self.pushButton_set_paras_ramp = QPushButton(self.groupBox_features_ramp)
        self.pushButton_set_paras_ramp.setObjectName(u"pushButton_set_paras_ramp")
        icon = QIcon()
        icon.addFile(u":/set1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_set_paras_ramp.setIcon(icon)

        self.gridLayout_ramp_features.addWidget(self.pushButton_set_paras_ramp, 0, 0, 1, 1)


        self.gridLayout_ramp_method_window.addWidget(self.groupBox_features_ramp, 2, 0, 1, 1)


        self.retranslateUi(RampMethodWindow)

        QMetaObject.connectSlotsByName(RampMethodWindow)
    # setupUi

    def retranslateUi(self, RampMethodWindow):
        RampMethodWindow.setWindowTitle(QCoreApplication.translate("RampMethodWindow", u"Form", None))
        self.groupBox_ramp_stimulation_method_set_paras.setTitle(QCoreApplication.translate("RampMethodWindow", u"Vth quantification", None))
        self.label_model_ramp.setText(QCoreApplication.translate("RampMethodWindow", u"Model", None))
        self.label_voltage_ramp.setText(QCoreApplication.translate("RampMethodWindow", u"Voltage ", None))
        self.lineEdit_k_ramp.setText(QCoreApplication.translate("RampMethodWindow", u"1", None))
        self.label_precision_ramp.setText(QCoreApplication.translate("RampMethodWindow", u"Precision (mV)", None))
        self.label_stimulus_name_ramp.setText(QCoreApplication.translate("RampMethodWindow", u"Iramp", None))
        self.label_k_ramp.setText(QCoreApplication.translate("RampMethodWindow", u"<html><head/><body><p>Slope (\u03bcA/(cm<span style=\" vertical-align:super;\">2</span>\u00b7ms))</p></body></html>", None))
        self.groupBox_ramp_method_simulation.setTitle(QCoreApplication.translate("RampMethodWindow", u"Simulation control", None))
        self.label_dt_ramp.setText(QCoreApplication.translate("RampMethodWindow", u"dt (ms)", None))
        self.label_timeline_ramp.setText(QCoreApplication.translate("RampMethodWindow", u"Duration (ms)", None))
        self.comboBox_ramp_ode_option.setItemText(0, QCoreApplication.translate("RampMethodWindow", u"odeint", None))

        self.label_ramp_ode_option.setText(QCoreApplication.translate("RampMethodWindow", u"ODE solver", None))
        self.pushButton_run_ramp.setText(QCoreApplication.translate("RampMethodWindow", u"Run", None))
        self.groupBox_features_ramp.setTitle(QCoreApplication.translate("RampMethodWindow", u"Feature calculation", None))
        self.pushButton_set_paras_ramp.setText(QCoreApplication.translate("RampMethodWindow", u"Set parameters", None))
    # retranslateUi

