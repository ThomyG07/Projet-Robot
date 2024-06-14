import json
from time import sleep
from Martycontroller.MartyEtalonnageCouleur import MartyEtalonnageCouleur
import numpy as np

class MatriceNavigation():
    def __init__(self, marty):
        self.marty = marty
        self.martycolor = MartyEtalonnageCouleur(self.marty)
        self.martycolor.LoadDataBase()
        self.grid_size = 3
        self.color_grid = {}
        self.loadMatrice()
        print(self.matrice)
        if (len(self.matrice) == 0): self.matrice =[[0,0,0],[0,0,0],[0,0,0]]
        

    def navigate_and_record(self):

        for col in range(self.grid_size):     # commencer du bas de la grille
            if col % 2 == 0 :  #colone 0 et 2
                self.scan_column(col, "up")
                

            else :    #colonne 1
                self.scan_column(col, "down")
            
            if col < self.grid_size - 1:
                self.marty.move_side('right', 5)
                sleep(1)
           

    def scan_column(self,col,direction):

        if direction == "up":
            start_row = 0
            end_row = self.grid_size - 1
            step = 1
        
        else :
            start_row = self.grid_size - 1
            end_row = 0
            step = -1

        for row in range(start_row , end_row + step , step ):

            #enregistrement de couleur
            self.record_color(col,row)
            
            #prochain mvt 
            if row != end_row:
                if direction == "up":
                  self.marty.move_forward_Blocking(6)
                  self.marty.get_ready()
                else :
                    self.marty.move_backward_Blocking(6)
                    self.marty.get_ready()
        
    def record_color(self, col, row):
        
        color = self.martycolor.test()
        print(f"Color at position ({col}, {row}): {color}")
        self.matrice[col][row] = color
        self.SaveMatrice()
        sleep(1)
    
    def SaveMatrice(self):   
        file = "Matrice.json"
        with open(file, "w") as test:
            json.dump(self.matrice, test)

    def loadMatrice(self):
        file = "Matrice.txt"
        self.matrice = np.loadtxt(file)


           


    

