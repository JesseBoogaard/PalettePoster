import numpy as np
from colournames import find

class Colour:
    def __init__(self):
        self.colourCode = self.generateRandomColour()
        self.colourName = self.getColourName(self.colourCode)

    def generateRandomColour(self):
        colour = tuple(np.random.choice(range(256), size=3))
        return colour
    
    def getColourName(self, colourCode):
        colourName = find(colourCode)
        return colourName