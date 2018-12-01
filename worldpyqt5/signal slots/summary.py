# -*- coding:utf-8 -*-
import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import (QWidget, QApplication)


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.display = QtWidgets.QLineEdit('0')
        self.text = '0'
        self.string = ''
        self.number = ''

        self.init()

    def init(self):
        self.setWindowTitle('简单计算器')
        # ？ QtWidgets.QGridLayout() 和 QGridLayout() 有什么区别
        grid = QtWidgets.QGridLayout()
        self.display.setFont(QtGui.QFont("Times", 20))
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)  # 设置文本位置，这里设置为右边开始
        self.display.setMaxLength(15)  # 设置最大的长度
        grid.addWidget(self.display, 0, 0, 1, 4)

        names = ['Cls', 'Back', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        pos = [(i, j) for i in range(1, 6) for j in range(4)]
        for position, name in zip(pos, names):

            button = QtWidgets.QPushButton(name)
            button.setFixedSize(QtCore.QSize(60, 30))
            button.clicked.connect(self.button_clicked)  # 给每个按钮设置信号/槽
            if name == '':
                continue
            grid.addWidget(button, *position)
        self.setLayout(grid)

        # pos = [(i, j) for i in range(5) for j in range(4)]
        # c = 0
        # for name in names:
        #     button = QtWidgets.QPushButton(name)
        #     button.setFixedSize(QtCore.QSize(60, 30))
        #     button.clicked.connect(self.button_clicked)  # 给每个按钮设置信号/槽
        #     if name == '':
        #         continue
        #         # grid.addWidget(QtWidgets.QLabel(''), 0, 2) #替换 第三个按钮 为 文本标签！
        #     grid.addWidget(button, pos[c][0] + 1, pos[c][1])
        #     print(pos[c][0] + 1, pos[c][1])
        #     c = c + 1
        # self.setLayout(grid)

    def button_clicked(self):
        sender = self.sender()
        text = sender.text()
        if text == '=':
            self.string = self.string + self.number
            self.number = str(eval(self.string))
            self.string = ''
        elif text in '+-*/':
            self.string = self.string + self.number + text
            self.number = '0'  # 清空数字
        elif text == "Back":
            self.number = self.number[0: -1]  # 删去最后一位
        elif text == "Cls":
            self.number = "0"
        elif text == "Close":
            self.close()
        else:
            if self.number == '0':
                self.number = ''
            self.number = self.number + text

        self.display.setText(self.number)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    e.show()
    sys.exit(app.exec_())
