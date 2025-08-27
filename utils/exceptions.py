# 自定义异常，用于中断优化过程
class OptimizationInterruptedException(Exception):
    """当优化被用户中断时抛出的异常"""
    pass
