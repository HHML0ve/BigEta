# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.resize(300, 300)
        # 调用自己写的函数
        self.center()
        self.setWindowTitle('windows center')
        self.show()

    def center(self):
        # 得到主窗体的大小
        qr = self.frameGeometry()
        # 得到屏幕的大小，中心位置
        cp = QDesktopWidget().availableGeometry().center()
        # 获取显示器的分辨率，得到中间点的位置
        qr.moveCenter(cp)
        # 把窗口的中心店位置放置到qr的中心点
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    e = Example()

    sys.exit(app.exec_())
