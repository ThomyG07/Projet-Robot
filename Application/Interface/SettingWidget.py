from PyQt6.QtWidgets import  QWidget, QLineEdit, QPushButton, QGridLayout, QMessageBox,QDialog, QLabel
from PyQt6.QtGui import QIcon , QPixmap
from PyQt6.QtCore import QSize
from PyQt6.QtCore import Qt 
import re
from Martycontroller.MartyController import MartyController
from Interface.ColorWindow import ColorWindow
from MatriceNavigation.MatriceNavigation import MatriceNavigation
import threading

class SettingWidget(QWidget):
    def __init__(self,TouchesDirectionnelles, ActionPanel):
        super(SettingWidget, self).__init__()
        self.TouchesDire = TouchesDirectionnelles
        self.ActionPanel = ActionPanel
        self.Colors = {}
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
        self.battery = QLabel("Niveau de batterie :")
        self.battery_value = QLabel("--%")
        self.btnColorsensor = QPushButton("Couleur")
        self.btnColorsensor.clicked.connect(self.DefColor)
        self.btnNavigation = QPushButton("Navigation")
        self.btnNavigation.clicked.connect(self.record)


    def InitGrid(self):
        layout = QGridLayout()

        layout.addWidget(self.text_ip, 0, 0)
        layout.addWidget(self.btnC, 0, 1)
        layout.addWidget(self.label, 0, 2)
        layout.addWidget(self.battery, 1,0)
        layout.addWidget(self.battery_value, 1,1)
        layout.addWidget(self.btnColorsensor, 2, 0)
        layout.addWidget(self.btnNavigation,3,0)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)

    def connect(self):
        motif = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
        resultat = motif.search(self.text_ip.text())
        if resultat:
            
            self.marty = MartyController(self.text_ip.text())
            self.marty.connect_to_marty()
            if self.marty.getMarty() is not None:   
                self.TouchesDire.SetMartyC(self.marty)
                self.ActionPanel.SetMartyC(self.marty)
                self.Change_value(self.marty.batttery())
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

    def Change_value(self, newText):
        self.battery_value.setText(str(newText)+" %")

    def DefColor(self):
        if self.CheckMartyC():
            colorW = ColorWindow(self.marty)
            colorW.show()

    def CheckMartyC(self):
        if self.marty is not None:
           return True
        else:
            message_erreurco = QMessageBox.critical(
            self,
            "Erreur",
            "Pas de Morty connecté",)
            return False
       
    def updateLabel(self):
        if self.marty.etat_connection():
            self.label.setPixmap(QPixmap("Application/img/icons8-emoji-cercle-vert-48.png"))
        else:
            self.label.setPixmap(QPixmap("Application/img/icons8-emoji-cercle-rouge-48.png"))
    def record(self):
        matriceNav = MatriceNavigation(self.marty)
        mon_thread = threading.Thread(target = matriceNav.navigate_and_record)
        mon_thread.start()