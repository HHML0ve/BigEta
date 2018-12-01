# -*- coding:utf-8 -*-
import sys

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow


class Communicate(QObject):
    closeApp = pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.c = Communicate()
        self.init_ui()

    def init_ui(self):
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, *args, **kwargs):
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()

    sys.exit(app.exec_())
