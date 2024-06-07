from PyQt6.QtWidgets import  QWidget, QLineEdit, QPushButton, QGridLayout, QMessageBox,QDialog, QLabel
from PyQt6.QtGui import QIcon , QPixmap
from PyQt6.QtCore import QSize
from PyQt6.QtCore import Qt 
import re
from Martycontroller.MartyController import MartyController
import threading

class ColorWindow(QWidget):
    def __init__(self):
        super(ColorWindow, self).__init__()
        self.Colors = {}
    