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

        # 创建子控件
        label = QLabel(self)
        label.setText("xxx")

# 1. 创建一个应用程序对象
app =  QApplication(sys.argv)

# 2. 控件的操作
# 2.1 通过调用Window类创建控件
window = Window()

# 2.2 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())