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

        self.btnGetReady = QPushButton("")
        self.btnGetReady.setIcon(QIcon("Application/img/icons8-bras-en-l'air-50.png"))
        self.btnGetReady.setIconSize(QSize(50,50))
        self.btnGetReady.setShortcut('t')
        self.btnGetReady.clicked.connect(self.getReady)

        self.btnCelebrate = QPushButton("")
        self.btnCelebrate.setIcon(QIcon("Application/img/icons8-confettis-50.png"))
        self.btnCelebrate.setIconSize(QSize(50,50))
        self.btnCelebrate.setShortcut('y')
        self.btnCelebrate.clicked.connect(self.celebrate)

        self.btnWaveLeft = QPushButton("")
        self.btnWaveLeft.setIcon(QIcon("Application/img/icons8-main-vers-la-gauche-50.png"))
        self.btnWaveLeft.setIconSize(QSize(50,50))
        self.btnWaveLeft.setShortcut('u')
        self.btnWaveLeft.clicked.connect(self.waveLeft)

        self.btnWaveRight = QPushButton("")
        self.btnWaveRight.setIcon(QIcon("Application/img/icons8-main-vers-la-droite-50.png"))
        self.btnWaveRight.setIconSize(QSize(50,50))
        self.btnWaveRight.setShortcut('i')
        self.btnWaveRight.clicked.connect(self.waveRight)

        self.btnWiggleEyes = QPushButton("")
        self.btnWiggleEyes.setIcon(QIcon("Application/img/icons8-yeux-heureux-50.png"))
        self.btnWiggleEyes.setIconSize(QSize(50,50))
        self.btnWiggleEyes.setShortcut('o')
        self.btnWiggleEyes.clicked.connect(self.wiggleEyes)

        self.btnKickLeft = QPushButton("")
        self.btnKickLeft.setIcon(QIcon("Application/img/icons8-messi-48.png"))
        self.btnKickLeft.setIconSize(QSize(50,50))
        self.btnKickLeft.setShortcut('g')
        self.btnKickLeft.clicked.connect(self.kickLeft)

        self.btnKickRight = QPushButton("")
        self.btnKickRight.setIcon(QIcon("Application/img/icons8-ronaldo-48.png"))
        self.btnKickRight.setIconSize(QSize(50,50))
        self.btnKickRight.setShortcut('h')
        self.btnKickRight.clicked.connect(self.kickRight)

        

    def InitGrid(self):
        layout = QGridLayout()

        layout.addWidget(self.btnDance, 0, 0)
        layout.addWidget(self.btnGetReady, 0, 1)
        layout.addWidget(self.btnCelebrate, 0, 2)
        layout.addWidget(self.btnWiggleEyes, 0, 3)
        layout.addWidget(self.btnWaveLeft, 1, 0)
        layout.addWidget(self.btnWaveRight, 1, 1)
        layout.addWidget(self.btnKickLeft, 1, 2)
        layout.addWidget(self.btnKickRight, 1, 3)

        self.setLayout(layout)

    def dance(self):
        if self.CheckMartyC():
            mon_thread = threading.Thread(target = self.marty.dance)
            mon_thread.start()

    def getReady(self):
        if self.CheckMartyC():
            mon_thread = threading.Thread(target= self.marty.get_ready)
            mon_thread.start()

    def celebrate(self):
        if self.CheckMartyC():
            mon_thread = threading.Thread(target=self.marty.celebrate)
            mon_thread.start()

    def waveLeft(self):
        if self.CheckMartyC():
            mon_thread = threading.Thread(target=self.marty.wave, args=("left",))
            mon_thread.start()

    def waveRight(self):
        if self.CheckMartyC():
            mon_thread = threading.Thread(target=self.marty.wave, args=("right",))
            mon_thread.start()

    def wiggleEyes(self):
        if self.CheckMartyC():
            mon_thread = threading.Thread(target=self.marty.wiggle)
            mon_thread.start()

    def kickLeft(self):
        if self.CheckMartyC():
            mon_thread = threading.Thread(target=self.marty.kick, args=("left",))
            mon_thread.start()
    
    def kickRight(self):
        if self.CheckMartyC():
            mon_thread = threading.Thread(target=self.marty.kick, args=("right",))
            mon_thread.start()

    def CheckMartyC(self):
        if self.marty is not None:
           return True
        else:
            message_erreurco = QMessageBox.critical(
            self,
            "Erreur",
            "Pas de Marty connecté",)
            return False
        
    def SetMartyC(self,martyC):
        self.marty = martyC
