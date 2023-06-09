import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.showNormal()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
