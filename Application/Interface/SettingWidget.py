from PyQt6.QtWidgets import  QWidget, QLineEdit, QPushButton, QGridLayout, QMessageBox,QDialog, QLabel
from PyQt6.QtGui import QIcon , QPixmap
from PyQt6.QtCore import QSize
from PyQt6.QtCore import Qt 
import re
from Martycontroller.MartyController import MartyController
from qasync import asyncSlot
import threading




class SettingWidget(QWidget):
    def __init__(self,TouchesDirectionnelles):
        super(SettingWidget, self).__init__()
        self.TouchesDire = TouchesDirectionnelles
        self.AddElement()
        self.InitGrid()
        self.marty = None
        
    
    def AddElement(self):
    
        self.text_ip = QLineEdit(self)
        self.text_ip.setGeometry(50, 50, 200, 30)
        self.btnC = QPushButton("")
        self.btnC.setIcon(QIcon("Application/img/icons8-wifi-50.png"))
        self.btnC.setIconSize(QSize(25, 25))
        self.btnC.clicked.connect(self.connect)
        self.label = QLabel("")
        self.label.setPixmap(QPixmap("Application/img/icons8-emoji-cercle-rouge-48.png"))
        self.label.setGeometry(25,25,25,25)


    def InitGrid(self):
        layout = QGridLayout()

        layout.addWidget(self.text_ip, 0, 0)
        layout.addWidget(self.btnC, 0, 1)
        layout.addWidget(self.label, 0, 2)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)

    def connect(self):
        motif = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
        resultat = motif.search(self.text_ip.text())
        if resultat:
            
            self.marty = MartyController(self.text_ip.text())
            #mon_thread = threading.Thread(target=self.test)
            #mon_thread.start()
            self.marty.connect_to_marty()
            if self.marty.getMarty() is not None:   
                self.TouchesDire.SetMartyC(self.marty)
                self.updateLabel()
            else:
                message_erreurco = QMessageBox.critical(
                self,
                "Erreur",
                "Erreur de connexion",)
           
            
        else:
            button = QMessageBox.critical(
            self,
            "Erreur",
            "Champ saisit n'est pas une addresse ip",
            
        )
    
    def getMartyController(self):
        return self.marty
    def setMartyController(self, MartyC):
        self.marty = MartyC
       
    def updateLabel(self):
        if self.marty.etat_connection():
            self.label.setPixmap(QPixmap("Application/img/icons8-emoji-cercle-vert-48.png"))
        else:
            self.label.setPixmap(QPixmap("Application/img/icons8-emoji-cercle-rouge-48.png"))