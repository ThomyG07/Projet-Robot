import martypy


class MatriceNavigation():
    def __init__(self,  marty_controller):
        self.marty = marty_controller
        self.grid_size = 3
        self.color_grid = {}


    
    def navigate_and_record(self):

        for col in range(self.grid_size):     # commencer du bas de la grille
            if col % 2 == 0 :  #colone 0 et 2
                self.scan_column(col, "up")
                self.marty.get_ready()

            else :    #colonne 1
                self.scan_column(col, "down")
                self.marty.get_ready()
            
            if col < self.grid_size - 1:
                self.marty.move_side('right', 3)
           

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
                  self.marty.move_forward(3)
                else :
                    self.marty.move_backward(3)


        
    def record_color(self, col, row):
        color = self.marty.get_color_sensor_hex()  
        print(f"Couleur à la  position ({col}, {row}): {color}")


    

