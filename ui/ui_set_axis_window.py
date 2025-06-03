# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_axis_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import apprcc_rc

class Ui_widget_Axis_AP(object):
    def setupUi(self, widget_Axis_AP):
        if not widget_Axis_AP.objectName():
            widget_Axis_AP.setObjectName(u"widget_Axis_AP")
        widget_Axis_AP.resize(362, 224)
        icon = QIcon()
        icon.addFile(u":/APThrehold_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        widget_Axis_AP.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(widget_Axis_AP)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_x = QVBoxLayout()
        self.verticalLayout_x.setObjectName(u"verticalLayout_x")
        self.label_X_axis = QLabel(widget_Axis_AP)
        self.label_X_axis.setObjectName(u"label_X_axis")

        self.verticalLayout_x.addWidget(self.label_X_axis)

        self.horizontalLayout_x = QHBoxLayout()
        self.horizontalLayout_x.setObjectName(u"horizontalLayout_x")
        self.comboBox_X_axis_main = QComboBox(widget_Axis_AP)
        self.comboBox_X_axis_main.setObjectName(u"comboBox_X_axis_main")

        self.horizontalLayout_x.addWidget(self.comboBox_X_axis_main)

        self.comboBox_X_axis_sub = QComboBox(widget_Axis_AP)
        self.comboBox_X_axis_sub.setObjectName(u"comboBox_X_axis_sub")

        self.horizontalLayout_x.addWidget(self.comboBox_X_axis_sub)


        self.verticalLayout_x.addLayout(self.horizontalLayout_x)


        self.verticalLayout_3.addLayout(self.verticalLayout_x)

        self.verticalLayout_y = QVBoxLayout()
        self.verticalLayout_y.setObjectName(u"verticalLayout_y")
        self.label_Y_axis = QLabel(widget_Axis_AP)
        self.label_Y_axis.setObjectName(u"label_Y_axis")

        self.verticalLayout_y.addWidget(self.label_Y_axis)

        self.horizontalLayout_y = QHBoxLayout()
        self.horizontalLayout_y.setObjectName(u"horizontalLayout_y")
        self.comboBox_Y_axis_main = QComboBox(widget_Axis_AP)
        self.comboBox_Y_axis_main.setObjectName(u"comboBox_Y_axis_main")

        self.horizontalLayout_y.addWidget(self.comboBox_Y_axis_main)

        self.comboBox_Y_axis_sub = QComboBox(widget_Axis_AP)
        self.comboBox_Y_axis_sub.setObjectName(u"comboBox_Y_axis_sub")

        self.horizontalLayout_y.addWidget(self.comboBox_Y_axis_sub)


        self.verticalLayout_y.addLayout(self.horizontalLayout_y)


        self.verticalLayout_3.addLayout(self.verticalLayout_y)

        self.verticalLayout_label = QVBoxLayout()
        self.verticalLayout_label.setObjectName(u"verticalLayout_label")
        self.label_label = QLabel(widget_Axis_AP)
        self.label_label.setObjectName(u"label_label")

        self.verticalLayout_label.addWidget(self.label_label)

        self.lineEdit_label = QLineEdit(widget_Axis_AP)
        self.lineEdit_label.setObjectName(u"lineEdit_label")

        self.verticalLayout_label.addWidget(self.lineEdit_label)


        self.verticalLayout_3.addLayout(self.verticalLayout_label)

        self.horizontalLayout_button = QHBoxLayout()
        self.horizontalLayout_button.setObjectName(u"horizontalLayout_button")
        self.pushButton_Save = QPushButton(widget_Axis_AP)
        self.pushButton_Save.setObjectName(u"pushButton_Save")

        self.horizontalLayout_button.addWidget(self.pushButton_Save)

        self.pushButton_Cancel = QPushButton(widget_Axis_AP)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")

        self.horizontalLayout_button.addWidget(self.pushButton_Cancel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_button)


        self.retranslateUi(widget_Axis_AP)

        QMetaObject.connectSlotsByName(widget_Axis_AP)
    # setupUi

    def retranslateUi(self, widget_Axis_AP):
        widget_Axis_AP.setWindowTitle(QCoreApplication.translate("widget_Axis_AP", u"X_axis,Y_axis", None))
        self.label_X_axis.setText(QCoreApplication.translate("widget_Axis_AP", u"<html><head/><body><p align=\"center\">X_axis</p></body></html>", None))
        self.label_Y_axis.setText(QCoreApplication.translate("widget_Axis_AP", u"<html><head/><body><p align=\"center\">Y_axis</p></body></html>", None))
        self.label_label.setText(QCoreApplication.translate("widget_Axis_AP", u"<html><head/><body><p align=\"center\">Label</p></body></html>", None))
        self.pushButton_Save.setText(QCoreApplication.translate("widget_Axis_AP", u"Save", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("widget_Axis_AP", u"Cancel", None))
    # retranslateUi

