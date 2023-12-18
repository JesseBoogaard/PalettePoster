import os
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
    colourCodes = [randomColours[i].colourCode for i in range(len(randomColours))]
    newImage = [colourCodes[0] if item[0] in ranges[0] else colourCodes[1] if item[0] in ranges[1] else colourCodes[2] if item[0] in ranges[2] else item for item in imageArray]
    templateImage.putdata(newImage)
    templateImage.save(newFileName)

def addColourNamesToImage(randomColours, fontInfo, textLocations, newFileName):
    image = Image.open(newFileName)
    tmp = ImageDraw.Draw(image)
    #this is definitely gonna break when you use different templates. but thats an issue for future me.
    for index, item in enumerate(textLocations):
        tmp.text(item, '"' + randomColours[index].colourName + '"', fill=fontInfo.fill, stroke_fill=fontInfo.strokeFill, stroke_width=fontInfo.strokeWidth, font=fontInfo.font)
    image.save(newFileName)

#######-------------------------------------MAIN PROGRAM HERE----------------------------------------######

def __main__():
    randomColours = []
    textLocations = [(150,915), (150,500), (570,915)]
    numberOfColours = 3
    imageTemplate = "templates/3way_template.jpg"
    saveFolder = "generated/"
    if not os.path.exists(saveFolder):
        os.makedirs(saveFolder)
    
    newFileName = saveFolder + generateNewFileName()

    fontInfo = FontInfo('fonts/Verdanai.ttf', 24)
    fontInfo.fill = (250,250,250)
    fontInfo.strokeFill = (50,50,50)
    fontInfo.strokeWidth = 1

    ranges = [range(20,30), range(30,100), range(100,200)]
    
    img = loadTemplateImage(imageTemplate)

    for n in range(numberOfColours):
         colour = Colour()
         colourCode = colour.generateRandomColour()
         colourName = colour.getColourName(colourCode)
         colour.colourCode = colourCode
         colour.colourName = colourName
         randomColours.append(colour)

    createNewImageFromTemplate(img, randomColours, newFileName, ranges)
    addColourNamesToImage(randomColours, fontInfo, textLocations, newFileName)

startTime = time.time()
__main__()
print("--- %s seconds ---" % (time.time() - startTime))