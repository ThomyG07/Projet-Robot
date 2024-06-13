import json
import martypy
from time import sleep

class MartyEtalonnageCouleur():
    def __init__(self, Marty):
        self.marty = Marty
        self.Colors = {"Rouge": {"rgb": None ,"action": "stop_and_dance"}, 
                       "Jaune": {"rgb": None ,"action": "move_backward"}, 
                       "Vert": { "rgb" :None, "action" : "move_forward" } , 
                       "Bleu Ciel": { "rgb" :None, "action" : "move_forward" },
                       "Bleu Marine":{ "rgb" :None, "action" : "side_right" }, 
                       "Rose": { "rgb" :None, "action" : "side_left" }, 
                       "Noir":{ "rgb" :None, "action" : "no_action" }
                       }

    def getDict(self):
        return self.Colors

    def AddColorDict(self, key):
        n = 5
        R,G,B = [0]*n,[0]*n,[0]*n
        sR, sG, sB = 0, 0, 0

        for i in range(n):
            value = self.marty.color()
            sleep(0.2)
            R[i],G[i],B[i] = value[0:2], value[2:4], value[4:6]
            sR += int(R[i], 16)
            sG += int(G[i], 16)
            sB += int(B[i], 16)

        sR = int(sR/n)
        sG = int(sG/n)
        sB = int(sB/n)
        
        self.Colors[key]["rgb"] = [sR, sG, sB]

    def SaveDict(self):
        # Enregistrement du dictionnaire dans un fichier JSON
        file = "databaseHexaColor"+self.marty.getIp()+".json"
        with open(file, "w") as test:
            json.dump(self.Colors, test)
    
    def LoadDataBase(self):
        file = "databaseHexaColor"+self.marty.getIp()+".json"
        with open(file,"r") as test:
            self.Colors = json.load(test)

    def test(self):
        valueHexa = self.marty.color()
        codeRGB = self.Hexa2RGB(valueHexa)
        for cle,hexvalue in self.Colors.items():
            ecart =0
            if(hexvalue["rgb"]!= None):
                for i in range(len(hexvalue["rgb"])):
                    ecart+=abs(codeRGB[i]-hexvalue["rgb"][i])
                if(ecart/3 <10): print(cle)

    def Hexa2RGB(self, hexa):
        R,G,B = hexa[0:2], hexa[2:4], hexa[4:6]
        sR = int(R, 16)
        sG = int(G, 16)
        sB = int(B, 16)
        codeRGB = [sR, sG, sB]
        return codeRGB




