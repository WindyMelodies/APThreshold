# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_datas_window.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_import_datas_widget(object):
    def setupUi(self, import_datas_widget):
        if not import_datas_widget.objectName():
            import_datas_widget.setObjectName(u"import_datas_widget")
        import_datas_widget.resize(297, 469)
        import_datas_widget.setAcceptDrops(True)
        self.verticalLayout_physiological_datas_widget = QVBoxLayout(import_datas_widget)
        self.verticalLayout_physiological_datas_widget.setSpacing(2)
        self.verticalLayout_physiological_datas_widget.setObjectName(u"verticalLayout_physiological_datas_widget")
        self.verticalLayout_physiological_datas_widget.setContentsMargins(3, 3, 3, 3)
        self.groupBox_import_abf_file = QGroupBox(import_datas_widget)
        self.groupBox_import_abf_file.setObjectName(u"groupBox_import_abf_file")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_import_abf_file.sizePolicy().hasHeightForWidth())
        self.groupBox_import_abf_file.setSizePolicy(sizePolicy)
        self.groupBox_import_abf_file.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.groupBox_import_abf_file)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_import_file = QLineEdit(self.groupBox_import_abf_file)
        self.lineEdit_import_file.setObjectName(u"lineEdit_import_file")
        self.lineEdit_import_file.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_import_file, 0, 1, 1, 1)

        self.pushButton_import_file = QPushButton(self.groupBox_import_abf_file)
        self.pushButton_import_file.setObjectName(u"pushButton_import_file")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_import_file.sizePolicy().hasHeightForWidth())
        self.pushButton_import_file.setSizePolicy(sizePolicy1)
        self.pushButton_import_file.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_import_file, 0, 0, 1, 1)

        self.spinBox_sample_rate = QSpinBox(self.groupBox_import_abf_file)
        self.spinBox_sample_rate.setObjectName(u"spinBox_sample_rate")
        self.spinBox_sample_rate.setMaximum(1000000000)

        self.gridLayout_2.addWidget(self.spinBox_sample_rate, 2, 1, 1, 1)

        self.label_unit_voltage = QLabel(self.groupBox_import_abf_file)
        self.label_unit_voltage.setObjectName(u"label_unit_voltage")

        self.gridLayout_2.addWidget(self.label_unit_voltage, 1, 0, 1, 1)

        self.label_sampling_rate = QLabel(self.groupBox_import_abf_file)
        self.label_sampling_rate.setObjectName(u"label_sampling_rate")
        sizePolicy.setHeightForWidth(self.label_sampling_rate.sizePolicy().hasHeightForWidth())
        self.label_sampling_rate.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_sampling_rate, 2, 0, 1, 1)

        self.comboBox_unit_voltage = QComboBox(self.groupBox_import_abf_file)
        self.comboBox_unit_voltage.addItem("")
        self.comboBox_unit_voltage.addItem("")
        self.comboBox_unit_voltage.setObjectName(u"comboBox_unit_voltage")

        self.gridLayout_2.addWidget(self.comboBox_unit_voltage, 1, 1, 1, 1)

        self.pushButton_other_file_run = QPushButton(self.groupBox_import_abf_file)
        self.pushButton_other_file_run.setObjectName(u"pushButton_other_file_run")

        self.gridLayout_2.addWidget(self.pushButton_other_file_run, 3, 0, 1, 2)


        self.verticalLayout_physiological_datas_widget.addWidget(self.groupBox_import_abf_file)

        self.groupBox_except_abf = QGroupBox(import_datas_widget)
        self.groupBox_except_abf.setObjectName(u"groupBox_except_abf")
        sizePolicy.setHeightForWidth(self.groupBox_except_abf.sizePolicy().hasHeightForWidth())
        self.groupBox_except_abf.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.groupBox_except_abf)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_spike_count = QLabel(self.groupBox_except_abf)
        self.label_spike_count.setObjectName(u"label_spike_count")

        self.gridLayout.addWidget(self.label_spike_count, 4, 0, 1, 1)

        self.lineEdit_spik_count = QLineEdit(self.groupBox_except_abf)
        self.lineEdit_spik_count.setObjectName(u"lineEdit_spik_count")
        self.lineEdit_spik_count.setStyleSheet(u"")
        self.lineEdit_spik_count.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_spik_count, 4, 1, 1, 1)

        self.label_maximal_ISI = QLabel(self.groupBox_except_abf)
        self.label_maximal_ISI.setObjectName(u"label_maximal_ISI")

        self.gridLayout.addWidget(self.label_maximal_ISI, 5, 0, 1, 1)

        self.lineEdit_maximal_ISI = QLineEdit(self.groupBox_except_abf)
        self.lineEdit_maximal_ISI.setObjectName(u"lineEdit_maximal_ISI")
        self.lineEdit_maximal_ISI.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_maximal_ISI, 5, 1, 1, 1)

        self.label_minimal_ISI = QLabel(self.groupBox_except_abf)
        self.label_minimal_ISI.setObjectName(u"label_minimal_ISI")

        self.gridLayout.addWidget(self.label_minimal_ISI, 6, 0, 1, 1)

        self.lineEdit_minimal_ISI = QLineEdit(self.groupBox_except_abf)
        self.lineEdit_minimal_ISI.setObjectName(u"lineEdit_minimal_ISI")
        self.lineEdit_minimal_ISI.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_minimal_ISI, 6, 1, 1, 1)


        self.verticalLayout_physiological_datas_widget.addWidget(self.groupBox_except_abf)


        self.retranslateUi(import_datas_widget)

        QMetaObject.connectSlotsByName(import_datas_widget)
    # setupUi

    def retranslateUi(self, import_datas_widget):
        import_datas_widget.setWindowTitle(QCoreApplication.translate("import_datas_widget", u"Form", None))
        self.groupBox_import_abf_file.setTitle(QCoreApplication.translate("import_datas_widget", u"Data import", None))
        self.pushButton_import_file.setText(QCoreApplication.translate("import_datas_widget", u"Select file", None))
        self.label_unit_voltage.setText(QCoreApplication.translate("import_datas_widget", u"Unit", None))
        self.label_sampling_rate.setText(QCoreApplication.translate("import_datas_widget", u"Sampling rate (kHz)", None))
        self.comboBox_unit_voltage.setItemText(0, QCoreApplication.translate("import_datas_widget", u"V", None))
        self.comboBox_unit_voltage.setItemText(1, QCoreApplication.translate("import_datas_widget", u"mV", None))

        self.pushButton_other_file_run.setText(QCoreApplication.translate("import_datas_widget", u"Ok", None))
        self.groupBox_except_abf.setTitle(QCoreApplication.translate("import_datas_widget", u"Spike info", None))
        self.label_spike_count.setText(QCoreApplication.translate("import_datas_widget", u"Spike count", None))
        self.label_maximal_ISI.setText(QCoreApplication.translate("import_datas_widget", u"Maximal ISI (ms)", None))
        self.label_minimal_ISI.setText(QCoreApplication.translate("import_datas_widget", u"Minimal ISI (ms)", None))
    # retranslateUi

