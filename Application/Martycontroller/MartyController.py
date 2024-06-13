import martypy
class MartyController():
    def __init__(self, ip ):
        self.ip = ip
        self.marty = None

    def connect_to_marty(self):
        try:
            print(f"connection")
            print(self.ip)
            marty = martypy.Marty("wifi", self.ip)
            self.marty = marty
            return marty
        except Exception as e:
            print(f"Failed to connect to Marty: {e}")
            self.marty = None
            return None

    def move_forward(self,steps = 2):
        if self.marty:
            self.marty.walk(steps, step_length=25)

    def move_forward_Blocking(self,steps = 2):
        if self.marty:
            self.marty.walk(steps, step_length=25, blocking=True)

    def move_backward(self,steps = 2):
        if self.marty:
            self.marty.walk(steps,step_length=-25)

    def move_backward_Blocking(self,steps = 2):
        if self.marty:
            self.marty.walk(steps,step_length=-25, blocking=True)

    def move_side(self,side, steps = 2 ):
        if self.marty:
            self.marty.sidestep(side,steps)

    def move_side_Blocking(self,side, steps = 2):
        if self.marty:
            self.marty.sidestep(side,steps, blocking=True)


    def batttery(self):
        if self.marty:
            return self.marty.get_battery_remaining()
        return None
    
    def color(self):
        
        if self.marty:
            try:
                return self.marty.get_color_sensor_hex("left")
            except Exception as e:
                print(f"Probleme avec le capteur de couleur {e}")
        return None

    def turn_left(self,degrees):
        if self.marty:
            self.marty.walk(turn=degrees, move_time=3000)
            self.marty.stand_straight()

    def dance(self):
        if self.marty:
            self.marty.dance()


    def get_ready(self):
        if self.marty:
            self.marty.get_ready()

    
    def show_off(self):
        if self.marty:
            self.marty.celebrate()

    def wave_left(self):
        if self.marty:
            self.marty.arms( left_angle = 1000, right_angle = 0, move_time= 1000)
        

    def wave_right(self):
        if self.marty:
            self.marty.arms(left_angle = 0, right_angle = 1000, move_time = 1000)


    def wiggle_eyes(self):
        if self.marty:
            self.marty.eyes(pose_or_angle= 'wiggle')

    def kick_left(self) :
        if self.marty:
            self.marty.kick(side='left')

    def kick_right(self):
        if self.marty:
            self.marty.kick(side='right')
            
    def etat_connection(self):
        print(self.marty)
        return self.marty.is_conn_ready()
    
    def getMarty(self):
        return self.marty

    def close(self):
        self.marty.close()
        

            
