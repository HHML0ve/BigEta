# -*- coding:utf-8 -*-
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QGridLayout,
                             QVBoxLayout, QHBoxLayout, QGroupBox, QLabel)


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.text = '0'
        self.label = None

        self.init()

    def init(self):
        self.createGridGroupBox()
        self.createVboxGroupBox()

        # 主布局为垂直布局
        main_layout = QHBoxLayout()
        # 添加一个水平布局和一个栅格布局
        v_box_layout = QVBoxLayout()
        v_box_layout.addStretch(10)
        v_box_layout.addWidget(self.vboxGroupBox)
        v_box_layout.addWidget(self.gridGroupBox)
        main_layout.addLayout(v_box_layout)
        self.setLayout(main_layout)

    def createGridGroupBox(self):
        self.gridGroupBox = QGroupBox("按键")
        grid = QGridLayout()
        # self.setLayout(grid)
        # 内容
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions = [(i, j) for i in range(5) for j in range(4)]

        # 使用addWidget()方法加入到布局中
        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            button.clicked.connect(self.button_clicked)
            grid.addWidget(button, *position)

        self.gridGroupBox.setLayout(grid)

    def createVboxGroupBox(self):
        # 这里不管如何(布局)都不可能让 显示框的数字变化了。通过debug知道这里只会运行一次
        # 哪怕这里的self.text来源于函数，这个函数也只在本函数中完全运行一次后就不会再改变
        # 一种方法就是这里的label和按钮绑定，每次按钮都是调用这个label的值的函数
        self.vboxGroupBox = QGroupBox("显示框")
        # v_box = QVBoxLayout()
        # big_editor = QTextEdit()
        # big_editor.setText(self.text)
        # v_box.addWidget(big_editor)
        # self.vboxGroupBox.setLayout(v_box)
        grid = QGridLayout()
        grid.setSpacing(10)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        self.vboxGroupBox.setLayout(grid)

    def button_clicked(self):
        sender = self.sender()
        self.text = sender.text()
        print(self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    e.show()
    sys.exit(app.exec_())
