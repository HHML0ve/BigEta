# -*- coding:utf-8 -*-
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLCDNumber, QSlider, QVBoxLayout


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 数字， 滑块
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        v_box = QVBoxLayout()
        v_box.addWidget(lcd)
        v_box.addWidget(sld)

        self.setLayout(v_box)
        # 把滑块的变化和数字的变化绑定到一起
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('grid lay out')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()

    sys.exit(app.exec_())
