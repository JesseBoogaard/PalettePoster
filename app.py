#imports
from classes.Colour import Colour
from classes.FontInfo import FontInfo
import uuid
import time
from PIL import Image, ImageDraw

def loadTemplateImage(imageTemplate):
    img = Image.open(imageTemplate)
    img = img.convert("RGB")
    return img

def generateNewFileName():
    return str(uuid.uuid4())+".png"

def createNewImageFromTemplate(templateImage, randomColours, newFileName, ranges):
    imageArray = templateImage.getdata()
    newImage = []
    for item in imageArray:
        if item[0] in ranges[0]:
            newImage.append(randomColours[0].colourCode)
        elif item[0] in ranges[1]:
            newImage.append(randomColours[1].colourCode)
        elif item[0] in ranges[2]:
            newImage.append(randomColours[2].colourCode)
        else:
            newImage.append(item)
    templateImage.putdata(newImage)
    templateImage.save(newFileName)

def addColourNamesToImage(randomColours, fontInfo, newFileName):
    image = Image.open(newFileName)
    tmp = ImageDraw.Draw(image)
    tmp.text((150,915), '"' + randomColours[0].colourName + '"', fill=fontInfo.fill, stroke_fill=fontInfo.strokeFill, stroke_width=fontInfo.strokeWidth, font=fontInfo.font)
    tmp.text((150,500), '"' + randomColours[1].colourName + '"', fill=fontInfo.fill, stroke_fill=fontInfo.strokeFill, stroke_width=fontInfo.strokeWidth, font=fontInfo.font)
    tmp.text((570,915), '"' + randomColours[2].colourName + '"', fill=fontInfo.fill, stroke_fill=fontInfo.strokeFill, stroke_width=fontInfo.strokeWidth, font=fontInfo.font)
    image.save(newFileName)

#######-------------------------------------MAIN PROGRAM HERE----------------------------------------######

def __main__():
    randomColours = []
    numberOfColours = 3
    imageTemplate = "templates/3way_template.jpg"
    saveFolder = "generated/"
    newFileName = saveFolder + generateNewFileName()

    fontInfo = FontInfo('fonts/Verdanai.ttf', 24)
    fontInfo.fill = (250,250,250)
    fontInfo.strokeFill = (50,50,50)
    fontInfo.strokeWidth = 1

    ranges = [range(20,30), range(30,100), range(100,200)]
    
    img = loadTemplateImage(imageTemplate)

    for n in range(numberOfColours):
         colour = Colour()
         colour.colourCode = colour.generateRandomColour()
         colour.colourName = colour.getColourName(colour.colourCode)
         randomColours.append(colour)

    createNewImageFromTemplate(img, randomColours, newFileName, ranges)
    addColourNamesToImage(randomColours, fontInfo, newFileName)

startTime = time.time()
__main__()
print("--- %s seconds ---" % (time.time() - startTime))