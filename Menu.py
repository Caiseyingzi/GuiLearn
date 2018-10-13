# 0. 导入需要的包和模块

from PyQt5.Qt import *
import sys

# Window类继承QWidget
class Window(QWidget):
    def __init__(self):
        super().__init__()

        # 在类内部调用自己，设置控制
        self.setWindowTitle("QLabel的学习")
        self.resize(500, 500)
        self.setup_ui()

    # 把子控件设置成一个方法
    def setup_ui(self):
        label = QLabel(self)
        label.setText("xxx")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())