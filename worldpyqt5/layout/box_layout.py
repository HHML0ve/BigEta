# -*- coding:utf-8 -*-
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建俩个按钮
        ok_button = QPushButton("ok")
        cancel_button = QPushButton("Cancel")

        # 创建水平布局
        qh_box = QHBoxLayout()
        qh_box.addStretch(1)
        qh_box.addWidget(ok_button)
        qh_box.addWidget(cancel_button)

        # 创建垂直布局，把上述创建的水平布局放入新垂直布局中
        vh_box = QVBoxLayout()
        vh_box.addStretch(1)
        vh_box.addLayout(qh_box)

        self.setLayout(vh_box)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('box lay out')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()

    sys.exit(app.exec_())
