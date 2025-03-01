# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_fig_window_Vth.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QToolBox,
    QWidget)
import ui.apprcc_rc

class Ui_setwidget_spike_threshold(object):
    def setupUi(self, setwidget_spike_threshold):
        if not setwidget_spike_threshold.objectName():
            setwidget_spike_threshold.setObjectName(u"setwidget_spike_threshold")
        setwidget_spike_threshold.resize(697, 433)
        icon = QIcon()
        icon.addFile(u":/APThrehold_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        setwidget_spike_threshold.setWindowIcon(icon)
        setwidget_spike_threshold.setStyleSheet(u"QWidget#setwidget_spike_threshold {background-color: #E4F4FE}")
        self.gridLayout_setwidget_get_aps = QGridLayout(setwidget_spike_threshold)
        self.gridLayout_setwidget_get_aps.setObjectName(u"gridLayout_setwidget_get_aps")
        self.gridLayout_setwidget_get_aps.setContentsMargins(0, 0, 0, 0)
        self.pushButton_apply = QPushButton(setwidget_spike_threshold)
        self.pushButton_apply.setObjectName(u"pushButton_apply")

        self.gridLayout_setwidget_get_aps.addWidget(self.pushButton_apply, 0, 0, 1, 1)

        self.pushButton_reset = QPushButton(setwidget_spike_threshold)
        self.pushButton_reset.setObjectName(u"pushButton_reset")

        self.gridLayout_setwidget_get_aps.addWidget(self.pushButton_reset, 0, 1, 1, 1)

        self.toolBox_plot_set = QToolBox(setwidget_spike_threshold)
        self.toolBox_plot_set.setObjectName(u"toolBox_plot_set")
        self.toolBox_plot_set.setStyleSheet(u"QToolBoxButton {min-height: 25px;}\n"
"QToolBox::tab {\n"
"    background-color: #414656;  /* Tab background color */\n"
"    color: white;  /* Tab text color */\n"
"	min-height: 30px;\n"
"    padding: 5px;  /* Padding around the text */\n"
"    height: 40px;  /* Set the minimum height of the tab */\n"
"	\n"
"}\n"
"")
        self.toolBox_plot_set.setLineWidth(1)
        self.page_figure_1_1 = QWidget()
        self.page_figure_1_1.setObjectName(u"page_figure_1_1")
        self.page_figure_1_1.setGeometry(QRect(0, 0, 697, 280))
        self.gridLayout_page_figure_1_1 = QGridLayout(self.page_figure_1_1)
        self.gridLayout_page_figure_1_1.setObjectName(u"gridLayout_page_figure_1_1")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_add_plot_figure_1_1 = QPushButton(self.page_figure_1_1)
        self.pushButton_add_plot_figure_1_1.setObjectName(u"pushButton_add_plot_figure_1_1")

        self.horizontalLayout.addWidget(self.pushButton_add_plot_figure_1_1)

        self.pushButton_clear_figure_1_1 = QPushButton(self.page_figure_1_1)
        self.pushButton_clear_figure_1_1.setObjectName(u"pushButton_clear_figure_1_1")
        self.pushButton_clear_figure_1_1.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_clear_figure_1_1)


        self.gridLayout_page_figure_1_1.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.scrollArea_figure_1_1 = QScrollArea(self.page_figure_1_1)
        self.scrollArea_figure_1_1.setObjectName(u"scrollArea_figure_1_1")
        self.scrollArea_figure_1_1.setWidgetResizable(True)
        self.scrollAreaWidgetContents_figure_1_1 = QWidget()
        self.scrollAreaWidgetContents_figure_1_1.setObjectName(u"scrollAreaWidgetContents_figure_1_1")
        self.scrollAreaWidgetContents_figure_1_1.setGeometry(QRect(0, 0, 677, 202))
        self.gridLayout_figure_1_1 = QGridLayout(self.scrollAreaWidgetContents_figure_1_1)
        self.gridLayout_figure_1_1.setObjectName(u"gridLayout_figure_1_1")
        self.scrollArea_figure_1_1.setWidget(self.scrollAreaWidgetContents_figure_1_1)

        self.gridLayout_page_figure_1_1.addWidget(self.scrollArea_figure_1_1, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radioButton_threshold_points_figure_1_1 = QRadioButton(self.page_figure_1_1)
        self.radioButton_threshold_points_figure_1_1.setObjectName(u"radioButton_threshold_points_figure_1_1")
        self.radioButton_threshold_points_figure_1_1.setAutoExclusive(False)

        self.horizontalLayout_5.addWidget(self.radioButton_threshold_points_figure_1_1)

        self.radioButton_threshold_range_figure_1_1 = QRadioButton(self.page_figure_1_1)
        self.radioButton_threshold_range_figure_1_1.setObjectName(u"radioButton_threshold_range_figure_1_1")
        self.radioButton_threshold_range_figure_1_1.setAutoExclusive(False)

        self.horizontalLayout_5.addWidget(self.radioButton_threshold_range_figure_1_1)


        self.gridLayout_page_figure_1_1.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.toolBox_plot_set.addItem(self.page_figure_1_1, u"Figure in (1, 1)")
        self.page_figure_1_2 = QWidget()
        self.page_figure_1_2.setObjectName(u"page_figure_1_2")
        self.page_figure_1_2.setGeometry(QRect(0, 0, 697, 280))
        self.gridLayout_page_figure_1_2 = QGridLayout(self.page_figure_1_2)
        self.gridLayout_page_figure_1_2.setObjectName(u"gridLayout_page_figure_1_2")
        self.scrollArea_figure_1_2 = QScrollArea(self.page_figure_1_2)
        self.scrollArea_figure_1_2.setObjectName(u"scrollArea_figure_1_2")
        self.scrollArea_figure_1_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_figure_1_2 = QWidget()
        self.scrollAreaWidgetContents_figure_1_2.setObjectName(u"scrollAreaWidgetContents_figure_1_2")
        self.scrollAreaWidgetContents_figure_1_2.setGeometry(QRect(0, 0, 677, 202))
        self.gridLayout_figure_1_2 = QGridLayout(self.scrollAreaWidgetContents_figure_1_2)
        self.gridLayout_figure_1_2.setObjectName(u"gridLayout_figure_1_2")
        self.scrollArea_figure_1_2.setWidget(self.scrollAreaWidgetContents_figure_1_2)

        self.gridLayout_page_figure_1_2.addWidget(self.scrollArea_figure_1_2, 2, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton_threshold_points_figure_1_2 = QRadioButton(self.page_figure_1_2)
        self.radioButton_threshold_points_figure_1_2.setObjectName(u"radioButton_threshold_points_figure_1_2")
        self.radioButton_threshold_points_figure_1_2.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.radioButton_threshold_points_figure_1_2)

        self.radioButton_threshold_range_figure_1_2 = QRadioButton(self.page_figure_1_2)
        self.radioButton_threshold_range_figure_1_2.setObjectName(u"radioButton_threshold_range_figure_1_2")
        self.radioButton_threshold_range_figure_1_2.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.radioButton_threshold_range_figure_1_2)


        self.gridLayout_page_figure_1_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_add_plot_figure_1_2 = QPushButton(self.page_figure_1_2)
        self.pushButton_add_plot_figure_1_2.setObjectName(u"pushButton_add_plot_figure_1_2")

        self.horizontalLayout_2.addWidget(self.pushButton_add_plot_figure_1_2)

        self.pushButton_clear_figure_1_2 = QPushButton(self.page_figure_1_2)
        self.pushButton_clear_figure_1_2.setObjectName(u"pushButton_clear_figure_1_2")

        self.horizontalLayout_2.addWidget(self.pushButton_clear_figure_1_2)


        self.gridLayout_page_figure_1_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.toolBox_plot_set.addItem(self.page_figure_1_2, u"Figure in (1, 2)")
        self.page_figure_2_1 = QWidget()
        self.page_figure_2_1.setObjectName(u"page_figure_2_1")
        self.page_figure_2_1.setGeometry(QRect(0, 0, 697, 280))
        self.gridLayout_page_figure_2_1 = QGridLayout(self.page_figure_2_1)
        self.gridLayout_page_figure_2_1.setObjectName(u"gridLayout_page_figure_2_1")
        self.scrollArea_figure_2_1 = QScrollArea(self.page_figure_2_1)
        self.scrollArea_figure_2_1.setObjectName(u"scrollArea_figure_2_1")
        self.scrollArea_figure_2_1.setWidgetResizable(True)
        self.scrollAreaWidgetContents_figure_2_1 = QWidget()
        self.scrollAreaWidgetContents_figure_2_1.setObjectName(u"scrollAreaWidgetContents_figure_2_1")
        self.scrollAreaWidgetContents_figure_2_1.setGeometry(QRect(0, 0, 677, 202))
        self.gridLayout_figure_2_1 = QGridLayout(self.scrollAreaWidgetContents_figure_2_1)
        self.gridLayout_figure_2_1.setObjectName(u"gridLayout_figure_2_1")
        self.scrollArea_figure_2_1.setWidget(self.scrollAreaWidgetContents_figure_2_1)

        self.gridLayout_page_figure_2_1.addWidget(self.scrollArea_figure_2_1, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_add_plot_figure_2_1 = QPushButton(self.page_figure_2_1)
        self.pushButton_add_plot_figure_2_1.setObjectName(u"pushButton_add_plot_figure_2_1")

        self.horizontalLayout_3.addWidget(self.pushButton_add_plot_figure_2_1)

        self.pushButton_clear_figure_2_1 = QPushButton(self.page_figure_2_1)
        self.pushButton_clear_figure_2_1.setObjectName(u"pushButton_clear_figure_2_1")

        self.horizontalLayout_3.addWidget(self.pushButton_clear_figure_2_1)


        self.gridLayout_page_figure_2_1.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.radioButton_threshold_points_figure_2_1 = QRadioButton(self.page_figure_2_1)
        self.radioButton_threshold_points_figure_2_1.setObjectName(u"radioButton_threshold_points_figure_2_1")
        self.radioButton_threshold_points_figure_2_1.setAutoExclusive(False)

        self.horizontalLayout_7.addWidget(self.radioButton_threshold_points_figure_2_1)

        self.radioButton_threshold_range_figure_2_1 = QRadioButton(self.page_figure_2_1)
        self.radioButton_threshold_range_figure_2_1.setObjectName(u"radioButton_threshold_range_figure_2_1")
        self.radioButton_threshold_range_figure_2_1.setAutoExclusive(False)

        self.horizontalLayout_7.addWidget(self.radioButton_threshold_range_figure_2_1)


        self.gridLayout_page_figure_2_1.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.toolBox_plot_set.addItem(self.page_figure_2_1, u"Figure in (2, 1)")
        self.page_figure_2_2 = QWidget()
        self.page_figure_2_2.setObjectName(u"page_figure_2_2")
        self.page_figure_2_2.setGeometry(QRect(0, 0, 697, 280))
        self.gridLayout_page_figure_2_2 = QGridLayout(self.page_figure_2_2)
        self.gridLayout_page_figure_2_2.setObjectName(u"gridLayout_page_figure_2_2")
        self.scrollArea_figure_2_2 = QScrollArea(self.page_figure_2_2)
        self.scrollArea_figure_2_2.setObjectName(u"scrollArea_figure_2_2")
        self.scrollArea_figure_2_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_figure_2_2 = QWidget()
        self.scrollAreaWidgetContents_figure_2_2.setObjectName(u"scrollAreaWidgetContents_figure_2_2")
        self.scrollAreaWidgetContents_figure_2_2.setGeometry(QRect(0, 0, 677, 202))
        self.gridLayout_figure_2_2 = QGridLayout(self.scrollAreaWidgetContents_figure_2_2)
        self.gridLayout_figure_2_2.setObjectName(u"gridLayout_figure_2_2")
        self.scrollArea_figure_2_2.setWidget(self.scrollAreaWidgetContents_figure_2_2)

        self.gridLayout_page_figure_2_2.addWidget(self.scrollArea_figure_2_2, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_add_plot_figure_2_2 = QPushButton(self.page_figure_2_2)
        self.pushButton_add_plot_figure_2_2.setObjectName(u"pushButton_add_plot_figure_2_2")

        self.horizontalLayout_4.addWidget(self.pushButton_add_plot_figure_2_2)

        self.pushButton_clear_figure_2_2 = QPushButton(self.page_figure_2_2)
        self.pushButton_clear_figure_2_2.setObjectName(u"pushButton_clear_figure_2_2")

        self.horizontalLayout_4.addWidget(self.pushButton_clear_figure_2_2)


        self.gridLayout_page_figure_2_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.radioButton_threshold_points_figure_2_2 = QRadioButton(self.page_figure_2_2)
        self.radioButton_threshold_points_figure_2_2.setObjectName(u"radioButton_threshold_points_figure_2_2")
        self.radioButton_threshold_points_figure_2_2.setAutoExclusive(False)

        self.horizontalLayout_8.addWidget(self.radioButton_threshold_points_figure_2_2)

        self.radioButton_threshold_range_figure_2_2 = QRadioButton(self.page_figure_2_2)
        self.radioButton_threshold_range_figure_2_2.setObjectName(u"radioButton_threshold_range_figure_2_2")
        self.radioButton_threshold_range_figure_2_2.setAutoExclusive(False)

        self.horizontalLayout_8.addWidget(self.radioButton_threshold_range_figure_2_2)


        self.gridLayout_page_figure_2_2.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.toolBox_plot_set.addItem(self.page_figure_2_2, u"Figure in (2, 2)")

        self.gridLayout_setwidget_get_aps.addWidget(self.toolBox_plot_set, 1, 0, 1, 2)


        self.retranslateUi(setwidget_spike_threshold)

        self.toolBox_plot_set.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(setwidget_spike_threshold)
    # setupUi

    def retranslateUi(self, setwidget_spike_threshold):
        setwidget_spike_threshold.setWindowTitle(QCoreApplication.translate("setwidget_spike_threshold", u"Set axes", None))
        self.pushButton_apply.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Apply", None))
        self.pushButton_reset.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Reset", None))
        self.pushButton_add_plot_figure_1_1.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Add plot", None))
        self.pushButton_clear_figure_1_1.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Clear", None))
        self.radioButton_threshold_points_figure_1_1.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Mark the threshold points", None))
        self.radioButton_threshold_range_figure_1_1.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Mark the threshold region", None))
        self.toolBox_plot_set.setItemText(self.toolBox_plot_set.indexOf(self.page_figure_1_1), QCoreApplication.translate("setwidget_spike_threshold", u"Figure in (1, 1)", None))
        self.radioButton_threshold_points_figure_1_2.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Mark the threshold points", None))
        self.radioButton_threshold_range_figure_1_2.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Mark the threshold region", None))
        self.pushButton_add_plot_figure_1_2.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Add plot", None))
        self.pushButton_clear_figure_1_2.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Clear", None))
        self.toolBox_plot_set.setItemText(self.toolBox_plot_set.indexOf(self.page_figure_1_2), QCoreApplication.translate("setwidget_spike_threshold", u"Figure in (1, 2)", None))
        self.pushButton_add_plot_figure_2_1.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Add plot", None))
        self.pushButton_clear_figure_2_1.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Clear", None))
        self.radioButton_threshold_points_figure_2_1.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Mark the threshold points", None))
        self.radioButton_threshold_range_figure_2_1.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Mark the threshold region", None))
        self.toolBox_plot_set.setItemText(self.toolBox_plot_set.indexOf(self.page_figure_2_1), QCoreApplication.translate("setwidget_spike_threshold", u"Figure in (2, 1)", None))
        self.pushButton_add_plot_figure_2_2.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Add plot", None))
        self.pushButton_clear_figure_2_2.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Clear", None))
        self.radioButton_threshold_points_figure_2_2.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Mark the threshold points", None))
        self.radioButton_threshold_range_figure_2_2.setText(QCoreApplication.translate("setwidget_spike_threshold", u"Mark the threshold region", None))
        self.toolBox_plot_set.setItemText(self.toolBox_plot_set.indexOf(self.page_figure_2_2), QCoreApplication.translate("setwidget_spike_threshold", u"Figure in (2, 2)", None))
    # retranslateUi

