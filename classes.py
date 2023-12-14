from PIL import ImageFont
#create custom colour class for storing colourvalue and name
class Colour:
    def __init__(self):
        self.colourCode = None
        self.colourName = None

#create custom font info class for storing misc. font info like strokeFill, fontType, etc.
class FontInfo:
    def __init__(self, fontType, fontSize):
        self.fill = None
        self.strokeFill = None
        self.strokeWidth = None
        self.font = ImageFont.truetype(fontType, fontSize)