from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QIcon, QPixmap, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        transparent_pixmap = QPixmap(32, 32)  # 创建一个 32x32 的透明图标
        transparent_pixmap.fill(Qt.transparent)  # 使其完全透明
        self.setWindowIcon(QIcon(transparent_pixmap))  # 设置为透明图标
        # 将窗口图标设置为空
        self.setWindowIcon()  # 清除图标

# 创建应用程序实例
app = QApplication([])
window = MainWindow()
window.show()

# 运行应用程序
app.exec()
