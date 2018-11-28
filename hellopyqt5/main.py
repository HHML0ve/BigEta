import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from hellopyqt5 import hello_world

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = hello_world.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
