#imports
from classes import Colour, FontInfo
import colornames
import numpy as np
import uuid
import time
from PIL import Image, ImageDraw
#end imports

#generate a random HEX-colour
def generateRandomColour():
    colour = tuple(np.random.choice(range(256), size=3))
    return colour
#end function

#load template image from file
def loadTemplateImage(imageTemplate):
    img = Image.open(imageTemplate)
    img = img.convert("RGB")
    return img
#end function

#generate new file name with random id
def generateNewFileName():
    return str(uuid.uuid4())+".png"
#end function

#fill template areas with random colours
def createNewImageFromTemplate(templateImage, randomColours, newFileName, ranges):
    #convert loaded template image to array
    imageArray = templateImage.getdata()
    #create empty array for new image data
    newImage = []
    #loop over all pixels in image-array, check the pre-defined colour ranges to replace those with random colours from the colourarray.
    for item in imageArray:
        if item[0] in ranges[0]:
            #change pixels with matching values to random colour from colourarray (convert to RGB here because lazy)
            newImage.append(randomColours[0].colourCode)
        elif item[0] in ranges[1]:
            newImage.append(randomColours[1].colourCode)
        elif item[0] in ranges[2]:
            newImage.append(randomColours[2].colourCode)
        else:
            newImage.append(item)
    #push new image data (array) to the template image, then save image
    templateImage.putdata(newImage)
    templateImage.save(newFileName)
#end function

#after generating an image, open it and add the corresponding colournames to the file
#its like this for now, because hardcoded positions in the image. can be improved later...
def addColourNamesToImage(randomColours, fontInfo, newFileName):
    image = Image.open(newFileName)
    tmp = ImageDraw.Draw(image)
    #add name for colour [0]
    tmp.text((150,915), '"' + randomColours[0].colourName + '"', fill=fontInfo.fill, stroke_fill=fontInfo.strokeFill, stroke_width=fontInfo.strokeWidth, font=fontInfo.font)
    #add name for colour [1]
    tmp.text((150,500), '"' + randomColours[1].colourName + '"', fill=fontInfo.fill, stroke_fill=fontInfo.strokeFill, stroke_width=fontInfo.strokeWidth, font=fontInfo.font)
    #add name for colour [2]
    tmp.text((570,915), '"' + randomColours[2].colourName + '"', fill=fontInfo.fill, stroke_fill=fontInfo.strokeFill, stroke_width=fontInfo.strokeWidth, font=fontInfo.font)
    image.save(newFileName)
#end function

#convert to hex and get colour name using colornames library
def getColourName(colourCode):
    colourName = colornames.find("#%02x%02x%02x" % colourCode)
    return colourName
#end function

#######----------------------------------------------------------------------------------------------######
#######-------------------------------------MAIN PROGRAM HERE----------------------------------------######
#######----------------------------------------------------------------------------------------------######
def __main__():
    #create array to store colours to display (using custom colour object)
    randomColours = []
    #amount of colours to generate. more than 3 doesnt matter for now, since the only template available supports 3 colours.
    numberOfColours = 3
    #template + default save path
    imageTemplate = "templates/3way_template.jpg"
    saveFolder = "generated/"
    #set fontInfo
    fontInfo = FontInfo('fonts/Verdanai.ttf', 24)
    fontInfo.fill = (250,250,250)
    fontInfo.strokeFill = (50,50,50)
    fontInfo.strokeWidth = 1

    #create empty array and add template filler (colour)ranges
    ranges = [range(20,30), range(30,100), range(100,200)]
    i = 0

    img = loadTemplateImage(imageTemplate)
    
    while i < numberOfColours:
         colour = Colour()
         colour.colourCode = generateRandomColour()
         colour.colourName = getColourName(colour.colourCode)
         randomColours.append(colour)
         i+=1

    newFileName = saveFolder + generateNewFileName()
    newImage = createNewImageFromTemplate(img, randomColours, newFileName, ranges)
    addColourNamesToImage(randomColours, fontInfo, newFileName)

#performance check -- for testing
startTime = time.time()
__main__()
print("--- %s seconds ---" % (time.time() - startTime))