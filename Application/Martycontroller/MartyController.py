import martypy
class MartyController():
    def __init__(self, ip ):
        self.marty = self.connect_to_marty(ip)
        self.main()

    def connect_to_marty(self,ip):
        try:
            print(f"connection")
            marty = martypy.Marty("wifi", ip)
            return marty
        except Exception as e:
            print(f"Failed to connect to Marty: {e}")
            return None

    def move_forward(self,steps=1):
        if self.marty:
            self.marty.walk(steps)

    def turn_left(self,degrees):
        if self.marty:
            self.marty.walk(turn=degrees)
            print("test")

    def dance(self):
        if self.marty:
            self.marty.dance()
            
    def main(self):
        
        if self.marty :
            print("Connected to Marty successfully!")
            self.move_forward(steps=5)
            self.turn_left(degrees=20)
            self.dance()
        else:
            print("Failed to control Marty. C")
    def close(self):
        self.marty.close()
        

            
