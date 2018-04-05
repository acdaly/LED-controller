#Ariana Daly + B + acdaly

import serial
import time
import sys
import os
import ast

from tkinter import *
import tkinter

#serial_ref = serial.Serial(port="/dev/cu.usbmodem1411", baudrate = 230400)


class Background(object):
    def __init__(self):
        self.windowWidth = 1000
        self.windowHeight = 1000

        self.barWidth = 510
        self.barMultiple = self.barWidth / 255
        self.barHeight = 20
        self.barX = 80
        self.barSpacing = 50
        self.bar1Y = 50
        self.bar2Y = self.bar1Y + self.barSpacing
        self.bar3Y = self.bar2Y + self.barSpacing
        self.bar4Y = self.bar3Y + self.barSpacing
        self.barSlider = [0, 0, 0, 0] #[red, green, blue, white]
        self.barSliderWidth = 3
        self.barSliderOffset = 3 #bar height offset

        self.colorBoxSpacing = 50
        self.colorBoxWidth = 100
        self.colorBoxHeight = 100
        self.colorBoxX = self.barX + self.barWidth + self.colorBoxSpacing
        self.colorBoxY = self.bar1Y + 10

        self.helpX1 = self.windowWidth - 100
        self.helpX2 = self.windowWidth 
        self.helpY1 = 0
        self.helpY2 = 25
        self.splashScreen = False
        self.image = None


    def redBar(self, canvas):
        canvas.create_rectangle(self.barX, self.bar1Y, 
                                self.barX + self.barWidth,
                                self.bar1Y + self.barHeight, fill="white")
        canvas.create_text(self.barX/2, self.bar1Y, text = "R", anchor = N)

            #barSlider
        sliderX1 = (self.barX + (self.barSlider[0] * self.barMultiple) 
                                                     - self.barSliderWidth//2)
        sliderX2 = (self.barX + (self.barSlider[0] * self.barMultiple) 
                                                     + self.barSliderWidth//2)
        sliderY1 = self.bar1Y - self.barSliderOffset
        sliderY2 = self.bar1Y + self.barHeight + self.barSliderOffset
        canvas.create_rectangle(sliderX1, sliderY1, sliderX2, sliderY2,
                                                                fill="black")

    def greenBar(self, canvas):
        canvas.create_rectangle(self.barX, self.bar2Y, 
                                self.barX + self.barWidth,
                                self.bar2Y + self.barHeight, fill="white")
        canvas.create_text(self.barX/2, self.bar2Y, text = "G", anchor = N)

            #barSlider
        sliderX1 = (self.barX + (self.barSlider[1] * self.barMultiple) 
                                                     - self.barSliderWidth//2)
        sliderX2 = (self.barX + (self.barSlider[1] * self.barMultiple) 
                                                     + self.barSliderWidth//2)
        sliderY1 = self.bar2Y - self.barSliderOffset
        sliderY2 = self.bar2Y + self.barHeight + self.barSliderOffset
        canvas.create_rectangle(sliderX1, sliderY1, sliderX2, sliderY2,
                                                                fill="black")

    def blueBar(self, canvas):
        canvas.create_rectangle(self.barX, self.bar3Y, 
                                self.barX + self.barWidth,
                                self.bar3Y + self.barHeight, fill="white")
        canvas.create_text(self.barX/2, self.bar3Y, text = "B", anchor = N)

            #barSlider
        sliderX1 = (self.barX + (self.barSlider[2] * self.barMultiple) 
                                                     - self.barSliderWidth//2)
        sliderX2 = (self.barX + (self.barSlider[2] * self.barMultiple) 
                                                     + self.barSliderWidth//2)
        sliderY1 = self.bar3Y - self.barSliderOffset
        sliderY2 = self.bar3Y + self.barHeight + self.barSliderOffset
        canvas.create_rectangle(sliderX1, sliderY1, sliderX2, sliderY2,
                                                                fill="black")

    def whiteBar(self, canvas):
        canvas.create_rectangle(self.barX, self.bar4Y, 
                                self.barX + self.barWidth,
                                self.bar4Y + self.barHeight, fill="white")
        canvas.create_text(self.barX/2, self.bar4Y, text = "W", anchor = N)

            #barSlider
        sliderX1 = (self.barX + (self.barSlider[3] * self.barMultiple) 
                                                     - self.barSliderWidth//2)
        sliderX2 = (self.barX + (self.barSlider[3] * self.barMultiple) 
                                                     + self.barSliderWidth//2)
        sliderY1 = self.bar4Y - self.barSliderOffset
        sliderY2 = self.bar4Y + self.barHeight + self.barSliderOffset
        canvas.create_rectangle(sliderX1, sliderY1, sliderX2, sliderY2,
                                                                fill="black")


    def colorSet(self, canvas):
        self.redBar(canvas)
        self.greenBar(canvas)
        self.blueBar(canvas)
        self.whiteBar(canvas)

    def colorBox(self, canvas):
        color=rgbString(self.barSlider[0], self.barSlider[1], self.barSlider[2])
        canvas.create_rectangle(self.colorBoxX, self.colorBoxY, 
                                self.colorBoxX + self.colorBoxWidth,
                                self.colorBoxY + self.colorBoxHeight,fill=color)

    def help(self, canvas):
        x1 = self.helpX1
        x2 = self.helpX2
        y1 = self.helpY1
        y2 = self.helpY2
        color = "black"

        canvas.create_rectangle(x1, y1, x2, y2, fill = color)
        canvas.create_text(x1 + (x2 - x1)/2, y1 + (y2 - y1)/2, 
                                    text = "instructions", fill = "white")

    def getBarSlider(self):
        return self.barSlider

    def createSplashScreen(self, canvas):
        self.image = tkinter.PhotoImage(file="instructions2.gif")
        canvas.create_image(self.windowWidth/2 + 2, self.windowHeight/2 - 122, 
                                                            image = self.image)


    def colorMousePressed(self, event):
        #within bars in x direction
        if self.barX <= event.x and event.x <= self.barX + self.barWidth:
            #within bar1 (red)
            if self.bar1Y <= event.y and event.y <= self.bar1Y + self.barHeight:
                self.barSlider[0] = int((event.x-self.barX) // self.barMultiple)
                #serial_ref.write(bytearray("r " + str(self.barSlider[0]),
                                                                     #'ascii')) 
            #within bar2 (green)
            if self.bar2Y <= event.y and event.y <= self.bar2Y + self.barHeight:
                self.barSlider[1] = int((event.x-self.barX) // self.barMultiple)
                #serial_ref.write(bytearray("g " + str(self.barSlider[1]), 
                                                                     #'ascii')) 
            #within bar3 (blue)
            if self.bar3Y <= event.y and event.y <= self.bar3Y + self.barHeight:
                self.barSlider[2] = int((event.x-self.barX) // self.barMultiple)
                #serial_ref.write(bytearray("b " + str(self.barSlider[2]), 
                                                                    #'ascii'))
            #within bar4 (white)
            if self.bar4Y <= event.y and event.y <= self.bar4Y + self.barHeight:
                self.barSlider[3] = int((event.x-self.barX) // self.barMultiple)
                #serial_ref.write(bytearray("w " + str(self.barSlider[3]), 
                                                                    #'ascii')) 
        #within help
        if self.helpX1 <= event.x and event.x <= self.helpX2:
            if self.helpY1 <= event.y and event.y <= self.helpY2:
                self.splashScreen = True

    def draw(self, canvas):
        canvas.create_rectangle(0, 0, self.windowWidth, self.windowHeight, 
                                                              fill="gray")
        self.colorBox(canvas)
        self.colorSet(canvas)
        self.help(canvas)

class BigBox(Background):
    def __init__(self):
        super().__init__()
        self.spaceToBox = self.barSpacing * 3
        self.X1 = self.barX
        self.X2 = self.windowWidth - self.barX
        self.Y1 = self.bar4Y + self.barHeight + self.spaceToBox
        self.Y2 = self.Y1 + 255 

        self.timeBoxWidth = 25
        xFromEdge = 25
        yFromEdge = 60
        arrowGap = 15
        self.secBoxDownX = [self.X2 - self.timeBoxWidth - xFromEdge,
            self.X2 - xFromEdge] #[x1, x2]
        self.secBoxUpX = [self.secBoxDownX[0] - self.timeBoxWidth - arrowGap, 
            self.secBoxDownX[0] - arrowGap] #[x1, x2]
        self.timeUpDownY = [self.Y2 + yFromEdge, 
                            self.Y2 + yFromEdge + self.timeBoxWidth]

        self.timeCount = 10
        self.timePixels = self.X2 - self.X1
        self.everySec = self.timePixels / self.timeCount

        #mini color Boxes
        self.boxWidth = 30
        self.colorY1 = self.bar4Y + self.spaceToBox/2
        self.colorY2 = self.colorY1 + self.boxWidth
        self.redX1 = self.X1 + (self.timePixels/8) - self.boxWidth/2
        self.redX2 = self.redX1 + self.boxWidth
        self.greenX1 = self.redX1 + self.timePixels/4
        self.greenX2 = self.greenX1 + self.boxWidth
        self.blueX1 = self.greenX1 + self.timePixels/4
        self.blueX2 = self. blueX1 + self.boxWidth
        self.whiteX1 = self.blueX1 + self.timePixels/4
        self.whiteX2 = self.whiteX1 + self.boxWidth

        self.color = "" 
        self.red = {self.X1:self.Y2, self.X2:self.Y2}
        self.green = {self.X1:self.Y2, self.X2:self.Y2}
        self.blue = {self.X1:self.Y2, self.X2:self.Y2}
        self.white = {self.X1:self.Y2, self.X2:self.Y2}
        self.colors = [self.red, self.green, self.blue, self.white]

        self.redLED = {}
        self.greenLED = {}
        self.blueLED = {}
        self.whiteLED = {}
        self.LEDs = [self.redLED, self.greenLED, self.blueLED, self.whiteLED]
        self.brightnessList = []

        self.resetX1 = self.X2
        self.resetX2 = self.X2 - 80
        self.resetY1 = self.Y1 - 20
        self.resetY2 = self.Y1

        self.loopX1 = self.resetX2 - (self.resetX1 - self.resetX2) 
        self.loopX2 = self.resetX2
        self.loopY1 = self.resetY1
        self.loopY2 = self.resetY2
        self.loopColor = "black"
        self.loopText = "white"
        self.loop = False

        loadSaveWidth = 50
        (self.loadX1, self.loadX2) = (self.X1 + 20,self.X1 + loadSaveWidth + 20)
        (self.saveX1, self.saveX2) = (self.loadX2 + loadSaveWidth + 20, self.loadX2 + 20)
        self.loadSaveY1 = self.timeUpDownY[0]
        self.loadSaveY2 = self.timeUpDownY[1]
        self.save = False
        self.load = False
        self.loadWidth = 40
        self.loadScreenY = []
        self.loadFiles = []
        self.loadNames = []
        self.getBrightnessList()

    def bigBoxMousePressed(self, event):
        #if in the mini color boxes
        if self.colorY1 < event.y and event.y < self.colorY2:
            if self.redX1 < event.x and event.x < self.redX2:
                self.color = "red"
            if self.greenX1 < event.x and event.x < self.greenX2:
                self.color = "green"
            if self.blueX1 < event.x and event.x < self.blueX2:
                self.color = "blue"
            if self.whiteX1 < event.x and event.x < self.whiteX2:
                self.color = "white"

        #if in sample color box
        if (self.colorBoxY < event.y and 
                                event.y < self.colorBoxY + self.colorBoxHeight):
            if (self.colorBoxX < event.x and 
                                   event.x < self.colorBoxX+self.colorBoxWidth):
                self.color = "rgbw"

        #if in the big box
        if (self.Y1 < event.y and event.y < self.Y2 and 
            self.X1 < event.x and event.x < self.X2):
            if self.color == "red":
                self.checkDots("red", event.x)
                self.red[event.x] = event.y
            if self.color == "green":
                self.checkDots("green", event.x)
                self.green[event.x] = event.y
            if self.color == "blue":
                self.checkDots("blue", event.x)
                self.blue[event.x] = event.y
            if self.color == "white":
                self.checkDots("white", event.x)
                self.white[event.x] = event.y
            self.getBrightnessList()
        #if in reset
        if (self.resetY1 < event.y and event.y < self.resetY2 and
            self.resetX1 > event.x and event.x > self.resetX2):
            self.red = {self.X1:self.Y2, self.X2:self.Y2}
            self.green = {self.X1:self.Y2, self.X2:self.Y2}
            self.blue = {self.X1:self.Y2, self.X2:self.Y2}
            self.white = {self.X1:self.Y2, self.X2:self.Y2}
            self.redLED = {}
            self.greenLED = {}
            self.blueLED = {}
            self.whiteLED = {}
            self.LEDs = [self.redLED,self.greenLED, self.blueLED, self.whiteLED]
            self.getBrightnessList()
        #if in loop
        if (self.loopY1 < event.y and event.y < self.loopY2 and 
            self.loopX1 < event.x and event.x < self.loopX2):
            if self.loopColor == "black":
                self.loopText = "black"
                self.loopColor = "red"
                self.loop = True
            else: 
                self.loopText = "white"
                self.loopColor =  "black"
                self.loop = False
        
        if self.timeUpDownY[0] < event.y and event.y < self.timeUpDownY[1]:
            #if in time 
            if self.secBoxDownX[0] < event.x and event.x < self.secBoxDownX[1]:
                if self.timeCount > 10: 
                    self.timeCount -=10
                    self.everySec = self.timePixels / self.timeCount
            if self.secBoxUpX[0] < event.x and event.x < self.secBoxUpX[1]:
                self.timeCount +=10
                self.everySec = self.timePixels / self.timeCount
            #if in load
            if self.loadX1 < event.x and event.x < self.loadX2:
                self.load = True
            #if in save
            if self.saveX1 > event.x and event.x > self.saveX2:
                files = len(self.listFiles("Files"))
                if files == 0: newFile = open("Files/Save", 'w')
                else: newFile = open(("Files/Save " + str(files + 1)), 'w')
                newFile.write(str(self.LEDs) + '\n' + str(self.colors))
                newFile.close()
                self.save = True

        if self.load == True:
            for i in range(len(self.loadScreenY)):
                y = self.loadScreenY[i]
                y -= 20
                if y < event.y and event.y < (y + self.loadWidth):
                    file = open(self.loadFiles[i])
                    contents = file.readlines()
                    self.LEDs = ast.literal_eval(contents[0])
                    self.redLED = self.LEDs[0]
                    self.greenLED = self.LEDs[1]
                    self.blueLED = self.LEDs[2]
                    self.whiteLED = self.LEDs[3]
                    self.colors = ast.literal_eval(contents[1])
                    self.red = self.colors[0]
                    self.green = self.colors[1]
                    self.blue = self.colors[2]
                    self.white = self.colors[3]
                    file.close()

    def getBrightnessList(self):
        brightnessList = [[],[],[],[]]
        self.createLEDs()
        (lastX, lastY) = (0, 0)
        (seconds, sleep) = (0, .05)
        rgbw = [0, 1, 2, 3]
        for color in rgbw:
            for sec in sorted(self.LEDs[color]):
                if sec != 0:
                    brightness = lastY
                    y = self.LEDs[color][sec]
                    cx = sec - lastX
                    cy = y - lastY
                    direction = (cy/cx) * sleep
                    while seconds < sec:
                        brightnessList[color].append(brightness)
                        brightness += direction
                        seconds += sleep
                    (lastX, lastY) = (sec, self.LEDs[color][sec])
            (lastX, lastY, seconds) = (0, 0, 0)
        self.brightnessList = brightnessList
    def drawDots(self, canvas):
        r = 7
        for x in self.red:
            y = self.red[x]
            canvas.create_oval(x - r/2, y - r/2, x + r/2, y + r/2, fill = "red")
        for x in self.green:
            y = self.green[x]
            canvas.create_oval(x - r/2, y - r/2, x+r/2, y + r/2, fill = "green")
        for x in self.blue:
            y = self.blue[x]
            canvas.create_oval(x - r/2, y - r/2, x +r/2, y + r/2, fill = "blue")
        for x in self.white:
            y = self.white[x]
            canvas.create_oval(x-r/2, y - r/2, x + r/2, y + r/2, fill = "white")

    def checkDots(self, color, eventX):
        #delete dots if they're too close together
        pixels = 5
        deleteList = []
        if color == "red":
            L = self.red
        if color == "green":
            L = self.green
        if color == "blue":
            L = self.blue
        if color == "white":
            L = self.white
        for x in L:
            if abs(x - eventX) < pixels:
                deleteList.append(x)
        for element in deleteList:
            del L[element]

    def drawLines(self, canvas):
        r = 7
        lastRedX = -1
        for x in sorted(self.red):
            if lastRedX == -1:
                lastRedX = x
            else:
                canvas.create_line(lastRedX, self.red[lastRedX],
                                    x, self.red[x], fill = "red")
                lastRedX = x
        lastGreenX = -1
        for x in sorted(self.green):
            if lastGreenX == -1:
                lastGreenX = x
            else:
                canvas.create_line(lastGreenX, self.green[lastGreenX],
                                  x, self.green[x], fill = "green")
                lastGreenX = x
        lastBlueX = -1
        for x in sorted(self.blue):
            if lastBlueX == -1:
                lastBlueX = x
            else:
                canvas.create_line(lastBlueX, self.blue[lastBlueX],
                                    x, self.blue[x], fill = "blue")
                lastBlueX = x
        lastWhiteX = -1
        for x in sorted(self.white):
            if lastWhiteX == -1:
                lastWhiteX = x
            else:
                canvas.create_line(lastWhiteX,self.white[lastWhiteX],
                                   x, self.white[x], fill = "black")
                lastWhiteX = x


    def listFiles(self, path):
    #copied from 112 notes
    #https://www.cs.cmu.edu/~112/notes/notes-recursion-examples.html#listFiles
        if (os.path.isdir(path) == False):
            # base case:  not a folder, but a file
            return [path]
        else:
            # recursive case: it's a folder, return list of all paths
            files = [ ]
            for filename in os.listdir(path):
                files += self.listFiles(path + "/" + filename)
            return files

    def absFiles(self, path):
    #modified listFiles 112 notes
        if (os.path.isdir(path) == False):
            # base case:  not a folder, but a file
            return [os.path.abspath('.') + "/" + path]
        else:
            # recursive case: it's a folder, return list of all paths
            files = [ ]
            for filename in os.listdir(path):
                files += self.listFiles(path + "/" + filename)
            return files

    def drawLoad(self, canvas):
        canvas.create_rectangle(0, 0, self.windowWidth, self.windowHeight, 
                                                                fill = "white")
        self.loadFiles = self.absFiles("Files")
        self.fileNames = self.listFiles("Files")
        loadScreenY = []
        xL = []
        width = self.loadWidth
        for file in range(len(self.loadFiles)):
            loadScreenY.append(width)
            canvas.create_text(20, width, text = self.fileNames[file], anchor=W)
            width += 40
        self.loadScreenY = loadScreenY

    def drawSample(self, canvas):
        y1 = self.Y2 + (self.timeUpDownY[1] - self.Y2)/4
        y2 = self.Y2 + (self.timeUpDownY[1] - self.Y2)/2
        
        canvas.create_rectangle(self.X1, y1, self.X2, y2, fill = "white")
        width = self.X2 - self.X1
        if len(self.brightnessList) != 0:
            miniWidth = width / (len(self.brightnessList[0]))
            x = 0
            for i in range(len(self.brightnessList[0])):
                canvas.create_rectangle(self.X1 + x, y1 + 1, self.X2, y2,
                    fill = rgbString(int(self.brightnessList[0][i]), 
                        int(self.brightnessList[1][i]), 
                        int(self.brightnessList[2][i])), width = 0)
                x += miniWidth


        
    def draw(self, canvas):
        canvas.create_rectangle(self.redX1, self.colorY1, self.redX2, 
                                                     self.colorY2, fill = "red")
        canvas.create_rectangle(self.greenX1, self.colorY1, self.greenX2, 
                                                   self.colorY2, fill = "green")
        canvas.create_rectangle(self.blueX1, self.colorY1, self.blueX2, 
                                                      self.colorY2, fill="blue")
        canvas.create_rectangle(self.whiteX1, self.colorY1, self.whiteX2, 
                                                     self.colorY2, fill="white")
        canvas.create_rectangle(self.X1, self.Y1, self.X2, self.Y2,fill="white")

        self.drawLines(canvas)
        self.drawDots(canvas)
        self.reset(canvas)
        self.drawLoop(canvas)
        self.drawTime(canvas)
        self.line(canvas)
        self.loadAndSave(canvas)
        self.drawSample(canvas)
        if self.load == True:
            self.drawLoad(canvas)
            self.getBrightnessList()
        

    def line(self, canvas):
        lines = self.timeCount // 10
        (y1, y2) = (self.Y1, self.Y2)
        for line in range(lines):
            x = self.everySec * (10 * line) + self.X1
            canvas.create_line(x, y1, x, y2)

    def drawLoop(self, canvas):
        x1 = self.loopX1
        x2 = self.loopX2
        y1 = self.loopY1
        y2 = self.loopY2
        canvas.create_rectangle(x1, y1, x2, y2, fill = self.loopColor)
        canvas.create_text(x1 + (x2 - x1)/2, y1 + (y2 - y1)/2, 
                                            fill = self.loopText, text = "loop")

    def drawTime(self, canvas):
        #create boxes
        canvas.create_rectangle(self.secBoxUpX[0],self.timeUpDownY[0],
                        self.secBoxUpX[1],self.timeUpDownY[1], fill = "black")
        canvas.create_rectangle(self.secBoxDownX[0],self.timeUpDownY[0],
                        self.secBoxDownX[1],self.timeUpDownY[1], fill = "black")
        #create arrows
        upMid = (self.secBoxUpX[0]+self.timeBoxWidth/2, self.timeUpDownY[0]+8)
        upLeft = (self.secBoxUpX[0]+7,self.timeUpDownY[1]-7)
        upRight = (self.secBoxUpX[1] - 7, self.timeUpDownY[1] - 7)
        canvas.create_polygon([upMid, upLeft, upRight], fill="green")

        downMid = (self.secBoxDownX[0]+self.timeBoxWidth/2, 
                                                        self.timeUpDownY[1]-7)
        downLeft = (self.secBoxDownX[0]+7,self.timeUpDownY[0]+8)
        downRight = (self.secBoxDownX[1] - 7, self.timeUpDownY[0] + 8)
        canvas.create_polygon([downMid, downLeft, downRight], fill="green")
        #create text
        canvas.create_text(self.secBoxUpX[0] - 30, 
                                    self.timeUpDownY[0] + self.timeBoxWidth/2, 
                                           text = "sec " + str(self.timeCount))

    def loadAndSave(self, canvas):
        loadSaveWidth = 50
        #load
        (loadX1, loadX2) = (self.X1 + 20, self.X1 + loadSaveWidth + 20)
        (y1, y2) = (self.timeUpDownY[0], self.timeUpDownY[1])
        loadTextX = self.X1 + 20 + loadSaveWidth/2
        textY= self.timeUpDownY[1]-(self.timeUpDownY[1] - self.timeUpDownY[0])/2
        canvas.create_rectangle(loadX1, y1, loadX2, y2, fill = "black")
        canvas.create_text(loadTextX, textY, fill = "yellow", text = "load")
        #save
        (saveX1, saveX2) = (loadX2 + loadSaveWidth + 20, loadX2 + 20)
        canvas.create_rectangle(saveX1, y1, saveX2, y2, fill = "black")
        canvas.create_text(saveX1 + (saveX2 - saveX1)/2, textY,
                                                fill = "yellow", text = "save")

    def reset(self, canvas):
        x1 = self.resetX1
        x2 = self.resetX2
        y1 = self.resetY1
        y2 = self.resetY2
        canvas.create_rectangle(x1, y1, x2, y2, fill = "black")
        canvas.create_text(x1 + (x2 - x1)/2, y1 + (y2 - y1)/2, 
                                                fill = "white", text = "reset")

    def createLEDs(self):
        for x in self.red:
            time = (x - self.X1) / self.everySec
            brightness = self.Y2 - self.red[x]
            self.redLED[time] = brightness
        for x in self.green:
            time = (x - self.X1) / self.everySec
            brightness = self.Y2 - self.green[x]
            self.greenLED[time] = brightness
        for x in self.blue:
            time = (x - self.X1) / self.everySec
            brightness = self.Y2 - self.blue[x]
            self.blueLED[time] = brightness
        for x in self.white:
            time = (x - self.X1) / self.everySec
            brightness = self.Y2 - self.white[x]
            self.whiteLED[time] = brightness

    def fade(self):
        #serial_ref = serial.Serial(port="/dev/cu.usbmodem1411",baudrate =230400)
        brightnessList = [[],[],[],[]]
        self.createLEDs()
        (lastX, lastY) = (0, 0)
        (seconds, sleep) = (0, .05)
        rgbw = [0, 1, 2, 3]
        for color in rgbw:
            for sec in sorted(self.LEDs[color]):
                if sec != 0:
                    brightness = lastY
                    y = self.LEDs[color][sec]
                    cx = sec - lastX
                    cy = y - lastY
                    direction = (cy/cx) * sleep
                    while seconds < sec:
                        brightnessList[color].append(brightness)
                        brightness += direction
                        seconds += sleep
                    (lastX, lastY) = (sec, self.LEDs[color][sec])
            (lastX, lastY, seconds) = (0, 0, 0)
        self.brightnessList = brightnessList
        for index in range(len(self.brightnessList[0])):
            # serial_ref.write(bytearray("r "+ str(int(brightnessList[0][index])), 
            #                                                         'ascii'))
            # serial_ref.write(bytearray("g "+ str(int(brightnessList[1][index])), 
            #                                                         'ascii'))
            # serial_ref.write(bytearray("b "+ str(int(brightnessList[2][index])), 
            #                                                         'ascii'))
            # serial_ref.write(bytearray("w "+ str(int(brightnessList[3][index])), 
            #                                                         'ascii'))
            time.sleep(sleep)
        if self.loop:
            #repeat if loop was clicked
            self.fade()

        


def rgbString(red, green, blue):
    #taken from 112 notes
    return "#%02x%02x%02x" % (red, green, blue)

def init(data):
    data.background = Background()
    data.bigBox = BigBox()
    data.create = [data.background, data.bigBox]
    data.delete = False
    data.lineX =  data.bigBox.X1

def receiveBarSlider(data):
    return data.create[0].getBarSlider

def inBox(event, data):
    if (data.bigBox.Y1 < event.y and event.y < data.bigBox.Y2 and 
            data.bigBox.X1 < event.x and event.x < data.bigBox.X2):
        if data.bigBox.color == "rgbw":
            data.bigBox.red[event.x] = (data.bigBox.Y2 - 
                                                data.background.barSlider[0])
            data.bigBox.green[event.x] = (data.bigBox.Y2 - 
                                                data.background.barSlider[1])
            data.bigBox.blue[event.x] = (data.bigBox.Y2 - 
                                                data.background.barSlider[2])
            data.bigBox.white[event.x] = (data.bigBox.Y2 - 
                                                data.background.barSlider[3])
            data.bigBox.getBrightnessList()

def mousePressed(event, data):
    data.create[0].colorMousePressed(event)
    data.create[1].bigBoxMousePressed(event)
    inBox(event, data)

def redrawAll(canvas, data):
    if data.create[0].splashScreen == False:
        for thing in data.create:
            thing.draw(canvas)
    else:
        data.create[0].createSplashScreen(canvas)

def keyPressed(event, data, canvas):
    if event.char == "d":
        data.delete = True
    if event.char == "h":
        data.delete = False
    if event.keysym == "space":
        data.create[1].fade()
    if event.char == "m":
        newPlay("beats.wav", data, canvas)
    if event.keysym == "Escape":
        data.create[0].splashScreen = False
        data.bigBox.load = False
        data.bigBox.save = False
        

def timerFired(data):
    pass

####################################
# use the run function as-is
####################################

def removeDsStore(path):
    #from 112 notes
    if (os.path.isdir(path) == False):
        if (path.endswith(".DS_Store")):
            print("removing:", path)
            os.remove(path)
    else:
        # recursive case: it's a folder
        for filename in os.listdir(path):
            removeDsStore(path + "/" + filename)

def run(width=1000, height=1000):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data, canvas)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")
removeDsStore("Files")
run()