from PyQt6.QtWidgets import  QWidget, QLineEdit, QPushButton, QGridLayout, QMessageBox,QDialog, QLabel
from PyQt6.QtGui import QIcon , QPixmap
from PyQt6.QtCore import QSize
from PyQt6.QtCore import Qt 
from Martycontroller.MartyController import MartyController
from Martycontroller.MartyEtalonnageCouleur import MartyEtalonnageCouleur

class ColorWindow(QWidget):
    def __init__(self, Marty):
        super(ColorWindow, self).__init__()
        self.marty = Marty
        self.martycol = MartyEtalonnageCouleur(Marty)
        self.ActionsCouleurs()
        self.InitGrid()
        

    def ActionsCouleurs(self):
        self.btnRouge = QPushButton("")
        self.btnRouge.setIcon(QIcon("Application/img/icons8-emoji-carré-rouge-48.png"))
        self.btnRouge.setIconSize(QSize(50, 50))
        self.btnRouge.clicked.connect(lambda: self.pushColor("Rouge"))

        self.btnJaune = QPushButton("")
        self.btnJaune.setIcon(QIcon("Application/img/icons8-emoji-carré-jaune-48.png"))
        self.btnJaune.setIconSize(QSize(50, 50))
        self.btnJaune.clicked.connect(lambda: self.pushColor("Jaune"))

        self.btnVert = QPushButton("")
        self.btnVert.setIcon(QIcon("Application/img/icons8-emoji-carré-vert-48.png"))
        self.btnVert.setIconSize(QSize(50, 50))
        self.btnVert.clicked.connect(lambda: self.pushColor("Vert"))

        self.btnBleu = QPushButton("")
        self.btnBleu.setIcon(QIcon("Application/img/icons8-emoji-carré-bleu-48.png"))
        self.btnBleu.setIconSize(QSize(50, 50))
        self.btnBleu.clicked.connect(lambda: self.pushColor("Bleu"))

        self.btnViolet = QPushButton("")
        self.btnViolet.setIcon(QIcon("Application/img/icons8-emoji-carré-violet-48.png"))
        self.btnViolet.setIconSize(QSize(50, 50))
        self.btnViolet.clicked.connect(lambda: self.pushColor("Violet"))

        self.btnNoir = QPushButton("")
        self.btnNoir.setIcon(QIcon("Application/img/icons8-emoji-grand-carré-noir-48.png"))
        self.btnNoir.setIconSize(QSize(50, 50))
        self.btnNoir.clicked.connect(lambda: self.pushColor("Noir"))

        self.btnSauvegarde = QPushButton("")
        self.btnSauvegarde.setIcon(QIcon("Application/img/icons8-sauvegarde-50.png"))
        self.btnSauvegarde.setIconSize(QSize(50, 50))
        self.btnSauvegarde.clicked.connect(self.sauvegardeDict)

        self.btnTest = QPushButton("test")
        self.btnTest.clicked.connect(self.test)

    def InitGrid(self):
        layout = QGridLayout() 

        layout.addWidget(self.btnRouge, 0, 0)
        layout.addWidget(self.btnJaune, 0, 1)
        layout.addWidget(self.btnVert, 0, 2)
        layout.addWidget(self.btnBleu, 0, 3)
        layout.addWidget(self.btnViolet, 0, 4)
        layout.addWidget(self.btnNoir,0,5)
        layout.addWidget(self.btnSauvegarde, 1, 2)
        layout.addWidget(self.btnTest, 1, 3)

        self.setLayout(layout)

    def pushColor(self, key):
        self.martycol.AddColorDict(key)

    def sauvegardeDict(self):
        self.martycol.SaveDict()
    
    def test(self):
        self.martycol.test()