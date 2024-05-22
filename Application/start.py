import sys
from PyQt6.QtCore import PYQT_VERSION_STR
from PyQt6.QtWidgets import QApplication
import cv2
import qreader
from Interface.MainWindow import MainWindow
from Martycontroller.MartyController import MartyController



marty = MartyController("192.168.0.5")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()