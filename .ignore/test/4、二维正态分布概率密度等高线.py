import numpy as np
import matplotlib.pyplot as plt


def multivariate_normal_density(x, mean, cov):
    """
    手动计算多维正态分布的概率密度函数。
    """
    cov = np.array(cov)  # 确保 cov 是 NumPy 数组
    d = len(mean)
    cov_inv = np.linalg.inv(cov)
    cov_det = np.linalg.det(cov)
    norm_factor = 1 / ((2 * np.pi) ** (d / 2) * np.sqrt(cov_det))
    diff = x - mean
    exponent = -0.5 * np.sum(diff @ cov_inv * diff, axis=1)
    return norm_factor * np.exp(exponent)


def plot_multivariate_normal_contours_manual(mean, cov, n_points=100):
    """
    手动计算并绘制二维正态分布概率密度函数的等高线图。
    """
    cov = np.array(cov)  # 确保 cov 是 NumPy 数组
    x = np.linspace(mean[0] - 3 * np.sqrt(cov[0, 0]), mean[0] + 3 * np.sqrt(cov[0, 0]), n_points)
    y = np.linspace(mean[1] - 3 * np.sqrt(cov[1, 1]), mean[1] + 3 * np.sqrt(cov[1, 1]), n_points)
    X, Y = np.meshgrid(x, y)
    points = np.column_stack([X.ravel(), Y.ravel()])
    Z = multivariate_normal_density(points, mean, cov).reshape(X.shape)
    plt.rcParams['savefig.dpi'] = 400
    plt.figure(figsize=(3.5, 2.625))
    contour = plt.contour(X, Y, Z, levels=10, cmap='viridis')
    plt.colorbar(contour)
    plt.title("∑=[[1,0],[0,3]]")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.axis('equal')
    plt.grid(True)
    plt.show()


# 示例：设置二维正态分布的参数
mean = [0, 0]
cov = [[1, 0], [0, 3]]
plot_multivariate_normal_contours_manual(mean, cov)
