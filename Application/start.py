import sys
from PyQt6.QtCore import PYQT_VERSION_STR
from PyQt6.QtWidgets import QApplication
import cv2
from Interface.MainWindow import MainWindow
from Martycontroller.MartyController import MartyController




app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()