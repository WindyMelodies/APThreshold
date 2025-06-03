# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'extract_AP_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)
import apprcc_rc

class Ui_Form_extract_AP(object):
    def setupUi(self, Form_extract_AP):
        if not Form_extract_AP.objectName():
            Form_extract_AP.setObjectName(u"Form_extract_AP")
        Form_extract_AP.resize(335, 89)
        Form_extract_AP.setFocusPolicy(Qt.StrongFocus)
        icon = QIcon()
        icon.addFile(u":/APThrehold_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_extract_AP.setWindowIcon(icon)
        Form_extract_AP.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Form_extract_AP)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_canel_extract_ap = QPushButton(Form_extract_AP)
        self.pushButton_canel_extract_ap.setObjectName(u"pushButton_canel_extract_ap")
        self.pushButton_canel_extract_ap.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.pushButton_canel_extract_ap, 2, 1, 1, 1, Qt.AlignHCenter)

        self.pushButton_save_extract_ap = QPushButton(Form_extract_AP)
        self.pushButton_save_extract_ap.setObjectName(u"pushButton_save_extract_ap")
        self.pushButton_save_extract_ap.setFocusPolicy(Qt.NoFocus)
        self.pushButton_save_extract_ap.setAutoDefault(False)

        self.gridLayout.addWidget(self.pushButton_save_extract_ap, 2, 0, 1, 1, Qt.AlignHCenter)

        self.doubleSpinBox_stop = QDoubleSpinBox(Form_extract_AP)
        self.doubleSpinBox_stop.setObjectName(u"doubleSpinBox_stop")
        self.doubleSpinBox_stop.setFocusPolicy(Qt.StrongFocus)

        self.gridLayout.addWidget(self.doubleSpinBox_stop, 1, 1, 1, 1)

        self.label_stop = QLabel(Form_extract_AP)
        self.label_stop.setObjectName(u"label_stop")

        self.gridLayout.addWidget(self.label_stop, 0, 1, 1, 1)

        self.label_start = QLabel(Form_extract_AP)
        self.label_start.setObjectName(u"label_start")

        self.gridLayout.addWidget(self.label_start, 0, 0, 1, 1)

        self.doubleSpinBox_start = QDoubleSpinBox(Form_extract_AP)
        self.doubleSpinBox_start.setObjectName(u"doubleSpinBox_start")
        self.doubleSpinBox_start.setFocusPolicy(Qt.StrongFocus)

        self.gridLayout.addWidget(self.doubleSpinBox_start, 1, 0, 1, 1)


        self.retranslateUi(Form_extract_AP)

        QMetaObject.connectSlotsByName(Form_extract_AP)
    # setupUi

    def retranslateUi(self, Form_extract_AP):
        Form_extract_AP.setWindowTitle(QCoreApplication.translate("Form_extract_AP", u"Form", None))
        self.pushButton_canel_extract_ap.setText(QCoreApplication.translate("Form_extract_AP", u"Canel", None))
#if QT_CONFIG(shortcut)
        self.pushButton_canel_extract_ap.setShortcut(QCoreApplication.translate("Form_extract_AP", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_save_extract_ap.setText(QCoreApplication.translate("Form_extract_AP", u"Save", None))
#if QT_CONFIG(shortcut)
        self.pushButton_save_extract_ap.setShortcut(QCoreApplication.translate("Form_extract_AP", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_stop.setText(QCoreApplication.translate("Form_extract_AP", u"<html><head/><body><p align=\"center\">Stop(ms)</p></body></html>", None))
        self.label_start.setText(QCoreApplication.translate("Form_extract_AP", u"<html><head/><body><p align=\"center\">Start(ms)</p></body></html>", None))
    # retranslateUi

