import martypy
from time import sleep

class MatriceNavigation():
    def __init__(self, ip):
        self.ip = ip
        self.grid_size = 3
        self.color_grid = {}


    
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
                  self.marty.move_forward(6)
                  sleep(1)
                  self.marty.get_ready()
                  sleep(1)
                else :
                    self.marty.move_backward(6)
                    sleep(1)
                    self.marty.get_ready()
                    sleep(1)
        
    def record_color(self, col, row):

        color = self.marty.color();
        print(f"Color at position ({col}, {row}): {"hej"}")
        sleep(1)
        print("test")


    

