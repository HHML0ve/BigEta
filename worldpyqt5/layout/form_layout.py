# -*- coding:utf-8 -*-
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QLineEdit, QTextEdit


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        title_edit = QLineEdit()
        author_edit = QLineEdit()
        review_edit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(title_edit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(author_edit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(review_edit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)

        self.setWindowTitle('form edit')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()

    sys.exit(app.exec_())
