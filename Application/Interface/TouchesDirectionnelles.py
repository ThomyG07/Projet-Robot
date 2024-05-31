
from PyQt6.QtWidgets import  QWidget, QPushButton, QGridLayout, QMessageBox
from PyQt6.QtGui import QIcon 
from PyQt6.QtCore import QSize
from Martycontroller.MartyController import MartyController




class TouchesDirectionnelles(QWidget):
    def __init__(self):
        super(TouchesDirectionnelles, self).__init__()
        self.marty = None
        self.AjoutTouche()
        self.InitGrid()
        
    
    def AjoutTouche(self):

        self.btnRG = QPushButton("")
        self.btnRG.setIcon(QIcon("Application/img/icons8-gauche-2-30.png"))
        self.btnRG.setIconSize(QSize(50, 50))
        self.btnRG.clicked.connect(self.RtG)

        self.btnRD = QPushButton("")
        self.btnRD.setIcon(QIcon("Application/img/icons8-droit-2-30.png"))
        self.btnRD.setIconSize(QSize(50, 50))
        self.btnRD.clicked.connect(self.RtD)

        self.btnH = QPushButton("")
        self.btnH.setIcon(QIcon("Application/img/icons8-flèche-haut-50.png"))
        self.btnH.setIconSize(QSize(50, 50))
        self.btnH.clicked.connect(self.Haut)

        self.btnD = QPushButton("")
        self.btnD.setIcon(QIcon("Application/img/icons8-flèche-haut-50_90.png"))
        self.btnD.setIconSize(QSize(50, 50))
        self.btnD.clicked.connect(self.MvtHD)
        
        self.btnG = QPushButton("")
        self.btnG.setIcon(QIcon("Application/img/icons8-flèche-haut-50_-90.png"))
        self.btnG.setIconSize(QSize(50, 50))
        self.btnG.clicked.connect(self.MvtHG)

        self.btnB = QPushButton("")
        self.btnB.setIcon(QIcon("Application/img/icons8-flèche-haut-50_180.png"))
        self.btnB.setIconSize(QSize(50, 50))
        self.btnB.clicked.connect(self.Bas)

    def InitGrid(self):

        layout = QGridLayout()

        layout.addWidget(self.btnRG, 0, 0)
        layout.addWidget(self.btnH, 0, 1)
        layout.addWidget(self.btnRD, 0, 2)
        layout.addWidget(self.btnG, 1, 0)
        layout.addWidget(self.btnD, 1, 2)
        layout.addWidget(self.btnB, 2, 1)

        self.setLayout(layout)
    
    def Haut(self):
        if self.CheckMartyC():
            self.btnG.animateClick()
            self.marty.move_forward(steps=5)
    def Bas(self):
        if self.CheckMartyC():
            self.btnG.animateClick()
            self.marty.move_backward(steps=5)
    def MvtHD(self):
        if self.CheckMartyC():
            self.marty.move_side("left", steps=5)
    def MvtHG(self):
        if self.CheckMartyC():
            self.marty.move_side("right", steps=5)
    def RtD(self):
        if self.CheckMartyC():
            self.marty.turn_left(20)
    def RtG(self):
        if self.CheckMartyC():
            self.marty.turn_left(-20)

    def Bas(self):
        if self.CheckMartyC():
            self.btnG.animateClick()
            self.marty.move_forward(steps=5)

    def SetMartyC(self,martyC):
        self.marty = martyC

    def CheckMartyC(self):
        if self.marty is not None:
           return True
        else:
            message_erreurco = QMessageBox.critical(
            self,
            "Erreur",
            "Pas de Morty connecté",)
            return False
    
    
        
