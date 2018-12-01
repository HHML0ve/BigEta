# -*- coding:utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        btn1 = QPushButton('button 1', self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        # 把按钮的点击事件同slot（用户自己写的函数）绑定在一起
        btn1.clicked.connect(self.button_clicked)
        btn2.clicked.connect(self.button_clicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def button_clicked(self):
        sender = self.sender()

        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()

    sys.exit(app.exec_())
