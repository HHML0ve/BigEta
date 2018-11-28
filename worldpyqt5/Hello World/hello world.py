# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # sys.argv是一组命令行参数的列表
    app = QApplication(sys.argv)

    # 新建一个控件， 设置大小，设置位置，设置名称，在桌面上显示控件
    w = QWidget()
    w.resize(400, 600)
    w.move(0, 0)

    # w.setGeometry(400, 600, 0, 0)
    w.setWindowTitle('Hello World')
    w.show()

    # 退出主循环
    sys.exit(app.exec_())
