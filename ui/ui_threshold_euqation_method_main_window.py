# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'threshold_euqation_method_main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_threshold_euqation_method_main_window(object):
    def setupUi(self, threshold_euqation_method_main_window):
        if not threshold_euqation_method_main_window.objectName():
            threshold_euqation_method_main_window.setObjectName(u"threshold_euqation_method_main_window")
        threshold_euqation_method_main_window.resize(293, 454)
        self.gridLayout_threshold_equation_method = QGridLayout(threshold_euqation_method_main_window)
        self.gridLayout_threshold_equation_method.setObjectName(u"gridLayout_threshold_equation_method")
        self.gridLayout_threshold_equation_method.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(threshold_euqation_method_main_window)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textEdit_2 = QTextEdit(self.groupBox_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit_2)

        self.pushButton_workflow_2 = QPushButton(self.groupBox_2)
        self.pushButton_workflow_2.setObjectName(u"pushButton_workflow_2")

        self.verticalLayout_2.addWidget(self.pushButton_workflow_2)


        self.gridLayout_threshold_equation_method.addWidget(self.groupBox_2, 2, 1, 1, 1)

        self.groupBox = QGroupBox(threshold_euqation_method_main_window)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.pushButton_workflow_1 = QPushButton(self.groupBox)
        self.pushButton_workflow_1.setObjectName(u"pushButton_workflow_1")

        self.verticalLayout.addWidget(self.pushButton_workflow_1)


        self.gridLayout_threshold_equation_method.addWidget(self.groupBox, 1, 1, 1, 1)

        self.textEdit_3 = QTextEdit(threshold_euqation_method_main_window)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMaximumSize(QSize(16777215, 90))
        self.textEdit_3.setReadOnly(True)

        self.gridLayout_threshold_equation_method.addWidget(self.textEdit_3, 0, 1, 1, 1)


        self.retranslateUi(threshold_euqation_method_main_window)

        QMetaObject.connectSlotsByName(threshold_euqation_method_main_window)
    # setupUi

    def retranslateUi(self, threshold_euqation_method_main_window):
        threshold_euqation_method_main_window.setWindowTitle(QCoreApplication.translate("threshold_euqation_method_main_window", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("threshold_euqation_method_main_window", u"Workflow 2", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("threshold_euqation_method_main_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Description: Spike threshold prediction using Integrate-and-Fire model</p></body></html>", None))
        self.pushButton_workflow_2.setText(QCoreApplication.translate("threshold_euqation_method_main_window", u"Start", None))
        self.groupBox.setTitle(QCoreApplication.translate("threshold_euqation_method_main_window", u"Workflow 1", None))
        self.textEdit.setHtml(QCoreApplication.translate("threshold_euqation_method_main_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Description: Spike threshold prediction based on membrane voltage</p></body></html>", None))
        self.pushButton_workflow_1.setText(QCoreApplication.translate("threshold_euqation_method_main_window", u"Start", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("threshold_euqation_method_main_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#000000;\">Choose a defined workflow to predict threshold voltage</span></p></body></html>", None))
    # retranslateUi

