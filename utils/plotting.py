"""Class and functions for handling plotting operations"""
import copy
import logging
import numpy as np
from PySide6.QtWidgets import QMessageBox
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression


class Plotting:
    """
    A class for performing plotting operations:
    1. Plot curves: phase portrait, time series plot.
    2. Scatter plot: threshold points.
    3. Fill-between: threshold region display.
    4. Linear fitting.
    """

    def __init__(self, data, figure_set, axes):
        """
        The parameter figure_set is a dynamic dictionary used to store configuration information for plotting operations
        Its structure is as follows:
            figure_set={(1,1):{'Vth_points':True,'1':{'x':{...},'y':{...},'Linear_fitting':True},'2':...,...}
                        (1,2):{...},(2,1):{...},(2,2):{...}}
            Keys:   (x, y) represents the coordinates of the subplot, where x and y are integers specifying the position
                    of the subplot on the canvas.
            Values: The value at each subplot position is another dictionary containing different plotting operations
                    and their associated data:
                        Vth_points, Vth_range, and Linear_fitting are flags indicating whether the corresponding operations
                    (such as threshold marking, threshold range display, and linear fitting) are enabled.
                    Subdictionary (`'1': {'x': {...}, 'y': {...}}`) stores the information of coordinates in each plot of its corresponding figure.
        """
        # 1. Update figure_set
        figure_set_copy = copy.deepcopy(figure_set)
        for order_1 in figure_set_copy:
            for order_2 in figure_set_copy[order_1]:
                if order_2 == 'Vth_points' or order_2 == 'Vth_range':
                    pass
                else:
                    self.update_figure_set(data=data, figure_set=figure_set, order_1=order_1, order_2=order_2)

        # 2. Clear all existing plots in axes
        self.clear_axes(axes=axes)

        # 3、Plot portraits
        Vth_name = ['Vth']
        superposition_name = ['V_superposition', 'timestamp_superposition']
        for order_1 in axes.keys():
            flag_mark_threshold_range = 0
            for order_2 in figure_set[order_1].keys():
                if order_2 == 'Vth_points':
                    # Mark threshold points
                    mark_threshold_point(order_1, figure_set, data, axes)

                elif order_2 == 'Vth_range':
                    # Display threshold range
                    flag_mark_threshold_range = 1
                else:
                    x, y, label, x_name, y_name = get_x_y_data(data=data, figure_set=figure_set, order_1=order_1,
                                                               order_2=order_2)
                    # Mark threshold points
                    if x_name in Vth_name or y_name in Vth_name:
                        self.axes_scatter(axes=axes[order_1], x=x, y=y, label=label)
                        if 'Linear_fitting' in figure_set[order_1][order_2]:
                            linear_fitting(x=x, y=y, axes=axes[order_1])
                    # Plot action potential superpositions
                    elif x_name in superposition_name or y_name in superposition_name:
                        if x_name in superposition_name and y_name in superposition_name:
                            for i in range(len(x)):
                                self.axes_plot(axes=axes[order_1], x=x[i], y=y[i])
                    # Plot time series or phase portrait
                    else:
                        self.axes_plot(axes=axes[order_1], x=x, y=y, label=label)
                        if 'Linear_fitting' in figure_set[order_1][order_2]:
                            linear_fitting(x=x, y=y, axes=axes[order_1])
                    if label:
                        axes[order_1].legend()
            if flag_mark_threshold_range == 1:
                mark_threshold_range(order_1, figure_set, data, axes)


    @staticmethod
    def clear_axes(axes):
        for i in axes:
            axes[i].cla()

    @staticmethod
    def axes_plot(axes, x, y, label=None):
        axes.plot(x, y, label=label)

    @staticmethod
    def axes_scatter(axes, x, y, label):
        axes.scatter(x, y, label=label, color='r', marker='o', s=6, zorder=10)

    @staticmethod
    def axes_fill_between(axes, Vth_range, y_min, y_max):
        axes.vlines([Vth_range[0], Vth_range[1]], y_min, y_max, color='k', zorder=3)
        axes.fill_between([Vth_range[0], Vth_range[1]], y_min, y_max, color='green',
                          alpha=0.3)

    @staticmethod
    def update_figure_set(data, figure_set, order_1, order_2):
        """
        Update the figure_set to ensure the same shape of the coordinates in each plot of figure_set dictionary
        """
        x_all = figure_set[order_1][order_2]['x']
        y_all = figure_set[order_1][order_2]['y']
        keys_1 = data.keys()
        if x_all[0] in keys_1 and y_all[0] in keys_1:
            keys_2_x = data[x_all[0]].keys()
            keys_2_y = data[y_all[0]].keys()
            if x_all[1] in keys_2_x and y_all[1] in keys_2_y:
                if len(x_all) == 3:
                    keys_3_x = data[x_all[0]][x_all[1]].keys()
                    keys_3_y = data[y_all[0]][y_all[1]].keys()
                    if x_all[2] in keys_3_x and y_all[2] in keys_3_y:
                        if plotting_condition_check(data=data, x_all=x_all, y_all=y_all):
                            pass
                        else:
                            figure_set[order_1].pop(order_2)

                    else:
                        figure_set[order_1].pop(order_2)

                else:
                    if plotting_condition_check(data=data, x_all=x_all, y_all=y_all):
                        pass
                    else:
                        figure_set[order_1].pop(order_2)

            else:
                figure_set[order_1].pop(order_2)

        else:
            figure_set[order_1].pop(order_2)


def get_x_y_data(data, figure_set, order_1, order_2):
    """
    Retrieves x and y data from data based on figure_set settings
    """
    x_all = figure_set[order_1][order_2]['x']
    x_1 = x_all[0]
    x_2 = x_all[1]
    y_all = figure_set[order_1][order_2]['y']
    y_1 = y_all[0]
    y_2 = y_all[1]
    label = figure_set[order_1][order_2]['label']
    if len(x_all) == 2:
        x = data[x_1][x_2]
        y = data[y_1][y_2]
        return x, y, label, x_2, y_2
    else:
        x_3 = x_all[2]
        y_3 = y_all[2]
        x = data[x_1][x_2][x_3]
        y = data[y_1][y_2][y_3]
        return x, y, label, x_3, y_3


def plotting_condition_check(data, x_all, y_all):
    if len(x_all) == 2:
        if len(data[x_all[0]][x_all[1]]) == len(data[y_all[0]][y_all[1]]):
            return True
        else:
            msg_box = QMessageBox(QMessageBox.Information, 'Message',
                                  '{} and {} have different shape'.format(x_all, y_all))
            msg_box.exec()
            return False
    else:
        if len(data[x_all[0]][x_all[1]][x_all[2]]) == len(data[y_all[0]][y_all[1]][y_all[2]]):
            return True
        else:
            msg_box = QMessageBox(QMessageBox.Information, 'Message',
                                  '{} and {} have different shape'.format(x_all, y_all))
            msg_box.exec()
            return False


def mark_threshold_point(order_1, figure_set, data, axes):
    """
    Indicate the spike onset in a phase space
    """
    for order_2 in figure_set[order_1].keys():
        if order_2 == 'Vth_points' or order_2 == 'Vth_range':
            pass
        else:
            x_name_1 = figure_set[order_1][order_2]['x'][0]
            x_name_2 = figure_set[order_1][order_2]['x'][1]
            x_name_3 = figure_set[order_1][order_2]['x'][2]
            y_name_1 = figure_set[order_1][order_2]['y'][0]
            y_name_2 = figure_set[order_1][order_2]['y'][1]
            y_name_3 = figure_set[order_1][order_2]['y'][2]
            if 'All' in x_name_1 or 'All' in y_name_1:
                pass
            else:
                if x_name_1 == y_name_1:
                    timestamp = data[x_name_1]['timestamp']['timestamp']
                    timestamp_Vth = data[x_name_1]['timestamp']['timestamp_Vth']
                    index_Vth = np.where(timestamp == timestamp_Vth)[0][0]
                    x = data[x_name_1][x_name_2][x_name_3][index_Vth]
                    y = data[y_name_1][y_name_2][y_name_3][index_Vth]
                    axes[order_1].scatter(x, y, color='r', marker='o', s=6, zorder=10)


def mark_threshold_range(order_1, figure_set, data, axes):
    """
    Marks the spike threshold region
    """
    array_list = []
    Vth_list = []
    for order_2 in figure_set[order_1].keys():
        if order_2 == 'Vth_points' or order_2 == 'Vth_range':
            pass
        else:
            x_name_1 = figure_set[order_1][order_2]['x'][0]
            y_name_1 = figure_set[order_1][order_2]['y'][0]
            y_name_2 = figure_set[order_1][order_2]['y'][1]
            y_name_3 = figure_set[order_1][order_2]['y'][2]
            if 'All' in x_name_1 or 'All' in y_name_1:
                pass
            else:
                if x_name_1 == y_name_1:
                    Vth = data[x_name_1]['features']['Vth']
                    Vth_list.append(Vth)
                    array = copy.deepcopy(data[y_name_1][y_name_2][y_name_3])
                    array_list = np.hstack((array_list, array))
    if Vth_list:
        Vth_min = min(Vth_list)
        Vth_max = max(Vth_list)
        y_min = np.min(array_list)
        y_max = np.max(array_list)
        axes[order_1].fill_between([Vth_min, Vth_max], y_min, y_max, color='green',
                                   alpha=0.3)


def linear_fitting(x, y, axes):
    """
    Performs linear fitting on the given data and plots the fit.
    """
    R = np.corrcoef(x, y)[0, 1]
    x = np.array(x)
    y = np.array(y)
    model = LinearRegression()
    model.fit(x.reshape(-1, 1), y.reshape(-1, 1))
    coef = model.coef_[0, 0]
    intercept = model.intercept_[0]
    X = x
    Y = X * coef + intercept
    axes.plot(X, Y)
    axes.set_title('slope={}, r={}'.format(round(coef, 3), round(R, 3)), loc='right')
    logging.info(f'The equation of linear regression fit is y={coef}x+{intercept}')
    logging.info(f'The Pearson correlation coefficient is {R}')
