import numpy as np
import colournames

class Colour:
    def __init__(self):
        self.colourCode = None
        self.colourName = None

    def generateRandomColour(self):
        colour = tuple(np.random.choice(range(256), size=3))
        return colour
    
    def getColourName(self, colourCode):
        colourName = colournames.find(int(colourCode[0]), int(colourCode[1]), int(colourCode[2]))
        return colourName