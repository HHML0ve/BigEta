# -*- coding:utf-8 -*-
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 移动控件，设置控件标题，在桌面显示控件
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    # 这个命名是必须的 -- 重构
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
