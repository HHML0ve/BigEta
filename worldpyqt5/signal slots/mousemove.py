# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QGridLayout,
                             QLabel, QLCDNumber, QSlider, QVBoxLayout, QHBoxLayout)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.text = ""
        self.label = None
        self.init()

    def init(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        x = 0
        y = 0

        self.text = "x:{0}, y:{1}".format(x, y)
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        # 只有这句话才会让布局生效
        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('summary')
        self.show()

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()

        text = 'x:{0}, y:{1}'.format(x, y)
        self.label.setText(text)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())
