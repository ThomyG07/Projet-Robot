import martypy
class MartyController():
    def __init__(self, ip ):
        self.ip = ip
        self.marty = None
        #self.marty = self.connect_to_marty(ip)

    def connect_to_marty(self):
        try:
            print(f"connection")
            marty = martypy.Marty("wifi", self.ip)
            return marty
        except Exception as e:
            print(f"Failed to connect to Marty: {e}")
            return None

    def move_forward(self,steps=1):
        if self.marty:
            self.marty.walk(steps, step_length=25)
            self.marty.stand_straight()
    def move_backward(self,steps=1):
        if self.marty:
            self.marty.walk(steps,"auto", 0,-25)
    def move_side(self,side, steps = 1 ):
        if self.marty:
            self.marty.sidestep(side,steps)
            

    def turn_left(self,degrees):
        if self.marty:
            self.marty.walk(turn=degrees, move_time=3000)
            self.marty.stand_straight()

    def dance(self):
        if self.marty:
            self.marty.dance()
            
    def etat_connection(self):
        print(self.marty)
        return self.marty.is_conn_ready()
    
    def getMarty(self):
        return self.marty
            
    def marty_function(self):
        print("hemm")

    def close(self):
        self.marty.close()
        

            
