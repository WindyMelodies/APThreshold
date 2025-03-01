# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_axis_window_Vth.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)
import ui.apprcc_rc

class Ui_widget_Axis_Vth(object):
    def setupUi(self, widget_Axis_Vth):
        if not widget_Axis_Vth.objectName():
            widget_Axis_Vth.setObjectName(u"widget_Axis_Vth")
        widget_Axis_Vth.resize(468, 247)
        icon = QIcon()
        icon.addFile(u":/APThrehold_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        widget_Axis_Vth.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(widget_Axis_Vth)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_x = QVBoxLayout()
        self.verticalLayout_x.setObjectName(u"verticalLayout_x")
        self.label_X_axis = QLabel(widget_Axis_Vth)
        self.label_X_axis.setObjectName(u"label_X_axis")

        self.verticalLayout_x.addWidget(self.label_X_axis)

        self.horizontalLayout_x = QHBoxLayout()
        self.horizontalLayout_x.setObjectName(u"horizontalLayout_x")
        self.comboBox_X_axis = QComboBox(widget_Axis_Vth)
        self.comboBox_X_axis.setObjectName(u"comboBox_X_axis")

        self.horizontalLayout_x.addWidget(self.comboBox_X_axis)

        self.comboBox_X_axis_main = QComboBox(widget_Axis_Vth)
        self.comboBox_X_axis_main.setObjectName(u"comboBox_X_axis_main")

        self.horizontalLayout_x.addWidget(self.comboBox_X_axis_main)

        self.comboBox_X_axis_sub = QComboBox(widget_Axis_Vth)
        self.comboBox_X_axis_sub.setObjectName(u"comboBox_X_axis_sub")

        self.horizontalLayout_x.addWidget(self.comboBox_X_axis_sub)


        self.verticalLayout_x.addLayout(self.horizontalLayout_x)


        self.gridLayout_2.addLayout(self.verticalLayout_x, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_label = QLineEdit(widget_Axis_Vth)
        self.lineEdit_label.setObjectName(u"lineEdit_label")

        self.gridLayout.addWidget(self.lineEdit_label, 1, 0, 1, 1)

        self.label_label = QLabel(widget_Axis_Vth)
        self.label_label.setObjectName(u"label_label")

        self.gridLayout.addWidget(self.label_label, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.verticalLayout_y = QVBoxLayout()
        self.verticalLayout_y.setObjectName(u"verticalLayout_y")
        self.label_Y_axis = QLabel(widget_Axis_Vth)
        self.label_Y_axis.setObjectName(u"label_Y_axis")

        self.verticalLayout_y.addWidget(self.label_Y_axis)

        self.horizontalLayout_y = QHBoxLayout()
        self.horizontalLayout_y.setObjectName(u"horizontalLayout_y")
        self.comboBox_Y_axis = QComboBox(widget_Axis_Vth)
        self.comboBox_Y_axis.setObjectName(u"comboBox_Y_axis")

        self.horizontalLayout_y.addWidget(self.comboBox_Y_axis)

        self.comboBox_Y_axis_main = QComboBox(widget_Axis_Vth)
        self.comboBox_Y_axis_main.setObjectName(u"comboBox_Y_axis_main")

        self.horizontalLayout_y.addWidget(self.comboBox_Y_axis_main)

        self.comboBox_Y_axis_sub = QComboBox(widget_Axis_Vth)
        self.comboBox_Y_axis_sub.setObjectName(u"comboBox_Y_axis_sub")

        self.horizontalLayout_y.addWidget(self.comboBox_Y_axis_sub)


        self.verticalLayout_y.addLayout(self.horizontalLayout_y)


        self.gridLayout_2.addLayout(self.verticalLayout_y, 1, 0, 1, 1)

        self.horizontalLayout_button = QHBoxLayout()
        self.horizontalLayout_button.setObjectName(u"horizontalLayout_button")
        self.pushButton_Save = QPushButton(widget_Axis_Vth)
        self.pushButton_Save.setObjectName(u"pushButton_Save")

        self.horizontalLayout_button.addWidget(self.pushButton_Save)

        self.pushButton_Cancel = QPushButton(widget_Axis_Vth)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")

        self.horizontalLayout_button.addWidget(self.pushButton_Cancel)


        self.gridLayout_2.addLayout(self.horizontalLayout_button, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_linear_fitting = QRadioButton(widget_Axis_Vth)
        self.radioButton_linear_fitting.setObjectName(u"radioButton_linear_fitting")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_linear_fitting.sizePolicy().hasHeightForWidth())
        self.radioButton_linear_fitting.setSizePolicy(sizePolicy)
        self.radioButton_linear_fitting.setAutoExclusive(False)

        self.horizontalLayout.addWidget(self.radioButton_linear_fitting)


        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)


        self.retranslateUi(widget_Axis_Vth)

        QMetaObject.connectSlotsByName(widget_Axis_Vth)
    # setupUi

    def retranslateUi(self, widget_Axis_Vth):
        widget_Axis_Vth.setWindowTitle(QCoreApplication.translate("widget_Axis_Vth", u"X_axis,Y_axis", None))
        self.label_X_axis.setText(QCoreApplication.translate("widget_Axis_Vth", u"<html><head/><body><p align=\"center\">X_axis</p></body></html>", None))
        self.label_label.setText(QCoreApplication.translate("widget_Axis_Vth", u"<html><head/><body><p align=\"center\">Label</p></body></html>", None))
        self.label_Y_axis.setText(QCoreApplication.translate("widget_Axis_Vth", u"<html><head/><body><p align=\"center\">Y_axis</p></body></html>", None))
        self.pushButton_Save.setText(QCoreApplication.translate("widget_Axis_Vth", u"Save", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("widget_Axis_Vth", u"Cancel", None))
        self.radioButton_linear_fitting.setText(QCoreApplication.translate("widget_Axis_Vth", u"Linear fitting", None))
    # retranslateUi

