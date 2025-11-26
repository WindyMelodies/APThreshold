import time
from collections import deque
import numpy as np


class PSO:
    def __init__(self, dim, lb, ub, pop_size=25, w_ini=0.9, w_fin=0.4, c1=1.5, c2=1.5, velocity_clamp=None):
        """
        粒子群优化算法 (PSO)，传入所需参数

        Args:
            dim: 问题的维度。
            pop_size: 粒子群数量。
            lb: 搜索空间的下界（列表或 NumPy 数组）。
            ub: 搜索空间的上界（列表或 NumPy 数组）。
            w_ini: 初始惯性权重。
            w_fin: 最终惯性权重。
            c1: 个体学习因子。
            c2: 群体学习因子。
            velocity_clamp: 速度钳制边界，一个包含 (min_vel, max_vel) 的元组。
        """
        self.dim = dim
        self.pop_size = pop_size

        # 确保边界是 NumPy 数组以便于向量化操作
        self.lb = np.array(lb)
        self.ub = np.array(ub)

        # 惯性权重参数
        self.w_ini = w_ini
        self.w_fin = w_fin
        self.c1 = c1
        self.c2 = c2

        # 种群位置：在指定边界内随机初始化
        self.x = np.random.uniform(
            low=self.lb, high=self.ub, size=(self.pop_size, self.dim)
        )

        # 种群速度：随机初始化，并应用速度钳制
        if velocity_clamp:
            min_velocity, max_velocity = velocity_clamp
            self.velocity = np.random.uniform(min_velocity, max_velocity, size=(self.pop_size, self.dim))
        else:
            # 如果未指定，通常将初始速度设为0或较小的随机值
            self.velocity = np.zeros((self.pop_size, self.dim))

        self.x_best = None  # 全局最优位置
        self.f_best = np.inf  # 全局最优目标函数值，初始设为无穷大
        self.x_i_best = None  # 粒子个体历史最优位置
        self.f_i_best = None  # 粒子个体历史最优目标函数值

    def optimize(self, objective_func, max_iter=100, ftol=1e-4, ftol_iter=5, kwargs=None):
        """
        运行PSO优化过程
        两种终止条件
        （1）运行至最大迭代次数
        （2）目标函数值收敛，在ftol_iter次迭代中的幅度变化小于收敛容差ftol
        Args:
            objective_func: 目标函数
            max_iter: 最大迭代次数
            ftol: 收敛容差，当最佳目标函数值的变化小于此值时，视为收敛
            ftol_iter: 连续满足收敛条件的迭代次数
            **kwargs: 目标函数的额外参数
        """
        # 初始化个体历史最佳位置和值
        self.f_i_best = []
        for i in range(self.pop_size):
            temp = objective_func(self.x[i], kwargs)
            self.f_i_best.append(temp)
        self.x_i_best = self.x.copy()

        # 初始化全局最佳位置和值
        min_f_i_best = np.min(self.f_i_best)
        if min_f_i_best < self.f_best:
            self.f_best = min_f_i_best
            self.x_best = self.x_i_best[np.argmin(self.f_i_best)].copy()

        start_time = time.time()

        # 用于跟踪收敛历史
        ftol_history = deque(maxlen=ftol_iter)

        # 记录前一次的最佳成本
        previous_best_cost = self.f_best

        for iter_num in range(1, max_iter + 1):
            # 动态更新惯性权重 w
            w = self.w_handler(iter_num=iter_num, max_iter=max_iter)

            # 更新粒子速度
            r1 = np.random.rand(self.pop_size, self.dim)
            r2 = np.random.rand(self.pop_size, self.dim)
            self.velocity = (w * self.velocity +
                             self.c1 * r1 * (self.x_i_best - self.x) +
                             self.c2 * r2 * (self.x_best - self.x))

            # 更新粒子位置
            self.x = self.x + self.velocity

            # 处理边界条件
            self.x = self.x_handler(self.x)

            # 更新个体和全局最佳位置
            for i in range(self.pop_size):
                f_i = objective_func(self.x[i], kwargs)
                if f_i < self.f_i_best[i]:
                    self.f_i_best[i] = f_i
                    self.x_i_best[i] = self.x[i].copy()

            # 使用向量化操作更新全局最佳
            min_f_i_best = np.min(self.f_i_best)
            if min_f_i_best < self.f_best:
                self.f_best = min_f_i_best
                self.x_best = self.x_i_best[np.argmin(self.f_i_best)].copy()

            end_time = time.time()
            duration = end_time - start_time
            print(f"迭代次数: {iter_num}, 最佳目标函数值: {self.f_best}, 所用时间: {duration:.2f}秒")

            # 检查收敛条件
            delta = abs(self.f_best - previous_best_cost) < ftol
            ftol_history.append(delta)

            # 终止条件
            # 情况 (1) 和 (3) 的逻辑：运行至最大迭代次数
            if iter_num >= max_iter:
                print(f"达到最大迭代次数 {max_iter}，终止优化。")
                break

            # 情况 (2) 和 (3) 的逻辑：目标值收敛
            if len(ftol_history) == ftol_iter and all(ftol_history):
                print(f"目标函数值已收敛，在连续 {ftol_iter} 次迭代中变化小于 {ftol}，终止优化。")
                break

            # 更新前一次的最佳成本
            previous_best_cost = self.f_best
        print("\n==========================")
        print("优化完成！")
        print(f"最终找到的最佳解（函数值）: {self.f_best}")
        print(f"最终找到的最佳解（位置）: {self.x_best}")
        print("==========================")
        return self.f_best, self.x_best

    def w_handler(self, iter_num, max_iter):
        """
        处理惯性权重w，使用线性递减策略。
        """
        # 如果w_ini和w_fin相同，则w为常数
        if self.w_ini == self.w_fin:
            return self.w_ini
        # 否则使用线性递减公式
        return self.w_ini - (self.w_ini - self.w_fin) * (iter_num / max_iter)

    def x_handler(self, x):
        """
        处理粒子位置的边界条件，将超出边界的粒子截断到最近的边界。
        """
        x_clipped = np.clip(x, self.lb, self.ub)
        return x_clipped

def sphere_function(x):
    """
    多维球形函数，用于测试优化算法。
    Args:
        x: 一个 NumPy 数组，代表粒子的位置。
    Returns:
        float: 函数值，即适应度值。
    """
    return np.sum(x ** 2)
def rastrigin_function(x):
    """
    Rastrigin 函数，一个经典的多峰值测试函数。
    Args:
        x: 一个 NumPy 数组，代表粒子的位置。
    Returns:
        float: 函数值，即适应度值。
    """
    n = len(x)
    return 10 * n + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))


if __name__ == "__main__":
    # 测试程序
    # 2. 设置PSO参数
    # 问题维度
    dim = 7
    # 粒子数量
    pop_size = 10 * dim
    # 搜索空间边界
    lb = -40 * np.ones(dim)  # 使用Rastrigin函数的标准边界
    ub = 40 * np.ones(dim)
    # 最大迭代次数
    max_iter = 5000
    # 惯性权重
    # 将初始惯性权重 w_ini 设置得更高，以便在初始阶段让粒子有更强的随机性和更大的步长来探索整个搜索空间。
    w_ini = 1.0
    w_fin = 0.4
    # 学习因子
    c1 = 2.0
    c2 = 1.5
    
    pso_optimizer = PSO(
        dim=dim,
        pop_size=pop_size,
        lb=lb,
        ub=ub,
        w_ini=w_ini,
        w_fin=w_fin,
        c1=c1,
        c2=c2
    )
    # 4. 运行优化并打印结果
    pso_optimizer.optimize(objective_func=rastrigin_function,max_iter=max_iter,ftol=-1 )
