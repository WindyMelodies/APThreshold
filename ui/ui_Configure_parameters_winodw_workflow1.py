# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Configure_parameters_winodw_workflow1.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QGroupBox, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)
import apprcc_rc

class Ui_ConfigureEquationParametersWindow(object):
    def setupUi(self, ConfigureEquationParametersWindow):
        if not ConfigureEquationParametersWindow.objectName():
            ConfigureEquationParametersWindow.setObjectName(u"ConfigureEquationParametersWindow")
        ConfigureEquationParametersWindow.resize(616, 596)
        icon = QIcon()
        icon.addFile(u":/APThrehold_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        ConfigureEquationParametersWindow.setWindowIcon(icon)
        ConfigureEquationParametersWindow.setStyleSheet(u"\n"
"QGroupBox {\n"
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
        self.gridLayout = QGridLayout(ConfigureEquationParametersWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.pushButton_OK = QPushButton(ConfigureEquationParametersWindow)
        self.pushButton_OK.setObjectName(u"pushButton_OK")

        self.gridLayout.addWidget(self.pushButton_OK, 3, 0, 1, 1)

        self.pushButton_canel = QPushButton(ConfigureEquationParametersWindow)
        self.pushButton_canel.setObjectName(u"pushButton_canel")

        self.gridLayout.addWidget(self.pushButton_canel, 3, 1, 1, 1)

        self.groupBox_3 = QGroupBox(ConfigureEquationParametersWindow)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)

        self.plainTextEdit_optimization = QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit_optimization.setObjectName(u"plainTextEdit_optimization")
        self.plainTextEdit_optimization.setReadOnly(True)

        self.gridLayout_2.addWidget(self.plainTextEdit_optimization, 2, 0, 1, 2)

        self.comboBox_algorithm = QComboBox(self.groupBox_3)
        self.comboBox_algorithm.addItem("")
        self.comboBox_algorithm.setObjectName(u"comboBox_algorithm")

        self.gridLayout_2.addWidget(self.comboBox_algorithm, 0, 1, 1, 1)

        self.pushButton_run = QPushButton(self.groupBox_3)
        self.pushButton_run.setObjectName(u"pushButton_run")

        self.gridLayout_2.addWidget(self.pushButton_run, 1, 0, 1, 1)

        self.pushButton_terminate = QPushButton(self.groupBox_3)
        self.pushButton_terminate.setObjectName(u"pushButton_terminate")

        self.gridLayout_2.addWidget(self.pushButton_terminate, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 2)

        self.groupBox_2 = QGroupBox(ConfigureEquationParametersWindow)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.comboBox_objective_function = QComboBox(self.groupBox_2)
        self.comboBox_objective_function.addItem("")
        self.comboBox_objective_function.setObjectName(u"comboBox_objective_function")

        self.gridLayout_5.addWidget(self.comboBox_objective_function, 0, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)

        self.stackedWidget_objective_function = QStackedWidget(self.groupBox_2)
        self.stackedWidget_objective_function.setObjectName(u"stackedWidget_objective_function")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_6 = QGridLayout(self.page_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.doubleSpinBox_time_window_gama_factor = QDoubleSpinBox(self.page_3)
        self.doubleSpinBox_time_window_gama_factor.setObjectName(u"doubleSpinBox_time_window_gama_factor")
        self.doubleSpinBox_time_window_gama_factor.setValue(0.840000000000000)

        self.gridLayout_6.addWidget(self.doubleSpinBox_time_window_gama_factor, 0, 1, 1, 1)

        self.label_13 = QLabel(self.page_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)

        self.stackedWidget_objective_function.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget_objective_function.addWidget(self.page_4)

        self.gridLayout_5.addWidget(self.stackedWidget_objective_function, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 2)

        self.groupBox = QGroupBox(ConfigureEquationParametersWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget_equation_parameters = QStackedWidget(self.groupBox)
        self.stackedWidget_equation_parameters.setObjectName(u"stackedWidget_equation_parameters")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.doubleSpinBox_Vi_dynamics_min = QDoubleSpinBox(self.page)
        self.doubleSpinBox_Vi_dynamics_min.setObjectName(u"doubleSpinBox_Vi_dynamics_min")
        self.doubleSpinBox_Vi_dynamics_min.setMinimum(-200.000000000000000)
        self.doubleSpinBox_Vi_dynamics_min.setMaximum(0.000000000000000)
        self.doubleSpinBox_Vi_dynamics_min.setValue(-90.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_Vi_dynamics_min, 5, 1, 1, 1)

        self.doubleSpinBox_ki_dynamics_max = QDoubleSpinBox(self.page)
        self.doubleSpinBox_ki_dynamics_max.setObjectName(u"doubleSpinBox_ki_dynamics_max")
        self.doubleSpinBox_ki_dynamics_max.setMinimum(-100.000000000000000)
        self.doubleSpinBox_ki_dynamics_max.setMaximum(0.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_ki_dynamics_max, 4, 2, 1, 1)

        self.label_Vi_dynamics = QLabel(self.page)
        self.label_Vi_dynamics.setObjectName(u"label_Vi_dynamics")

        self.gridLayout_4.addWidget(self.label_Vi_dynamics, 5, 0, 1, 1)

        self.doubleSpinBox_ki_dynamics_min = QDoubleSpinBox(self.page)
        self.doubleSpinBox_ki_dynamics_min.setObjectName(u"doubleSpinBox_ki_dynamics_min")
        self.doubleSpinBox_ki_dynamics_min.setMinimum(-100.000000000000000)
        self.doubleSpinBox_ki_dynamics_min.setMaximum(0.000000000000000)
        self.doubleSpinBox_ki_dynamics_min.setValue(-20.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_ki_dynamics_min, 4, 1, 1, 1)

        self.label_VT_dynamics = QLabel(self.page)
        self.label_VT_dynamics.setObjectName(u"label_VT_dynamics")

        self.gridLayout_4.addWidget(self.label_VT_dynamics, 6, 0, 1, 1)

        self.doubleSpinBox_alpha_dynamics_min = QDoubleSpinBox(self.page)
        self.doubleSpinBox_alpha_dynamics_min.setObjectName(u"doubleSpinBox_alpha_dynamics_min")

        self.gridLayout_4.addWidget(self.doubleSpinBox_alpha_dynamics_min, 2, 1, 1, 1)

        self.label_alpha_dynamics = QLabel(self.page)
        self.label_alpha_dynamics.setObjectName(u"label_alpha_dynamics")

        self.gridLayout_4.addWidget(self.label_alpha_dynamics, 2, 0, 1, 1)

        self.doubleSpinBox_ka_dynamics_max = QDoubleSpinBox(self.page)
        self.doubleSpinBox_ka_dynamics_max.setObjectName(u"doubleSpinBox_ka_dynamics_max")
        self.doubleSpinBox_ka_dynamics_max.setValue(20.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_ka_dynamics_max, 3, 2, 1, 1)

        self.label_ka_dynamics = QLabel(self.page)
        self.label_ka_dynamics.setObjectName(u"label_ka_dynamics")

        self.gridLayout_4.addWidget(self.label_ka_dynamics, 3, 0, 1, 1)

        self.doubleSpinBox_tao_theta_dynamics_min = QDoubleSpinBox(self.page)
        self.doubleSpinBox_tao_theta_dynamics_min.setObjectName(u"doubleSpinBox_tao_theta_dynamics_min")
        self.doubleSpinBox_tao_theta_dynamics_min.setMinimum(0.010000000000000)
        self.doubleSpinBox_tao_theta_dynamics_min.setValue(0.100000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_tao_theta_dynamics_min, 1, 1, 1, 1)

        self.label_ki_dyamics = QLabel(self.page)
        self.label_ki_dyamics.setObjectName(u"label_ki_dyamics")

        self.gridLayout_4.addWidget(self.label_ki_dyamics, 4, 0, 1, 1)

        self.doubleSpinBox_Vi_dynamics_fixed = QDoubleSpinBox(self.page)
        self.doubleSpinBox_Vi_dynamics_fixed.setObjectName(u"doubleSpinBox_Vi_dynamics_fixed")
        self.doubleSpinBox_Vi_dynamics_fixed.setMinimum(-2000.000000000000000)
        self.doubleSpinBox_Vi_dynamics_fixed.setMaximum(9900.989999999999782)

        self.gridLayout_4.addWidget(self.doubleSpinBox_Vi_dynamics_fixed, 5, 4, 1, 1)

        self.label_tao_theta_dynamics = QLabel(self.page)
        self.label_tao_theta_dynamics.setObjectName(u"label_tao_theta_dynamics")

        self.gridLayout_4.addWidget(self.label_tao_theta_dynamics, 1, 0, 1, 1)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_4.addWidget(self.label_2, 0, 1, 1, 3)

        self.doubleSpinBox_alpha_dynamics_fixed = QDoubleSpinBox(self.page)
        self.doubleSpinBox_alpha_dynamics_fixed.setObjectName(u"doubleSpinBox_alpha_dynamics_fixed")
        self.doubleSpinBox_alpha_dynamics_fixed.setMinimum(-1000000.000000000000000)
        self.doubleSpinBox_alpha_dynamics_fixed.setMaximum(1000000.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_alpha_dynamics_fixed, 2, 4, 1, 1)

        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_4.addWidget(self.label_3, 0, 4, 1, 2)

        self.doubleSpinBox_ki_dynamics_fixed = QDoubleSpinBox(self.page)
        self.doubleSpinBox_ki_dynamics_fixed.setObjectName(u"doubleSpinBox_ki_dynamics_fixed")
        self.doubleSpinBox_ki_dynamics_fixed.setMinimum(-2000.000000000000000)
        self.doubleSpinBox_ki_dynamics_fixed.setMaximum(2000.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_ki_dynamics_fixed, 4, 4, 1, 1)

        self.doubleSpinBox_VT_dynamics_fixed = QDoubleSpinBox(self.page)
        self.doubleSpinBox_VT_dynamics_fixed.setObjectName(u"doubleSpinBox_VT_dynamics_fixed")
        self.doubleSpinBox_VT_dynamics_fixed.setMinimum(-20000.000000000000000)
        self.doubleSpinBox_VT_dynamics_fixed.setMaximum(1000000.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_VT_dynamics_fixed, 6, 4, 1, 1)

        self.doubleSpinBox_alpha_dynamics_max = QDoubleSpinBox(self.page)
        self.doubleSpinBox_alpha_dynamics_max.setObjectName(u"doubleSpinBox_alpha_dynamics_max")
        self.doubleSpinBox_alpha_dynamics_max.setValue(1.570000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_alpha_dynamics_max, 2, 2, 1, 1)

        self.doubleSpinBox_tao_theta_dynamics_max = QDoubleSpinBox(self.page)
        self.doubleSpinBox_tao_theta_dynamics_max.setObjectName(u"doubleSpinBox_tao_theta_dynamics_max")
        self.doubleSpinBox_tao_theta_dynamics_max.setValue(10.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_tao_theta_dynamics_max, 1, 2, 1, 1)

        self.doubleSpinBox_Vi_dynamics_max = QDoubleSpinBox(self.page)
        self.doubleSpinBox_Vi_dynamics_max.setObjectName(u"doubleSpinBox_Vi_dynamics_max")

        self.gridLayout_4.addWidget(self.doubleSpinBox_Vi_dynamics_max, 5, 2, 1, 1)

        self.doubleSpinBox_ka_dynamics_min = QDoubleSpinBox(self.page)
        self.doubleSpinBox_ka_dynamics_min.setObjectName(u"doubleSpinBox_ka_dynamics_min")

        self.gridLayout_4.addWidget(self.doubleSpinBox_ka_dynamics_min, 3, 1, 1, 1)

        self.doubleSpinBox_VT_dynamics_max = QDoubleSpinBox(self.page)
        self.doubleSpinBox_VT_dynamics_max.setObjectName(u"doubleSpinBox_VT_dynamics_max")

        self.gridLayout_4.addWidget(self.doubleSpinBox_VT_dynamics_max, 6, 2, 1, 1)

        self.doubleSpinBox_ka_dynamics_fixed = QDoubleSpinBox(self.page)
        self.doubleSpinBox_ka_dynamics_fixed.setObjectName(u"doubleSpinBox_ka_dynamics_fixed")
        self.doubleSpinBox_ka_dynamics_fixed.setMinimum(-10100.000000000000000)
        self.doubleSpinBox_ka_dynamics_fixed.setMaximum(100000.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_ka_dynamics_fixed, 3, 4, 1, 1)

        self.doubleSpinBox_tao_theta_dynamics_fixed = QDoubleSpinBox(self.page)
        self.doubleSpinBox_tao_theta_dynamics_fixed.setObjectName(u"doubleSpinBox_tao_theta_dynamics_fixed")
        self.doubleSpinBox_tao_theta_dynamics_fixed.setMinimum(-1000000.000000000000000)
        self.doubleSpinBox_tao_theta_dynamics_fixed.setMaximum(1000000.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_tao_theta_dynamics_fixed, 1, 4, 1, 1)

        self.doubleSpinBox_VT_dynamics_min = QDoubleSpinBox(self.page)
        self.doubleSpinBox_VT_dynamics_min.setObjectName(u"doubleSpinBox_VT_dynamics_min")
        self.doubleSpinBox_VT_dynamics_min.setMinimum(-200.000000000000000)
        self.doubleSpinBox_VT_dynamics_min.setMaximum(100.000000000000000)
        self.doubleSpinBox_VT_dynamics_min.setValue(-90.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_VT_dynamics_min, 6, 1, 1, 1)

        self.checkBox_fit_dynamics = QCheckBox(self.page)
        self.checkBox_fit_dynamics.setObjectName(u"checkBox_fit_dynamics")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox_fit_dynamics.sizePolicy().hasHeightForWidth())
        self.checkBox_fit_dynamics.setSizePolicy(sizePolicy1)
        self.checkBox_fit_dynamics.setMaximumSize(QSize(20, 16777215))
        self.checkBox_fit_dynamics.setIconSize(QSize(16, 14))
        self.checkBox_fit_dynamics.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_fit_dynamics, 1, 3, 6, 1)

        self.checkBox_fixed_dynamics = QCheckBox(self.page)
        self.checkBox_fixed_dynamics.setObjectName(u"checkBox_fixed_dynamics")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkBox_fixed_dynamics.sizePolicy().hasHeightForWidth())
        self.checkBox_fixed_dynamics.setSizePolicy(sizePolicy2)
        self.checkBox_fixed_dynamics.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_4.addWidget(self.checkBox_fixed_dynamics, 1, 5, 6, 1)

        self.stackedWidget_equation_parameters.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_equation_parameters.addWidget(self.page_2)

        self.gridLayout_3.addWidget(self.stackedWidget_equation_parameters, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)


        self.retranslateUi(ConfigureEquationParametersWindow)
        self.stackedWidget_equation_parameters.currentChanged.connect(self.stackedWidget_equation_parameters.setCurrentIndex)

        self.stackedWidget_objective_function.setCurrentIndex(0)
        self.stackedWidget_equation_parameters.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ConfigureEquationParametersWindow)
    # setupUi

    def retranslateUi(self, ConfigureEquationParametersWindow):
        ConfigureEquationParametersWindow.setWindowTitle(QCoreApplication.translate("ConfigureEquationParametersWindow", u"Configure equation parameters", None))
        self.pushButton_OK.setText(QCoreApplication.translate("ConfigureEquationParametersWindow", u"OK", None))
        self.pushButton_canel.setText(QCoreApplication.translate("ConfigureEquationParametersWindow", u"Canel", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ConfigureEquationParametersWindow", u"Optimization", None))
        self.label_12.setText(QCoreApplication.translate("ConfigureEquationParametersWindow", u"Algorithm", None))
        self.comboBox_algorithm.setItemText(0, QCoreApplication.translate("ConfigureEquationParametersWindow", u"CMA-ES", None))

        self.pushButton_run.setText(QCoreApplication.translate("ConfigureEquationParametersWindow", u"Run", None))
        self.pushButton_terminate.setText(QCoreApplication.translate("ConfigureEquationParametersWindow", u"Terminate", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ConfigureEquationParametersWindow", u"Objective function", None))
        self.comboBox_objective_function.setItemText(0, QCoreApplication.translate("ConfigureEquationParametersWindow", u"Gama factor", None))

        self.label_11.setText(QCoreApplication.translate("ConfigureEquationParametersWindow", u"Option", None))
        self.label_13.setText(QCoreApplication.translate("ConfigureEquationParametersWindow", u"Time window \u03c3 (ms)", None))
        self.groupBox.setTitle(QCoreApplication.translate("ConfigureEquationParametersWindow", u"Equation parameters", None))
        self.label_Vi_dynamics.setText(QCoreApplication.translate("ConfigureEquationParametersWindow", u"Vi", None))
        self.label_VT_dynamics.setText(QCoreApplication.translate("ConfigureEquationParametersWindow", u"VT", None))
        self.label_alpha_dynamics.setText(QCoreApplication.translate("ConfigureEquationParametersWindow", u"\u03b1", None))
        self.label_ka_dynamics.setText(QCoreApplication.translate("ConfigureEquationParametersWindow", u"ka", None))
        self.label_ki_dyamics.setText(QCoreApplication.translate("ConfigureEquationParametersWindow", u"ki", None))
        self.label_tao_theta_dynamics.setText(QCoreApplication.translate("ConfigureEquationParametersWindow", u"\u03c4\u03b8", None))
        self.label.setText(QCoreApplication.translate("ConfigureEquationParametersWindow", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("ConfigureEquationParametersWindow", u"Bounds", None))
        self.label_3.setText(QCoreApplication.translate("ConfigureEquationParametersWindow", u"Fixed value", None))
        self.checkBox_fit_dynamics.setText("")
        self.checkBox_fixed_dynamics.setText("")
    # retranslateUi

