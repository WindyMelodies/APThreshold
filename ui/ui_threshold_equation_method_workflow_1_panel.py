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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTextEdit, QWidget)
import apprcc_rc

class Ui_workflow_1_panel(object):
    def setupUi(self, workflow_1_panel):
        if not workflow_1_panel.objectName():
            workflow_1_panel.setObjectName(u"workflow_1_panel")
        workflow_1_panel.resize(279, 597)
        self.gridLayout = QGridLayout(workflow_1_panel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_back_to_home_workflow_1 = QPushButton(workflow_1_panel)
        self.pushButton_back_to_home_workflow_1.setObjectName(u"pushButton_back_to_home_workflow_1")

        self.gridLayout.addWidget(self.pushButton_back_to_home_workflow_1, 0, 0, 1, 1)

        self.pushButton_reset_workflow_1 = QPushButton(workflow_1_panel)
        self.pushButton_reset_workflow_1.setObjectName(u"pushButton_reset_workflow_1")

        self.gridLayout.addWidget(self.pushButton_reset_workflow_1, 0, 1, 1, 1)

        self.groupBox_threshold_euqation_workflow_1 = QGroupBox(workflow_1_panel)
        self.groupBox_threshold_euqation_workflow_1.setObjectName(u"groupBox_threshold_euqation_workflow_1")
        self.gridLayout_threshold_equation_workflow_1 = QGridLayout(self.groupBox_threshold_euqation_workflow_1)
        self.gridLayout_threshold_equation_workflow_1.setObjectName(u"gridLayout_threshold_equation_workflow_1")
        self.pushButton_config_threshold_params_workflow_1 = QPushButton(self.groupBox_threshold_euqation_workflow_1)
        self.pushButton_config_threshold_params_workflow_1.setObjectName(u"pushButton_config_threshold_params_workflow_1")

        self.gridLayout_threshold_equation_workflow_1.addWidget(self.pushButton_config_threshold_params_workflow_1, 2, 0, 1, 2)

        self.comboBox_threshold_equation_option_workflow_1 = QComboBox(self.groupBox_threshold_euqation_workflow_1)
        self.comboBox_threshold_equation_option_workflow_1.setObjectName(u"comboBox_threshold_equation_option_workflow_1")

        self.gridLayout_threshold_equation_workflow_1.addWidget(self.comboBox_threshold_equation_option_workflow_1, 0, 1, 1, 1)

        self.label_threshold_equation_option_workflow_1 = QLabel(self.groupBox_threshold_euqation_workflow_1)
        self.label_threshold_equation_option_workflow_1.setObjectName(u"label_threshold_equation_option_workflow_1")

        self.gridLayout_threshold_equation_workflow_1.addWidget(self.label_threshold_equation_option_workflow_1, 0, 0, 1, 1)

        self.textEdit_threshold_equation_workflow_1 = QTextEdit(self.groupBox_threshold_euqation_workflow_1)
        self.textEdit_threshold_equation_workflow_1.setObjectName(u"textEdit_threshold_equation_workflow_1")
        self.textEdit_threshold_equation_workflow_1.setReadOnly(True)

        self.gridLayout_threshold_equation_workflow_1.addWidget(self.textEdit_threshold_equation_workflow_1, 1, 0, 1, 2)

        self.pushButton_run_workflow_1 = QPushButton(self.groupBox_threshold_euqation_workflow_1)
        self.pushButton_run_workflow_1.setObjectName(u"pushButton_run_workflow_1")

        self.gridLayout_threshold_equation_workflow_1.addWidget(self.pushButton_run_workflow_1, 3, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox_threshold_euqation_workflow_1, 1, 0, 1, 2)

        self.Feature_calculation_workflow_1 = QGroupBox(workflow_1_panel)
        self.Feature_calculation_workflow_1.setObjectName(u"Feature_calculation_workflow_1")
        self.gridLayout_Feature_calculation_workflow_1 = QGridLayout(self.Feature_calculation_workflow_1)
        self.gridLayout_Feature_calculation_workflow_1.setSpacing(6)
        self.gridLayout_Feature_calculation_workflow_1.setObjectName(u"gridLayout_Feature_calculation_workflow_1")
        self.gridLayout_Feature_calculation_workflow_1.setContentsMargins(0, 9, 0, 0)
        self.tableWidget_features_workflow_1 = QTableWidget(self.Feature_calculation_workflow_1)
        self.tableWidget_features_workflow_1.setObjectName(u"tableWidget_features_workflow_1")

        self.gridLayout_Feature_calculation_workflow_1.addWidget(self.tableWidget_features_workflow_1, 1, 0, 1, 1)

        self.pushButton_set_parameters_workflow_1 = QPushButton(self.Feature_calculation_workflow_1)
        self.pushButton_set_parameters_workflow_1.setObjectName(u"pushButton_set_parameters_workflow_1")
        icon = QIcon()
        icon.addFile(u":/set1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_set_parameters_workflow_1.setIcon(icon)

        self.gridLayout_Feature_calculation_workflow_1.addWidget(self.pushButton_set_parameters_workflow_1, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.Feature_calculation_workflow_1, 2, 0, 1, 2)


        self.retranslateUi(workflow_1_panel)

        QMetaObject.connectSlotsByName(workflow_1_panel)
    # setupUi

    def retranslateUi(self, workflow_1_panel):
        workflow_1_panel.setWindowTitle(QCoreApplication.translate("workflow_1_panel", u"Workflow 1", None))
        self.pushButton_back_to_home_workflow_1.setText(QCoreApplication.translate("workflow_1_panel", u"Back to Home", None))
        self.pushButton_reset_workflow_1.setText(QCoreApplication.translate("workflow_1_panel", u"Reset", None))
        self.groupBox_threshold_euqation_workflow_1.setTitle(QCoreApplication.translate("workflow_1_panel", u"Threshold equation", None))
        self.pushButton_config_threshold_params_workflow_1.setText(QCoreApplication.translate("workflow_1_panel", u"Configure equation parameters", None))
        self.label_threshold_equation_option_workflow_1.setText(QCoreApplication.translate("workflow_1_panel", u"Option", None))
        self.pushButton_run_workflow_1.setText(QCoreApplication.translate("workflow_1_panel", u"Run", None))
        self.Feature_calculation_workflow_1.setTitle(QCoreApplication.translate("workflow_1_panel", u"Feature calculation", None))
        self.pushButton_set_parameters_workflow_1.setText(QCoreApplication.translate("workflow_1_panel", u"Set parameters", None))
    # retranslateUi

