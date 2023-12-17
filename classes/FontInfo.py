from PIL import ImageFont

class FontInfo:
    def __init__(self, fontType, fontSize):
        self.fill = None
        self.strokeFill = None
        self.strokeWidth = None
        self.font = ImageFont.truetype(fontType, fontSize)