# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sava_result_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTreeView, QVBoxLayout, QWidget)

class Ui_save_results(object):
    def setupUi(self, save_results):
        if not save_results.objectName():
            save_results.setObjectName(u"save_results")
        save_results.resize(400, 300)
        self.verticalLayout_save_results = QVBoxLayout(save_results)
        self.verticalLayout_save_results.setObjectName(u"verticalLayout_save_results")
        self.lineEdit_search = QLineEdit(save_results)
        self.lineEdit_search.setObjectName(u"lineEdit_search")

        self.verticalLayout_save_results.addWidget(self.lineEdit_search)

        self.treeView = QTreeView(save_results)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout_save_results.addWidget(self.treeView)

        self.widget_save_results_1 = QWidget(save_results)
        self.widget_save_results_1.setObjectName(u"widget_save_results_1")
        self.gridLayout_save_results_1action_potential = QGridLayout(self.widget_save_results_1)
        self.gridLayout_save_results_1action_potential.setObjectName(u"gridLayout_save_results_1action_potential")
        self.pushButton_refresh = QPushButton(self.widget_save_results_1)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")

        self.gridLayout_save_results_1action_potential.addWidget(self.pushButton_refresh, 1, 0, 1, 1)

        self.label_save_to = QLabel(self.widget_save_results_1)
        self.label_save_to.setObjectName(u"label_save_to")
        self.label_save_to.setAlignment(Qt.AlignCenter)

        self.gridLayout_save_results_1action_potential.addWidget(self.label_save_to, 0, 0, 1, 1)

        self.comboBox_file_format = QComboBox(self.widget_save_results_1)
        self.comboBox_file_format.addItem("")
        self.comboBox_file_format.addItem("")
        self.comboBox_file_format.setObjectName(u"comboBox_file_format")

        self.gridLayout_save_results_1action_potential.addWidget(self.comboBox_file_format, 0, 1, 1, 1)

        self.pushButton_save_selected = QPushButton(self.widget_save_results_1)
        self.pushButton_save_selected.setObjectName(u"pushButton_save_selected")

        self.gridLayout_save_results_1action_potential.addWidget(self.pushButton_save_selected, 1, 1, 1, 1)

        self.gridLayout_save_results_1action_potential.setColumnStretch(0, 1)
        self.gridLayout_save_results_1action_potential.setColumnStretch(1, 2)

        self.verticalLayout_save_results.addWidget(self.widget_save_results_1)


        self.retranslateUi(save_results)

        QMetaObject.connectSlotsByName(save_results)
    # setupUi

    def retranslateUi(self, save_results):
        save_results.setWindowTitle(QCoreApplication.translate("save_results", u"Form", None))
        self.lineEdit_search.setText("")
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("save_results", u"Search...", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("save_results", u"Refresh", None))
        self.label_save_to.setText(QCoreApplication.translate("save_results", u"Save to", None))
        self.comboBox_file_format.setItemText(0, QCoreApplication.translate("save_results", u"txt", None))
        self.comboBox_file_format.setItemText(1, QCoreApplication.translate("save_results", u"dat", None))

        self.pushButton_save_selected.setText(QCoreApplication.translate("save_results", u"Save selected", None))
    # retranslateUi

