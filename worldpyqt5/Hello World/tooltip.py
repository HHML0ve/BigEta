# -*- coding:utf-8 -*-
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 设置字体与大小
        QToolTip.setFont(QFont('SansSerif', 10))

        # 创建提示框，提示内容可以使用富文本
        self.setToolTip('This is a <b>Qwidget</b> widget')

        # 设置一个按钮，链接事件如果点击按钮就退出。
        # 创建提示框，提示内容使用富文本，重新设置提示框大小，移动提示框
        btn = QPushButton('Button', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        # 移动控件，设置控件标题，在桌面显示控件
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips/ click quit')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    e = Example()
    sys.exit(app.exec_())
