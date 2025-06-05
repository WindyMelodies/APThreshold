"""The MainWindow class is the main user interface for the application. It inherits from QMainWindow and Ui_MainWindow,
and is responsible for initializing user interface. The class also handles user interactions, and coordinating with
other modules and manages all the interface components, child windows, and plotting functionalities."""

import matplotlib.pyplot as plt
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QWidget, QMainWindow, QGridLayout, QLabel, QSpinBox, QComboBox, \
    QDoubleSpinBox, QPushButton, QMessageBox, QTableWidgetItem, QAbstractItemView, QTabWidget, QHeaderView, \
    QStackedWidget, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from utils.condition_check import data_source_check, spike_check, data_exists_check
from .calculate_feature_window import CalculateFeatureWindow
from ui import ExtractAPWindow
from .import_data_widget import ImportDataWidget
from .ramp_based_method_window import RampMethodWindow
from .set_fig_window_AP import SetFigWindowAP
from .set_fig_window_Vth import SetFigWindowVth
from .threshold_equation_method_window import ThresholdEquationMethodMainWindow, \
    ThresholdEquationMethodWorkflowOneWindow
from .ui_main_window import Ui_MainWindow
from utils.custom_navigation_toolbar import CustomNavigationToolbar as NavigationToolbar
from utils.curvature_based_method import MethodBasedOnCurvature
from utils.ode_solver import Model
from utils.plotting import Plotting
from utils.tools import *


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.threshold_equation_workflow_2_panel = None
        self.threshold_equation_workflow_1_panel = None
        self.layout_panel_threshold_equation_stacked_widget = None
        self.layout_page_threshold_equation = None
        self.threshold_equation_main_window = None
        self.features_option = {'<Vm>': 0, 'dV/dt': [None, 0]}
        self.pos_APWindow = None
        self.rampMethod_window = None
        self.Model = None
        self.model_name = None
        self.plotting_curvature = None
        self.CurvatureSpikeThreshold = None
        self.plotting_simulation = None
        self.ramp_window = None
        self.figure_set_simulation = None
        self.figure_set_experiment = None
        self.figure_set_curvature = None
        self.figure_set_ramp = None
        self.ParasOfFeaturesWindow = None

        self.names_window = {}  # Store sub-windows embedded in the main user interface
        self.names = {}  # Store all current stimulus pages
        self.names_fig = {}  # Store all figure
        self.AP = {}

        self.names_AP = {}  # AP: action potential
        self.names_AP_window = {}
        self.init_ui()
        self.setup_signal_slot()
        self.setObjectName('Mywindow')
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        width = 1000
        height = 700
        x = (screen_geometry.width() - width) // 2
        y = (screen_geometry.height() - height) // 2
        self.setGeometry(QRect(x, y, width, height))

    def init_ui(self):
        self.setStyleSheet("""QWidget#Mywindow {background-color: #E4F4FE}""")
        self.setupUi(self)
        self.lineEdit_minimum_Vth.setStyleSheet("background-color: silver; color: black;")
        self.lineEdit_maximum_Vth.setStyleSheet("background-color: silver; color: black;")
        self.lineEdit_mean_Vth.setStyleSheet("background-color: silver; color: black;")
        self.lineEdit_SD_Vth.setStyleSheet("background-color: silver; color: black;")
        self.setWindowTitle("APThreshold".center(50))
        self.page_ramp_method_init()
        self.page_canvas_init()
        self.page_threshold_equation_method_init()
        self.page_stimulus_init()
        self.widget_physiological_data_init()
        self.doubleSpinBox_kth_curvature.setMaximum(10000000)
        self.tabWidget_main.setTabPosition(QTabWidget.North)
        plt.rcParams['font.size'] = 10
        plt.rcParams['font.sans-serif'] = ['Times New Roman']
        plt.rcParams['savefig.dpi'] = 400

    def simulation_run(self):
        """
        Simulates the biophysical model of a neuron to generate action potentials .
        """
        # 1. Reset the CurvatureSpikeThreshold class.
        self.CurvatureSpikeThreshold = None
        # 2. Update the voltage option for extracting APs corresponding to different compartments of neuron model.
        self.slot_update_voltage_option()
        # 3. Generate the stimulus current and solve the differential equations for the model.
        self.Model = Model(self)
        # 4. Plot the results in default settings
        self.plotting_simulation = Plotting(data=self.Model.data, figure_set=self.Model.figure_set,
                                            axes=self.names['axes_AP'])
        # 5. Update the SetFigWindow_AP with the new simulation results.
        self.names['Canvas_AP'].draw()
        if 'SetFigWindow_AP' in self.names_window:
            self.names_window['SetFigWindow_AP'].close()
            self.names_window['SetFigWindow_AP'].deleteLater()
            self.names_window.pop('SetFigWindow_AP')
            self.names_window['SetFigWindow_AP'] = SetFigWindowAP(data_operation_module=self.Model,
                                                                  main_window=self)
            self.names_window['SetFigWindow_AP'].show()

    def slot_curvature_run(self):
        """
        Estimating spike threshold of extracted APs using the waveform curvature-based method
        """
        # 1. Retrieve the parameter settings: method option, `k_th` value, and voltage option.
        option = self.comboBox_method_curvature.currentIndex()
        kth = self.doubleSpinBox_kth_curvature.value()
        voltage_option = self.comboBox_voltage_option.currentText()
        logging.info(
            'Estimating spike threshold of extracted APs using the waveform curvature-based method\nk_th={}'.format(
                kth))
        logging.info('voltage_option:{}'.format(voltage_option))
        self.CurvatureSpikeThreshold = MethodBasedOnCurvature(main_window=self, option=option, k_th=kth,
                                                              voltage_option=voltage_option)
        if self.CurvatureSpikeThreshold.condition:
            # 2. Close the feature calculation window.
            if self.ParasOfFeaturesWindow:
                self.ParasOfFeaturesWindow.cancel_clicked()
            else:
                pass
            # 3. Update the feature table
            self.add_features_to_TableWidget(self.tableWidget_features, self.CurvatureSpikeThreshold.data)
            # 4. Plotting
            self.plotting_curvature = Plotting(data=self.CurvatureSpikeThreshold.data,
                                               figure_set=self.CurvatureSpikeThreshold.figure_set,
                                               axes=self.names['axes_Vth'])
            self.names['Canvas_Vth'].draw()
            # 5. Update SetFigWindow_Vth for new data visualization
            if 'SetFigWindow_Vth' in self.names_window:
                self.names_window['SetFigWindow_Vth'].close()

                if 'SetFigWindow_Vth' in self.names_window:
                    self.names_window['SetFigWindow_Vth'].deleteLater()
                    self.names_window.pop('SetFigWindow_Vth')
                self.names_window['SetFigWindow_Vth'] = SetFigWindowVth(
                    data_operation_module=self.CurvatureSpikeThreshold,
                    main_window=self)
                self.names_window['SetFigWindow_Vth'].show()
            # 6. display Vth (spike threshold) info
            if self.CurvatureSpikeThreshold.data:
                if 'Vth' in self.CurvatureSpikeThreshold.data['All']['features'].keys():
                    Vth_list = self.CurvatureSpikeThreshold.data['All']['features']['Vth']
                    Vth_max = round(max(Vth_list), 3)
                    Vth_min = round(min(Vth_list), 3)
                    Vth_mean = round(np.mean(Vth_list), 3)
                    Vth_stand_deviation = round(np.std(Vth_list), 3)
                    self.lineEdit_SD_Vth.setText("{:.3f}".format(Vth_stand_deviation))
                    self.lineEdit_mean_Vth.setText("{:.3f}".format(Vth_mean))
                    self.lineEdit_maximum_Vth.setText("{:.3f}".format(Vth_max))
                    self.lineEdit_minimum_Vth.setText("{:.3f}".format(Vth_min))

    def widget_physiological_data_init(self):
        """Initiate widget objective for importing experimental data"""
        self.widget_physiological_data = ImportDataWidget(self)
        self.gridLayout_physiological_datas.addWidget(self.widget_physiological_data)

    def page_threshold_equation_method_init(self):
        self.threshold_equation_main_window = ThresholdEquationMethodMainWindow()
        self.threshold_equation_workflow_1_panel = ThresholdEquationMethodWorkflowOneWindow(main_window=self)
        self.threshold_equation_workflow_2_panel = None
        self.stackedWidget_threshold_equation_method.addWidget(self.threshold_equation_main_window)
        self.stackedWidget_threshold_equation_method.addWidget(self.threshold_equation_workflow_1_panel)
        self.threshold_equation_main_window.pushButton_workflow_1.clicked.connect(
            lambda: self.stackedWidget_threshold_equation_method.setCurrentIndex(1))
        self.threshold_equation_workflow_1_panel.pushButton_back_to_home_workflow_1.clicked.connect(
            lambda: self.stackedWidget_threshold_equation_method.setCurrentIndex(0))

    def page_ramp_method_init(self):
        """Initiate widget objective for quantify spike threshold using ramp stimulation-based method"""
        self.layout_page_ramp = QGridLayout(self.page_method_ramp)
        self.layout_page_ramp.setContentsMargins(0, 0, 0, 0)
        self.layout_page_ramp.setSpacing(6)
        self.rampMethod_window = RampMethodWindow(self)
        self.layout_page_ramp.addWidget(self.rampMethod_window)

    def setup_signal_slot(self):
        self.pushButton_add_stim.clicked.connect(self.slot_auto_add_stim)
        self.pushButton_simulation_run.clicked.connect(self.simulation_run)
        self.pushButton_setplot_AP.clicked.connect(
            self.set_plot_simulation)
        self.pushButton_auto_extrac_APs.clicked.connect(self.auto_detect_aps)
        self.pushButton_add_ap.clicked.connect(self.slot_auto_add_ap_pushbutton)
        self.pushButton_subtract_ap.toggled.connect(self.slot_subtract_aps_button_isChecked)
        self.pushButton_run_curvature.clicked.connect(self.slot_curvature_run)
        self.pushButton_setplot_Vth.clicked.connect(self.set_plot_spike_threshold)
        self.pushButton_set_parameters_features.clicked.connect(self.slot_pushButton_set_parameters_features_clicked)
        self.comboBox_model.currentIndexChanged.connect(self.slot_update_stimulus_page)
        self.pushButton_save_data_APs.clicked.connect(self.save_data)
        self.pushButton_save_data_Vth.clicked.connect(self.save_data)

    def save_data(self):
        if self.sender().objectName() == 'pushButton_save_data_APs':
            if self.toolBox_aquire_ap.currentIndex() == 0:
                if self.Model is None:
                    msg_box = QMessageBox(QMessageBox.Information, 'Message', 'No action potentials')
                    msg_box.exec()
                else:
                    open_save_data_window(self.Model.data)
            else:
                if self.widget_physiological_data.data is None:
                    msg_box = QMessageBox(QMessageBox.Information, 'Message', 'No experimental data!')
                    msg_box.exec()
                else:
                    open_save_data_window(self.widget_physiological_data.data)
        else:
            if self.toolBox_calculate_spike_threshold.currentIndex() == 0:
                if self.CurvatureSpikeThreshold is None:
                    msg_box = QMessageBox(QMessageBox.Information, 'Message', 'Run first!')
                    msg_box.exec()
                else:
                    open_save_data_window(self.CurvatureSpikeThreshold.data)
            elif self.toolBox_calculate_spike_threshold.currentIndex() == 1:
                if self.rampMethod_window.data:
                    open_save_data_window(self.rampMethod_window.data)
                else:
                    msg_box = QMessageBox(QMessageBox.Information, 'Message', 'Run first!')
                    msg_box.exec()

    def slot_update_stimulus_page(self):
        #  Update the stimulus names in each stimulation page's comboBox.
        text = self.comboBox_model.currentText().replace(' model', 'model')
        model = importlib.import_module(text)
        compartment_num = model.Model.number_of_compartment
        if compartment_num == 1:
            name_list = ['Istim']
        elif compartment_num == 2:
            name_list = ['Is', 'Id']
        else:
            name_list = []
            for i in range(compartment_num):
                name = 'Istim' + '{}'.format(i + 1)
                name_list.append(name)
        # Get all stimulus page name in "Stimulation" panel
        tab_list = self.tabWidget_stimulus.findChildren(QWidget)
        tab_name_list = []
        for i in tab_list:
            tab_name_list.append(i.objectName())
        tab_name_list_only_tab = []
        for i in tab_name_list:
            if i.startswith('tab'):
                tab_name_list_only_tab.append(i.strip('tab_'))
        for i in tab_name_list_only_tab:
            self.names['comboBox_' + i + '_name'].clear()
            for j in name_list:
                self.names['comboBox_' + i + '_name'].addItem(j)

    def slot_auto_add_ap_pushbutton(self):
        """
        Slot function to add an AP button, display the Extract AP window, and perform data checks.
        If voltage data exists, the 'AP' button can be added.
        """
        flag = 0

        # Check that the position of user interface is in 'Model simulation' or 'Experimental recording' panel.
        if self.toolBox_aquire_ap.currentIndex() == 0:
            # 'Model simulation' panel
            if self.Model:
                flag = 1
            else:
                msg_box = QMessageBox(QMessageBox.Information, 'Message', 'NO Action Potentials!')
                msg_box.exec()
        else:
            # 'Experimental recording' panel
            if self.widget_physiological_data.data:
                flag = 1
            else:
                msg_box = QMessageBox(QMessageBox.Information, 'Message', 'NO Action Potentials!')
                msg_box.exec()
        # Add 'AP' button only if voltage data exists (flag = 1)
        if flag != 0:
            if self.pushButton_subtract_ap.isChecked():
                self.pushButton_subtract_ap.toggle()
            widgets = self.scrollAreaWidgetContents_aps.findChildren(QPushButton)
            if len(widgets) == 0:
                num = '1'
            else:
                num = str(int(widgets[len(widgets) - 1].objectName().strip('AP')) + 1)
            name = 'AP' + num
            self.names_AP[name] = QPushButton(self.scrollAreaWidgetContents_aps)
            self.names_AP[name].setText(name)
            self.names_AP[name].setObjectName(name)
            self.names_AP[name].clicked.connect(self.slot_show_ExtractAPWindow)
            self.horizontalLayout_aps.addWidget(self.names_AP[name])

    def slot_subtract_aps_button_isChecked(self):
        """Function to subtract AP button"""
        if self.pushButton_subtract_ap.isChecked():
            for i in self.names_AP:
                self.names_AP[i].clicked.disconnect(self.slot_show_ExtractAPWindow)
                self.names_AP[i].clicked.connect(self.slot_delete_pushbutton)
        else:
            for i in self.names_AP:
                self.names_AP[i].clicked.disconnect(self.slot_delete_pushbutton)
                self.names_AP[i].clicked.connect(self.slot_show_ExtractAPWindow)

    def auto_detect_aps(self):
        """自动提取单个动作电位"""
        # 1. 检查是否存在膜电压数据，以及界面位置位于Model simulation还是Experimental recording
        if data_exists_check(main_window=self):

            data_source, voltage_option, data, dt = data_source_check(
                self)
            logging.info(f'data_source: {data_source}')
            logging.info(f'voltage_option: {voltage_option}')
            voltage = np.array(get_voltage_from_data(data=data, data_source=data_source,
                                                     voltage_option=voltage_option))
            timestamp = get_timestamp_from_data(data=data)
            index_peaks = detect_spike(voltage)
            dVdt1 = get_derivative_voltage_from_data(data=data, data_source=data_source, voltage_option=voltage_option)
            ap_start_stop_index = identify_single_aps(index_peaks=index_peaks, voltage=voltage, dVdt1=dVdt1,
                                                      timestamp=timestamp)
            if self.names_AP:
                for name in self.names_AP:
                    self.names_AP[name].deleteLater()
                self.AP = {}
            for i in range(len(ap_start_stop_index)):
                widgets = self.scrollAreaWidgetContents_aps.findChildren(QPushButton)
                if len(widgets) == 0:
                    num = '1'
                else:
                    num = str(int(widgets[len(widgets) - 1].objectName().strip('AP')) + 1)
                name = 'AP' + num
                self.names_AP[name] = QPushButton(self.scrollAreaWidgetContents_aps)
                self.names_AP[name].setText(name)
                self.names_AP[name].setObjectName(name)
                self.names_AP[name].clicked.connect(self.slot_show_ExtractAPWindow)
                self.horizontalLayout_aps.addWidget(self.names_AP[name])
                self.AP[name] = {'start': timestamp[ap_start_stop_index[i][0]],
                                 'stop': timestamp[ap_start_stop_index[i][1]]}

        else:
            msg_box = QMessageBox(QMessageBox.Information, 'Message', 'No spike data!')
            msg_box.exec()

    def slot_delete_pushbutton(self):
        sender = self.sender()
        name = sender.objectName()
        self.names_AP[name].deleteLater()
        self.names_AP.pop(name)
        if name in self.AP:
            self.AP.pop(name)

    def slot_show_ExtractAPWindow(self):
        sender = self.sender()
        name = sender.objectName()
        self.names_AP_window[name] = ExtractAPWindow(name, self)
        if self.pos_APWindow:
            self.names_AP_window[name].setGeometry(self.pos_APWindow)
        self.names_AP_window[name].show()

    def slot_auto_add_stim(self):
        """
        Click '+' button in Stimulation sub-panel, and a new 'Stim' page is added standing for another stimulus. At end,
        all stimulus will be applied to the neuronal model at once.
        """
        if self.tabWidget_stimulus.count() >= 10:
            pass
        else:
            tab_num = self.tabWidget_stimulus.count()
            tab_list = self.tabWidget_stimulus.findChildren(QWidget)
            tab_name_list = []
            tab_name_list_final = []

            for i in tab_list:
                tab_name_list.append(i.objectName())

            for i in tab_name_list:
                if 'tab_stim' in i and len(i) <= 10:
                    tab_name_list_final.append(int(i.strip('tab_stim')))

            list_all = list(range(1, 1 + max(tab_name_list_final)))

            tab_name1 = 'stim' + str(tab_num + 1)
            if len(list_all) == len(tab_name_list_final):
                tab_name2 = None
            else:
                tab_name2 = 'stim' + str(min(list(set(list_all) - set(tab_name_list_final))))
            tab_name = tab_name1 if tab_name2 is None else tab_name2

            self.names['tab_' + tab_name] = QWidget()
            self.names['tab_' + tab_name].setObjectName('tab_' + tab_name)

            self.names['gridLayout_tab_' + tab_name] = QGridLayout(self.names['tab_' + tab_name])
            self.names['gridLayout_tab_' + tab_name].setObjectName('gridLayout_tab_' + tab_name)
            self.tabWidget_stimulus.addTab(self.names['tab_' + tab_name], tab_name)
            model = importlib.import_module(self.comboBox_model.currentText().replace(' model', 'model'))
            compartment_num = model.Model.number_of_compartment
            self.add_stim_name(names=self.names, tab_name=tab_name, com_num=compartment_num)

            self.names['label_' + tab_name + '_type'] = QLabel(self.names['tab_' + tab_name])
            self.names['label_' + tab_name + '_type'].setObjectName('label_' + tab_name + '_type')
            self.names['label_' + tab_name + '_type'].setText('Type')
            self.names['gridLayout_tab_' + tab_name].addWidget(self.names['label_' + tab_name + '_type'], 2, 1, 1, 1)

            self.names['comboBox_' + tab_name] = QComboBox(self.names['tab_' + tab_name])
            self.names['comboBox_' + tab_name].setObjectName('comboBox_' + tab_name)
            self.names['comboBox_' + tab_name].addItem("DC")
            self.names['comboBox_' + tab_name].addItem("AC")
            self.names['comboBox_' + tab_name].addItem("Ramp")
            self.names['comboBox_' + tab_name].addItem("OU process")
            self.names['gridLayout_tab_' + tab_name].addWidget(self.names['comboBox_' + tab_name], 2, 2, 1, 1)

            self.names['label_' + tab_name + '_Start'] = QLabel(self.names['tab_' + tab_name])
            self.names['label_' + tab_name + '_Start'].setObjectName('label_' + tab_name + '_Start')
            self.names['label_' + tab_name + '_Start'].setText("Start (ms)")
            self.names['gridLayout_tab_' + tab_name].addWidget(self.names['label_' + tab_name + '_Start'], 3, 1, 1, 1)

            self.names['doubleSpinBox_' + tab_name + '_start'] = QDoubleSpinBox(self.names['tab_' + tab_name])
            self.names['doubleSpinBox_' + tab_name + '_start'].setObjectName('doubleSpinBox_' + tab_name + '_start')
            self.names['doubleSpinBox_' + tab_name + '_start'].setMaximum(10000000)
            self.names['gridLayout_tab_' + tab_name].addWidget(self.names['doubleSpinBox_' + tab_name + '_start'], 3, 2,
                                                               1, 1)

            self.names['label_' + tab_name + '_Stop'] = QLabel(self.names['tab_' + tab_name])
            self.names['label_' + tab_name + '_Stop'].setObjectName('label_' + tab_name + '_Stop')
            self.names['label_' + tab_name + '_Stop'].setText('Stop (ms)')
            self.names['gridLayout_tab_' + tab_name].addWidget(self.names['label_' + tab_name + '_Stop'], 4, 1, 1, 1)

            self.names['doubleSpinBox_' + tab_name + '_stop'] = QDoubleSpinBox(self.names['tab_' + tab_name])
            self.names['doubleSpinBox_' + tab_name + '_stop'].setObjectName('doubleSpinBox_' + tab_name + '_stop')
            self.names['doubleSpinBox_' + tab_name + '_stop'].setMaximum(10000000)
            self.names['gridLayout_tab_' + tab_name].addWidget(self.names['doubleSpinBox_' + tab_name + '_stop'], 4, 2,
                                                               1, 1)
            self.names['label_' + tab_name + '_amplitude'] = QLabel(self.names['tab_' + tab_name])
            self.names['label_' + tab_name + '_amplitude'].setText('Amplitude (μA/cm<sup>2</sup>)')
            self.names['label_' + tab_name + '_amplitude'].setObjectName('label_' + tab_name + '_amplitude')

            self.names['gridLayout_tab_' + tab_name].addWidget(self.names['label_' + tab_name + '_amplitude'], 5, 1,
                                                               1, 1)
            self.names['doubleSpinBox_' + tab_name + '_amplitude'] = QDoubleSpinBox(self.names['tab_' + tab_name])

            self.names['doubleSpinBox_' + tab_name + '_amplitude'].setObjectName(
                'doubleSpinBox_' + tab_name + '_amplitude')

            self.names['doubleSpinBox_' + tab_name + '_amplitude'].setMinimum(-1000)
            self.names['gridLayout_tab_' + tab_name].addWidget(self.names['doubleSpinBox_' + tab_name + '_amplitude'],
                                                               5, 2, 1, 1)

            self.names['comboBox_' + tab_name].currentIndexChanged.connect(self.slot_auto_add_widget)

    def delete_stim_tab(self, index):
        self.tabWidget_stimulus.widget(index).deleteLater()

    def set_plot_simulation(self):
        """
        Show the SetFigWindow to configure visualization settings of simulation data.
        Check the position of current panel ('Model simulation' of 'Experimental recording' panel), and the spike data
        corresponding to the panel will be passed to the SetFigWindow for initialization.
        """
        if self.toolBox_aquire_ap.currentIndex() == 0:
            if self.Model is None:
                msg_box = QMessageBox(QMessageBox.Information, 'Message', 'No action potentials')
                msg_box.exec()
            else:
                self.names_window['SetFigWindow_AP'] = SetFigWindowAP(data_operation_module=self.Model,
                                                                      main_window=self)
                self.names_window['SetFigWindow_AP'].show()
        else:
            if self.widget_physiological_data.data is None:
                msg_box = QMessageBox(QMessageBox.Information, 'Message', 'No experimental data!')
                msg_box.exec()
            else:
                self.names_window['SetFigWindow_AP'] = SetFigWindowAP(
                    data_operation_module=self.widget_physiological_data,
                    main_window=self)
                self.names_window['SetFigWindow_AP'].show()

    def set_plot_spike_threshold(self):
        """
        Create a SetFigWindowVth object to configure visualization settings of spike threshold dynamics data.
        """
        if self.toolBox_calculate_spike_threshold.currentIndex() == 0:
            if self.CurvatureSpikeThreshold is None:
                msg_box = QMessageBox(QMessageBox.Information, 'Message', 'Run first!')
                msg_box.exec()
            else:
                self.names_window['SetFigWindow_Vth'] = SetFigWindowVth(
                    data_operation_module=self.CurvatureSpikeThreshold,
                    main_window=self)
                self.names_window['SetFigWindow_Vth'].show()
        elif self.toolBox_calculate_spike_threshold.currentIndex() == 1:
            if self.rampMethod_window.data:
                self.names_window['SetFigWindow_Vth'] = SetFigWindowVth(data_operation_module=self.rampMethod_window,
                                                                        main_window=self)
                self.names_window['SetFigWindow_Vth'].show()
            else:
                msg_box = QMessageBox(QMessageBox.Information, 'Message', 'Please run first!')
                msg_box.exec()

    def slot_pushButton_set_parameters_features_clicked(self):
        """Create a CalculateFeatureWindow object to calculate spike features, including rate of depolarization (dV/dt)
        and average membrane potential (<V>) preceding to spike onset"""
        self.ParasOfFeaturesWindow = CalculateFeatureWindow(mainWindow=self, data=self.CurvatureSpikeThreshold.data,
                                                            features_option=self.features_option,
                                                            tableWidget=self.tableWidget_features)
        self.ParasOfFeaturesWindow.show()

    @staticmethod
    def add_features_to_TableWidget(tableWidget_features, data):
        """
        Add calculated spike features to table widget.
        """
        tableWidget_features.clear()

        font = tableWidget_features.horizontalHeader().font()
        font.setBold(True)
        tableWidget_features.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Set the vertical title of the table
        tableWidget_features.setRowCount(len(data) - 1)
        row = 0
        for i in data:
            if i == 'All':
                pass
            else:
                item = QTableWidgetItem()
                item.setText(i)
                tableWidget_features.setVerticalHeaderItem(row, item)
                row += 1
        # Set the horizontal title of the table
        # Vth: spike threshold, t_Vth: time of spike threshold, ISI: inter-spike interval, dV/dt:rate of depolarization
        # <V>: average voltage preceding to spike
        col_names = ['Vth', 't_Vth', 'ISI', 'dV/dt', '<V>']
        col_count = 5
        tableWidget_features.setColumnCount(col_count)
        col = 0
        for i in col_names:
            item = QTableWidgetItem()
            item.setText(i)
            tableWidget_features.setHorizontalHeaderItem(col, item)
            tableWidget_features.setColumnWidth(col, 50)
            col += 1
        row = 0
        for i in data:
            if i == 'All':
                pass
            else:
                item_Vth = QTableWidgetItem()
                item_Vth.setText(str(round(data[i]['features']['Vth'][0], 3)))
                tableWidget_features.setItem(row, 0, item_Vth)
                item_t_Vth = QTableWidgetItem()
                item_t_Vth.setText(str(round(data[i]['timestamp']['timestamp_Vth'][0], 3)))
                tableWidget_features.setItem(row, 1, item_t_Vth)
                if 'ISI' in data[i]['features']:
                    item_ISI = QTableWidgetItem()
                    item_ISI.setText(str(round(data[i]['features']['ISI'][0], 3)))
                    tableWidget_features.setItem(row, 2, item_ISI)
                if 'dV/dt' in data[i]['features']:
                    item_dVdt = QTableWidgetItem()
                    item_dVdt.setText(str(round(data[i]['features']['dV/dt'][0], 3)))
                    tableWidget_features.setItem(row, 3, item_dVdt)
                if '<V>' in data[i]['features']:
                    item_average_V = QTableWidgetItem()
                    item_average_V.setText(str(round(data[i]['features']['<V>'][0], 3)))
                    tableWidget_features.setItem(row, 4, item_average_V)
                row += 1
        for i in data.keys():
            if 'k' in i:
                tableWidget_features.removeColumn(2)
                break
        tableWidget_features.horizontalHeader().setStretchLastSection(True)  # Stretch the last column to fill the space
        tableWidget_features.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def slot_update_voltage_option(self):
        """
        Update voltage option (e.g. Vm, Vs, Vd, ...) in the "Vm" drop-down list to extract APs in a specific compartment
        """
        self.comboBox_voltage_option.clear()
        model = self.comboBox_model.currentText().replace(' model', 'model')
        model = importlib.import_module(model)
        compartment_num = model.Model.number_of_compartment
        name_list = []
        if compartment_num == 1:
            name_list = ['Vm']
        elif compartment_num == 2:
            name_list = ['Vs', 'Vd']
        else:
            for i in range(compartment_num):
                name = 'V' + '{}'.format(i + 1)
                name_list.append(name)
        for i in name_list:
            self.comboBox_voltage_option.addItem(i)

    def page_stimulus_init(self):
        model_name_list = get_model_names()
        logging.info(f'Model names: {model_name_list}')
        for i in model_name_list:
            self.comboBox_model.addItem(i.replace('model', ' ') + 'model')
        item_count = self.comboBox_model.count()
        logging.info(f"Number of items in comboBox_model: {item_count}")

        for index in range(item_count):
            item_text = self.comboBox_model.itemText(index)
        self.comboBox_model.repaint()

        self.model_name = self.comboBox_model.currentText().replace(' model', 'model')  #
        model = importlib.import_module(self.model_name)
        compartment_num = model.Model.number_of_compartment
        self.names['tab_stim1'] = self.tab_stim1
        self.names['gridLayout_tab_stim1'] = self.gridLayout_tab_stim1
        self.add_stim_name(compartment_num, self.names, 'stim1')
        self.names['label_stim1_type'] = QLabel(self.names['tab_stim1'])
        self.names['label_stim1_type'].setObjectName("label_stim1_type")
        self.names['label_stim1_type'].setText('Type')
        self.names['gridLayout_tab_stim1'].addWidget(self.names['label_stim1_type'], 2, 1, 1, 1)
        self.names['comboBox_stim1'] = QComboBox(self.names['tab_stim1'])
        self.names['comboBox_stim1'].setObjectName("comboBox_stim1")
        self.names['comboBox_stim1'].addItem("DC")
        self.names['comboBox_stim1'].addItem("AC")
        self.names['comboBox_stim1'].addItem("Ramp")
        self.names['comboBox_stim1'].addItem("OU process")

        self.names['gridLayout_tab_stim1'].addWidget(self.names['comboBox_stim1'], 2, 2, 1, 1)
        self.names['label_stim1_Start'] = QLabel(self.tab_stim1)
        self.names['label_stim1_Start'].setObjectName("label_stim1_Start")
        self.names['label_stim1_Start'].setText("Start (ms)")
        self.names['gridLayout_tab_stim1'].addWidget(self.names['label_stim1_Start'], 3, 1, 1, 1)
        self.names['doubleSpinBox_stim1_start'] = QDoubleSpinBox(self.names['tab_stim1'])
        self.names['doubleSpinBox_stim1_start'].setObjectName("doubleSpinBox_stim1_start")
        self.names['doubleSpinBox_stim1_start'].setMaximum(1000000)
        self.names['doubleSpinBox_stim1_start'].setDecimals(3)
        self.names['gridLayout_tab_stim1'].addWidget(self.names['doubleSpinBox_stim1_start'], 3, 2, 1, 1)
        self.names['label_stim1_Stop'] = QLabel(self.names['tab_stim1'])
        self.names['label_stim1_Stop'].setObjectName('label_stim1_Stop')
        self.names['label_stim1_Stop'].setText("Stop (ms)")
        self.names['gridLayout_tab_stim1'].addWidget(self.names['label_stim1_Stop'], 4, 1, 1, 1)
        self.names['doubleSpinBox_stim1_stop'] = QDoubleSpinBox(self.names['tab_stim1'])
        self.names['doubleSpinBox_stim1_stop'].setObjectName('doubleSpinBox_stim1_stop')

        self.names['gridLayout_tab_stim1'].addWidget(self.names['doubleSpinBox_stim1_stop'], 4, 2, 1, 1)
        self.names['doubleSpinBox_stim1_stop'].setMaximum(1000000)
        self.names['doubleSpinBox_stim1_stop'].setDecimals(3)
        self.names['label_stim1_amplitude'] = QLabel(self.names['tab_stim1'])
        self.names['label_stim1_amplitude'].setObjectName('label_stim1_amplitude')
        self.names['label_stim1_amplitude'].setText("Amplitude (μA/cm<sup>2</sup>)")
        self.names['gridLayout_tab_stim1'].addWidget(self.names['label_stim1_amplitude'], 5, 1, 1, 1)
        self.names['doubleSpinBox_stim1_amplitude'] = QDoubleSpinBox(self.names['tab_stim1'])
        self.names['doubleSpinBox_stim1_amplitude'].setMaximum(1000000)
        self.names['doubleSpinBox_stim1_amplitude'].setMinimum(-1000)
        self.names['doubleSpinBox_stim1_amplitude'].setDecimals(4)
        self.names['doubleSpinBox_stim1_amplitude'].setObjectName('doubleSpinBox_stim1_amplitude')
        self.names['gridLayout_tab_stim1'].addWidget(self.names['doubleSpinBox_stim1_amplitude'], 5, 2, 1, 1)
        self.names['comboBox_stim1'].currentIndexChanged.connect(self.slot_auto_add_widget)

        self.tabWidget_stimulus.setTabsClosable(True)
        self.tabWidget_stimulus.setMovable(True)

        self.tabWidget_stimulus.tabCloseRequested.connect(self.delete_stim_tab)

    def page_canvas_init(self):
        self.gridLayout_widget_fig_simulation = QGridLayout(self.widget_fig_AP)
        self.gridLayout_widget_fig_spike_threshold = QGridLayout(self.widget_fig_Vth)
        """
        Note
        --------
        The figure and canvas are created only once in the main window, which operation should be outside the below 
        'for' loop. Recreating them for each plotting would cause unnecessary duplication of UI elements.
        """
        self.names_fig['fig_AP'] = plt.figure()
        self.names_fig['fig_Vth'] = plt.figure()

        for i in self.names_fig:
            name = i.strip('fig_')
            self.names['Canvas_' + name] = FigureCanvas(self.names_fig[i])
            self.names['mpl_ntb_' + name] = NavigationToolbar(self.names['Canvas_' + name])
            self.names['ax_' + name + '_1'] = self.names_fig[i].add_subplot(221)
            self.names['ax_' + name + '_2'] = self.names_fig[i].add_subplot(222)
            self.names['ax_' + name + '_3'] = self.names_fig[i].add_subplot(223)
            self.names['ax_' + name + '_4'] = self.names_fig[i].add_subplot(224)
            self.names['axes_' + name] = {(1, 1): self.names['ax_' + name + '_1'],
                                          (1, 2): self.names['ax_' + name + '_2'],
                                          (2, 1): self.names['ax_' + name + '_3'],
                                          (2, 2): self.names['ax_' + name + '_4']}
        self.gridLayout_widget_fig_simulation.addWidget(self.names['Canvas_' + 'AP'])
        self.gridLayout_widget_fig_simulation.addWidget(self.names['mpl_ntb_' + 'AP'])
        self.gridLayout_widget_fig_spike_threshold.addWidget(self.names['Canvas_' + 'Vth'])
        self.gridLayout_widget_fig_spike_threshold.addWidget(self.names['mpl_ntb_' + 'Vth'])
        for i in self.names_fig:
            self.names_fig[i].subplots_adjust(top=0.952,
                                              bottom=0.092,
                                              left=0.088,
                                              right=0.983,
                                              hspace=0.311,
                                              wspace=0.246)

    @staticmethod
    def add_stim_name(com_num, names, tab_name):
        if com_num == 1:
            name_list = ['Istim']
        elif com_num == 2:
            name_list = ['Is', 'Id']
        else:
            name_list = []
            for i in range(com_num):
                name = 'Istim' + '{}'.format(i + 1)
                name_list.append(name)
        names['label_' + tab_name + '_name'] = QLabel(names['tab_' + tab_name])
        names['label_' + tab_name + '_name'].setObjectName('label_' + tab_name + '_name')
        names['label_' + tab_name + '_name'].setText('Name')
        names['comboBox_' + tab_name + '_name'] = QComboBox(names['tab_' + tab_name])
        names['comboBox_' + tab_name + '_name'].setObjectName('comboBox_' + tab_name + '_name')
        for i in name_list:
            names['comboBox_' + tab_name + '_name'].addItem(i)
        names['gridLayout_tab_' + tab_name].addWidget(names['label_' + tab_name + '_name'], 1, 1, 1, 1)
        names['gridLayout_tab_' + tab_name].addWidget(names['comboBox_' + tab_name + '_name'], 1, 2, 1, 1)

    def slot_auto_add_widget(self):
        sender_object = self.sender()
        object_name = sender_object.objectName()
        tab_name = object_name.strip('comboBox_')
        tab_objectname = 'tab_' + tab_name
        dic = {}
        dic['label_list'] = self.names[tab_objectname].findChildren(QLabel)
        for i in dic:
            for j in range(len(dic[i])):
                dic[i][j] = dic[i][j].objectName()

        if self.names[object_name].currentIndex() == 0:

            if 'label_' + tab_name + '_frequency' in dic['label_list']:
                self.names['label_' + tab_name + '_frequency'].deleteLater()
                self.names['label_' + tab_name + '_frequency'] = None
                self.names['spinBox_' + tab_name + '_frequency'].deleteLater()
                self.names['spinBox_' + tab_name + '_frequency'] = None
            if 'label_' + tab_name + '_K' in dic['label_list']:
                self.names['label_' + tab_name + '_K'].deleteLater()
                self.names['label_' + tab_name + '_K'] = None
                self.names['doubleSpinBox_' + tab_name + '_K'].deleteLater()
                self.names['doubleSpinBox_' + tab_name + '_K'] = None
            if 'label_' + tab_name + '_mu' in dic['label_list']:
                self.names['label_' + tab_name + '_mu'].deleteLater()
                self.names['doubleSpinBox_' + tab_name + '_mu'].deleteLater()
                self.names['label_' + tab_name + '_mu'] = None
                self.names['doubleSpinBox_' + tab_name + '_mu'] = None
            if 'label_' + tab_name + '_theta' in dic['label_list']:
                self.names['label_' + tab_name + '_theta'].deleteLater()
                self.names['doubleSpinBox_' + tab_name + '_theta'].deleteLater()
                self.names['label_' + tab_name + '_theta'] = None
                self.names['doubleSpinBox_' + tab_name + '_theta'] = None
            if 'label_' + tab_name + '_sigma' in dic['label_list']:
                self.names['label_' + tab_name + '_sigma'].deleteLater()
                self.names['doubleSpinBox_' + tab_name + '_sigma'].deleteLater()
                self.names['label_' + tab_name + '_sigma'] = None
                self.names['doubleSpinBox_' + tab_name + '_sigma'] = None

            if 'label_' + tab_name + '_amplitude' in dic['label_list']:
                pass
            else:
                self.names['label_' + tab_name + '_amplitude'] = QLabel(self.names['tab_' + tab_name])
                self.names['label_' + tab_name + '_amplitude'].setText('Amplitude (μA/cm<sup>2</sup>)')
                self.names['label_' + tab_name + '_amplitude'].setObjectName('label_' + tab_name + '_amplitude')
                self.names['gridLayout_tab_' + tab_name].addWidget(self.names['label_' + tab_name + '_amplitude'], 5, 1,
                                                                   1, 1)
                self.names['doubleSpinBox_' + tab_name + '_amplitude'] = QDoubleSpinBox(self.names['tab_' + tab_name])
                self.names['doubleSpinBox_' + tab_name + '_amplitude'].setObjectName(
                    'doubleSpinBox_' + tab_name + '_amplitude')
                self.names['doubleSpinBox_' + tab_name + '_amplitude'].setMinimum(-1000)
                self.names['doubleSpinBox_' + tab_name + '_amplitude'].setMaximum(1000000)
                self.names['gridLayout_tab_' + tab_name].addWidget(
                    self.names['doubleSpinBox_' + tab_name + '_amplitude'],
                    5, 2, 1, 1)
            dic = {}
            dic['label_list'] = self.names[tab_objectname].findChildren(QLabel)
            for i in dic:
                for j in range(len(dic[i])):
                    dic[i][j] = dic[i][j].objectName()

        elif self.names[object_name].currentIndex() == 1:

            if 'label_' + tab_name + '_K' in dic['label_list']:
                self.names['label_' + tab_name + '_K'].deleteLater()
                self.names['label_' + tab_name + '_K'] = None
                self.names['doubleSpinBox_' + tab_name + '_K'].deleteLater()
                self.names['doubleSpinBox_' + tab_name + '_K'] = None

            if 'label_' + tab_name + '_mu' in dic['label_list']:
                self.names['label_' + tab_name + '_mu'].deleteLater()
                self.names['doubleSpinBox_' + tab_name + '_mu'].deleteLater()
                self.names['label_' + tab_name + '_mu'] = None
                self.names['doubleSpinBox_' + tab_name + '_mu'] = None
            if 'label_' + tab_name + '_theta' in dic['label_list']:
                self.names['label_' + tab_name + '_theta'].deleteLater()
                self.names['doubleSpinBox_' + tab_name + '_theta'].deleteLater()
                self.names['label_' + tab_name + '_theta'] = None
                self.names['doubleSpinBox_' + tab_name + '_theta'] = None
            if 'label_' + tab_name + '_sigma' in dic['label_list']:
                self.names['label_' + tab_name + '_sigma'].deleteLater()
                self.names['doubleSpinBox_' + tab_name + '_sigma'].deleteLater()
                self.names['label_' + tab_name + '_sigma'] = None
                self.names['doubleSpinBox_' + tab_name + '_sigma'] = None
            if 'label_' + tab_name + '_amplitude' in dic['label_list']:
                pass
            else:
                self.names['label_' + tab_name + '_amplitude'] = QLabel(self.names['tab_' + tab_name])
                self.names['label_' + tab_name + '_amplitude'].setText('Amplitude (μA/cm<sup>2</sup>)')
                self.names['label_' + tab_name + '_amplitude'].setObjectName('label_' + tab_name + '_amplitude')
                self.names['gridLayout_tab_' + tab_name].addWidget(self.names['label_' + tab_name + '_amplitude'], 5, 1,
                                                                   1, 1)
                self.names['doubleSpinBox_' + tab_name + '_amplitude'] = QDoubleSpinBox(self.names['tab_' + tab_name])
                self.names['doubleSpinBox_' + tab_name + '_amplitude'].setObjectName(
                    'doubleSpinBox_' + tab_name + '_amplitude')
                self.names['gridLayout_tab_' + tab_name].addWidget(
                    self.names['doubleSpinBox_' + tab_name + '_amplitude'],
                    5, 2, 1, 1)
                self.names['doubleSpinBox_' + tab_name + '_amplitude'].setMinimum(-1000)
                self.names['doubleSpinBox_' + tab_name + '_amplitude'].setMaximum(1000000)
            if 'label_' + tab_name + '_frequency' in dic['label_list']:
                pass
            else:
                self.names['label_' + tab_name + '_frequency'] = QLabel(self.names['tab_' + tab_name])
                self.names['label_' + tab_name + '_frequency'].setText("Frequency (Hz)")
                self.names['label_' + tab_name + '_frequency'].setObjectName('label_' + tab_name + '_frequency')
                self.names['gridLayout_tab_' + tab_name].addWidget(self.names['label_' + tab_name + '_frequency'], 6, 1,
                                                                   1, 1)
                self.names['spinBox_' + tab_name + '_frequency'] = QSpinBox(self.names['tab_' + tab_name])
                self.names['spinBox_' + tab_name + '_frequency'].setObjectName('spinBox_stim1_frequency')
                self.names['gridLayout_tab_' + tab_name].addWidget(self.names['spinBox_' + tab_name + '_frequency'], 6,
                                                                   2, 1, 1)
            dic = {}
            dic['label_list'] = self.names[tab_objectname].findChildren(QLabel)
            for i in dic:
                for j in range(len(dic[i])):
                    dic[i][j] = dic[i][j].objectName()

        elif self.names[object_name].currentIndex() == 2:

            if 'label_' + tab_name + '_frequency' in dic['label_list']:
                self.names['label_' + tab_name + '_frequency'].deleteLater()
                self.names['label_' + tab_name + '_frequency'] = None
                self.names['spinBox_' + tab_name + '_frequency'].deleteLater()
                self.names['spinBox_' + tab_name + '_frequency'] = None
            if 'label_' + tab_name + '_amplitude' in dic['label_list']:
                self.names['label_' + tab_name + '_amplitude'].deleteLater()
                self.names['label_' + tab_name + '_amplitude'] = None
                self.names['doubleSpinBox_' + tab_name + '_amplitude'].deleteLater()
                self.names['doubleSpinBox_' + tab_name + '_amplitude'] = None
            if 'label_' + tab_name + '_mu' in dic['label_list']:
                self.names['label_' + tab_name + '_mu'].deleteLater()
                self.names['doubleSpinBox_' + tab_name + '_mu'].deleteLater()
                self.names['label_' + tab_name + '_mu'] = None
                self.names['doubleSpinBox_' + tab_name + '_mu'] = None
            if 'label_' + tab_name + '_theta' in dic['label_list']:
                self.names['label_' + tab_name + '_theta'].deleteLater()
                self.names['doubleSpinBox_' + tab_name + '_theta'].deleteLater()
                self.names['label_' + tab_name + '_theta'] = None
                self.names['doubleSpinBox_' + tab_name + '_theta'] = None
            if 'label_' + tab_name + '_sigma' in dic['label_list']:
                self.names['label_' + tab_name + '_sigma'].deleteLater()
                self.names['doubleSpinBox_' + tab_name + '_sigma'].deleteLater()
                self.names['label_' + tab_name + '_sigma'] = None
                self.names['doubleSpinBox_' + tab_name + '_sigma'] = None

            if 'label_' + tab_name + '_K' in dic['label_list']:
                pass
            else:
                self.names['label_' + tab_name + '_K'] = QLabel(self.names['tab_' + tab_name])
                self.names['label_' + tab_name + '_K'].setText("Slope (mV/ms)")
                self.names['label_' + tab_name + '_K'].setObjectName('label_' + tab_name + '_K')
                self.names['gridLayout_tab_' + tab_name].addWidget(self.names['label_' + tab_name + '_K'], 6, 1,
                                                                   1, 1)
                self.names['doubleSpinBox_' + tab_name + '_K'] = QDoubleSpinBox(self.names['tab_' + tab_name])
                self.names['doubleSpinBox_' + tab_name + '_K'].setObjectName(
                    'doubleSpinBox_' + tab_name + '_K')
                self.names['gridLayout_tab_' + tab_name].addWidget(
                    self.names['doubleSpinBox_' + tab_name + '_K'],
                    6, 2, 1, 1)
            dic = {}
            dic['label_list'] = self.names[tab_objectname].findChildren(QLabel)
            for i in dic:
                for j in range(len(dic[i])):
                    dic[i][j] = dic[i][j].objectName()
        elif self.names[object_name].currentIndex() == 3:
            if 'label_' + tab_name + '_frequency' in dic['label_list']:
                self.names['label_' + tab_name + '_frequency'].deleteLater()
                self.names['label_' + tab_name + '_frequency'] = None
                self.names['spinBox_' + tab_name + '_frequency'].deleteLater()
                self.names['spinBox_' + tab_name + '_frequency'] = None
            if 'label_' + tab_name + '_amplitude' in dic['label_list']:
                self.names['label_' + tab_name + '_amplitude'].deleteLater()
                self.names['label_' + tab_name + '_amplitude'] = None
                self.names['doubleSpinBox_' + tab_name + '_amplitude'].deleteLater()
                self.names['doubleSpinBox_' + tab_name + '_amplitude'] = None
            if 'label_' + tab_name + '_K' in dic['label_list']:
                self.names['label_' + tab_name + '_K'].deleteLater()
                self.names['label_' + tab_name + '_K'] = None
                self.names['doubleSpinBox_' + tab_name + '_K'].deleteLater()
                self.names['doubleSpinBox_' + tab_name + '_K'] = None

            if 'label_' + tab_name + '_mu' in dic['label_list']:
                pass
            else:
                self.names['label_' + tab_name + '_mu'] = QLabel(self.names['tab_' + tab_name])
                self.names['label_' + tab_name + '_mu'].setText("μ")
                self.names['label_' + tab_name + '_mu'].setObjectName('label_' + tab_name + '_mu')
                self.names['gridLayout_tab_' + tab_name].addWidget(self.names['label_' + tab_name + '_mu'], 5, 1,
                                                                   1, 1)
                self.names['doubleSpinBox_' + tab_name + '_mu'] = QDoubleSpinBox(self.names['tab_' + tab_name])
                self.names['doubleSpinBox_' + tab_name + '_mu'].setObjectName(
                    'doubleSpinBox_' + tab_name + '_mu')
                self.names['gridLayout_tab_' + tab_name].addWidget(
                    self.names['doubleSpinBox_' + tab_name + '_mu'],
                    5, 2, 1, 1)
                self.names['label_' + tab_name + '_theta'] = QLabel(self.names['tab_' + tab_name])
                self.names['label_' + tab_name + '_theta'].setText("τ")
                self.names['label_' + tab_name + '_theta'].setObjectName('label_' + tab_name + '_theta')
                self.names['gridLayout_tab_' + tab_name].addWidget(self.names['label_' + tab_name + '_theta'], 6, 1,
                                                                   1, 1)
                self.names['doubleSpinBox_' + tab_name + '_theta'] = QDoubleSpinBox(self.names['tab_' + tab_name])
                self.names['doubleSpinBox_' + tab_name + '_theta'].setObjectName(
                    'doubleSpinBox_' + tab_name + '_theta')
                self.names['gridLayout_tab_' + tab_name].addWidget(
                    self.names['doubleSpinBox_' + tab_name + '_theta'],
                    6, 2, 1, 1)
                self.names['label_' + tab_name + '_sigma'] = QLabel(self.names['tab_' + tab_name])
                self.names['label_' + tab_name + '_sigma'].setText("σ")
                self.names['label_' + tab_name + '_sigma'].setObjectName('label_' + tab_name + '_sigma')
                self.names['gridLayout_tab_' + tab_name].addWidget(self.names['label_' + tab_name + '_sigma'], 7, 1,
                                                                   1, 1)
                self.names['doubleSpinBox_' + tab_name + '_sigma'] = QDoubleSpinBox(self.names['tab_' + tab_name])
                self.names['doubleSpinBox_' + tab_name + '_sigma'].setObjectName(
                    'doubleSpinBox_' + tab_name + '_sigma')
                self.names['gridLayout_tab_' + tab_name].addWidget(
                    self.names['doubleSpinBox_' + tab_name + '_sigma'],
                    7, 2, 1, 1)
            dic = {}
            dic['label_list'] = self.names[tab_objectname].findChildren(QLabel)
            for i in dic:
                for j in range(len(dic[i])):
                    dic[i][j] = dic[i][j].objectName()
