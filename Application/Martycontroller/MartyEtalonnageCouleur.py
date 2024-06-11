import martypy
from time import sleep

class MartyEtalonnageCouleur():
    def __init__(self, Marty):
        self.marty = Marty
        self.Colors = {"Rouge": None, "Jaune": None, "Vert": None, "Bleu": None, "Violet": None, "Noir":None}

    def getDict(self):
        return self.Colors

    def AddColorDict(self, key):
        n = 5
        R,G,B = [0]*n,[0]*n,[0]*n
        sR, sG, sB = 0, 0, 0

        for i in range(n):
            value = self.marty.color()
            sleep(0.2)
            print(value)
            R[i],G[i],B[i] = value[0:2], value[2:4], value[4:6]
            sR += int(R[i], 16)
            sG += int(G[i], 16)
            sB += int(B[i], 16)

        sR = int(sR/n)
        sG = int(sG/n)
        sB = int(sB/n)
        
        self.Colors[key] = [sR, sG, sB]

    def SaveDict(self):
        Database = open("databaseHexaColor.txt","w")
        Database.write(str(self.Colors))
        Database.close()

    def test(self):
        value = self.marty.color()
        R,G,B = value[0:2], value[2:4], value[4:6]
        sR = int(R, 16)
        sG = int(G, 16)
        sB = int(B, 16)
        codeRGB = [sR, sG, sB]
        for cle,hexvalue in self.Colors.items():
            ecart =0
            if(hexvalue!= None):
                for i in range(len(hexvalue)):
                    ecart+=abs(codeRGB[i]-hexvalue[i])
                    print(cle + str(i) + " : " + str(ecart))
                if(ecart/3 <10): print(cle)

        




