from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 500, 300)
    win.setWindowTitle("Turbo Window")

    label = QtWidgets.QLabel(win)
    label.setText("not just a Window")
    label.move(200, 200)

    win.show()
    sys.exit(app.exec_())

window()