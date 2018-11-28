# -*- coding:utf-8 -*-
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import (QWidget, QApplication,
                             QDesktopWidget, QMessageBox, QToolTip, QPushButton)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('鼠标停留我是被给出的提示信息')

        btn = QPushButton('点击我', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setToolTip('鼠标停留在按钮上面我是被给出的提示信息')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.resize(300, 300)
        self.center()
        self.setWindowTitle('Summarize')
        self.setWindowIcon(QIcon('resource/pen1.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '', '',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())
