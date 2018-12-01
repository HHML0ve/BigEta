# -*- coding:utf-8 -*-
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建栅格化布局实例，并放入窗口中
        grid = QGridLayout()
        self.setLayout(grid)

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
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('grid lay out')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()

    sys.exit(app.exec_())
