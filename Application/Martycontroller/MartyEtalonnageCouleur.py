import martypy
class MartyEtalonnageCouleur():
    def __init__(self, Marty):
        self.marty = Marty
        self.Colors = {"Rouge", "Jaune", "Vert", "Bleu", "Violet", "Noir"}

    def getDict(self):
        return self.Colors

    def AddColorDict(self, key):
        n = 5
        R,G,B = [0]*n,[0]*n,[0]*n
        sR, sG, sB = 0, 0, 0

        for i in range(n):
            value = self.marty.color()
            R[i],G[i],B[i] = value[0:2], value[2:4], value[4:6]
            sR += int(R[i], 16)
            sG += int(G[i], 16)
            sB += int(B[i], 16)

        sR = hex(int(sR/5))
        sG = hex(int(sG/5))
        sB = hex(int(sB/5))

        sR = sR[2:4]
        sG = sG[2:4]
        sB = sB[2:4]

        valueM = sR + sG + sB
        
        self.Colors[key] = valueM

    def SaveDict(self):
        Database = open("databaseHexaColor.txt","w")
        Database.write(self.Colors)