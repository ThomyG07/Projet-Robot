import martypy
import json

class InterpretationCouleur() :

    def __init__(self, marty_controller ):
        self.marty = marty_controller
        self.config_path = "databaseHexaColor.json"
        self.color_actions = self.load_color_config() # Chargement des configurations des actions

    
    def Hexa2RGB(self, hexa):
        R, G, B = hexa[0:2], hexa[2:4], hexa[4:6]
        return [int(R, 16), int(G, 16), int(B, 16)]
    

    #lire le fichier de config
    def load_color(self):
        with open(self.config_path, 'r') as file:
            return json.load(file)



    def interpret_and_act(self):
        # Scanner couleur
        hex_color = self.marty.get_color_sensor_hex()

        # Convertir en RGB
        rgb_color = self.Hexa2RGB(hex_color)
        
        # Trouver l'action correspondante
        action_name = self.find_action(rgb_color)

        # Executer l'action
        if action_name :
            self.execute_action(action_name)



    def find_action(self, color_rgb):
        
        for color_name , color_data in self.color_actions.items():
            if self.is_color_match(color_rgb, color_data['rgb']):
                return color_data['action']
        return None
    
    def execute_action(self, action_name):
        action_method = getattr(self, action_name)
        if action_method:
            action_method()
    


    def is_color_match(self, detected_rgb, target_rgb):
        #Determine si la couleur detectée correspond à la couleur cible
        tolerance = 10
        for i in range (3):
            difference = abs(detected_rgb[i] - target_rgb[i])
            if difference > tolerance:
                return False
        return True

    def stop_and_dance(self):
        self.marty.get_ready()
        self.marty.dance()

    def move_forward(self):
        self.marty.move_forward(6)

    def move_backward(self):
        self.marty.move_backward(6)

    def slide_left(self):
        self.marty.move_side('left', 3)

    def slide_right(self):
        self.marty.move_side('right', 3)

    def no_action(self):
        print("Aucune action pour cette couleur")
