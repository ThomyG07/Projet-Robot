from PyQt6.QtWidgets import  QWidget, QLineEdit, QPushButton, QGridLayout, QMessageBox,QDialog, QLabel
from PyQt6.QtGui import QIcon , QPixmap
from PyQt6.QtCore import QSize
from PyQt6.QtCore import Qt 
import re
from Martycontroller.MartyController import MartyController
import threading
class ActionPanel(QWidget):
    def __init__(self):
        super(ActionPanel, self).__init__()
        self.marty = None
        self.ActionsAffichage()
        self.InitGrid()

    def ActionsAffichage(self):
        self.btnDance = QPushButton("")
        self.btnDance.setIcon(QIcon("Application/img/icons8-danse-50.png"))
        self.btnDance.setIconSize(QSize(50, 50))
        self.btnDance.setShortcut('r')
        self.btnDance.clicked.connect(self.dance)



    def InitGrid(self):
        layout = QGridLayout()

        layout.addWidget(self.btnDance, 0, 0)

        self.setLayout(layout)

    def dance(self):
        if self.CheckMartyC():
            mon_thread = threading.Thread(target = self.marty.dance)
            mon_thread.start()

    def CheckMartyC(self):
        if self.marty is not None:
           return True
        else:
            message_erreurco = QMessageBox.critical(
            self,
            "Erreur",
            "Pas de Morty connecté",)
            return False
        
    def SetMartyC(self,martyC):
        self.marty = martyC
