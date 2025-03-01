import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def multivariate_normal_density(x, mean, cov):
    """
    手动计算多维正态分布的概率密度函数。

    :param x: 数据点数组，形状为 (n, d)，其中 n 是点数，d 是变量数。
    :param mean: 均值向量，长度为 d。
    :param cov: 协方差矩阵，形状为 (d, d)。
    :return: 概率密度值数组，长度为 n。
    """
    cov = np.array(cov)  # 确保 cov 是 NumPy 数组
    d = len(mean)  # 变量数
    cov_inv = np.linalg.inv(cov)  # 协方差矩阵的逆
    cov_det = np.linalg.det(cov)  # 协方差矩阵的行列式
    norm_factor = 1 / ((2 * np.pi) ** (d / 2) * np.sqrt(cov_det))  # 正态分布的归一化系数

    # 计算密度
    diff = x - mean  # 每个点减去均值
    exponent = -0.5 * np.sum(diff @ cov_inv * diff, axis=1)  # 指数项
    return norm_factor * np.exp(exponent)


def plot_multivariate_normal_3d(mean, cov, n_points=100):
    """
    绘制二维正态分布的三维概率密度曲面图。

    :param mean: 均值向量 (长度为2的数组)。
    :param cov: 协方差矩阵 (2x2矩阵)。
    :param n_points: 网格点数。
    """
    cov = np.array(cov)  # 确保 cov 是 NumPy 数组

    # 创建网格
    x = np.linspace(mean[0] - 3 * np.sqrt(cov[0, 0]), mean[0] + 3 * np.sqrt(cov[0, 0]), n_points)
    y = np.linspace(mean[1] - 3 * np.sqrt(cov[1, 1]), mean[1] + 3 * np.sqrt(cov[1, 1]), n_points)
    X, Y = np.meshgrid(x, y)

    # 将网格点合并为形状 (n, 2) 的数组
    points = np.column_stack([X.ravel(), Y.ravel()])

    # 计算每个点的密度
    Z = multivariate_normal_density(points, mean, cov).reshape(X.shape)

    # 绘制三维曲面图
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k', alpha=0.8)

    # 添加标签和标题
    ax.set_title("Multivariate Normal Distribution Surface (3D)")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Probability Density")
    plt.show()


# 示例：设置二维正态分布的参数
mean = [0, 0]  # 均值向量
cov = [[1, 0], [0, 1]]  # 协方差矩阵

# 调用函数绘制三维图
plot_multivariate_normal_3d(mean, cov)
