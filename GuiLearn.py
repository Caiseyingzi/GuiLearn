# 0. 导入需要的包和模块

from PyQt5.Qt import *
import sys

# 导入模块，注意用from
from Menu import Window

# 1. 创建一个应用程序对象
app =  QApplication(sys.argv)

# 2. 控件的操作
# 2.1 通过调用Window类创建控件
window = Window()

# 2.2 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())

