#Ariana Daly + B + acdaly

import serial
import time
import pyaudio
import wave
import audioop

from tkinter import *

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
        self.barSlider = [0, 0, 0, 0] #[red, green, blue]
        self.barSliderWidth = 3
        self.barSliderOffset = 3 #bar height offset

        self.colorBoxSpacing = 50
        self.colorBoxWidth = 100
        self.colorBoxHeight = 100
        self.colorBoxX = self.barX + self.barWidth + self.colorBoxSpacing
        self.colorBoxY = self.bar1Y + 10

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


    def colorMousePressed(self, event):
        #within bars in x direction
        if self.barX <= event.x and event.x <= self.barX + self.barWidth:
            #within bar1 (red)
            if self.bar1Y <= event.y and event.y <= self.bar1Y + self.barHeight:
                self.barSlider[0] = int((event.x-self.barX) // self.barMultiple)
                serial_ref.write(bytearray("r " + str(self.barSlider[0]),
                                                                     'ascii')) 
            #within bar2 (green)
            if self.bar2Y <= event.y and event.y <= self.bar2Y + self.barHeight:
                self.barSlider[1] = int((event.x-self.barX) // self.barMultiple)
                serial_ref.write(bytearray("g " + str(self.barSlider[1]), 
                                                                     'ascii')) 
            #within bar3 (blue)
            if self.bar3Y <= event.y and event.y <= self.bar3Y + self.barHeight:
                self.barSlider[2] = int((event.x-self.barX) // self.barMultiple)
                serial_ref.write(bytearray("b " + str(self.barSlider[2]), 
                                                                     'ascii'))
            #within bar4 (white)
            if self.bar4Y <= event.y and event.y <= self.bar4Y + self.barHeight:
                self.barSlider[3] = int((event.x-self.barX) // self.barMultiple)
                serial_ref.write(bytearray("w " + str(self.barSlider[3]), 
                                                                     'ascii')) 


    def draw(self, canvas):
        canvas.create_rectangle(0, 0, self.windowWidth, self.windowHeight, 
                                                              fill="gray")
        self.colorBox(canvas)
        self.colorSet(canvas)

class BigBox(Background):
    def __init__(self):
        super().__init__()
        self.spaceToBox = self.barSpacing * 3
        self.X1 = self.barX
        self.X2 = self.windowWidth - self.barX
        self.Y1 = self.bar4Y + self.barHeight + self.spaceToBox
        self.Y2 = self.Y1 + 255 

        self.tenSec = self.X2 - self.X1
        self.everySec = self.tenSec / 10

        self.boxWidth = 30
        self.colorY1 = self.bar4Y + self.spaceToBox/2
        self.colorY2 = self.colorY1 + self.boxWidth
        self.redX1 = self.X1 + (self.tenSec/8) - self.boxWidth/2
        self.redX2 = self.redX1 + self.boxWidth
        self.greenX1 = self.redX1 + self.tenSec/4
        self.greenX2 = self.greenX1 + self.boxWidth
        self.blueX1 = self.greenX1 + self.tenSec/4
        self.blueX2 = self. blueX1 + self.boxWidth
        self.whiteX1 = self.blueX1 + self.tenSec/4
        self.whiteX2 = self.whiteX1 + self.boxWidth

        self.color = "" 
        self.red = {self.X1:self.Y2, self.X2:self.Y2}
        self.green = {self.X1:self.Y2, self.X2:self.Y2}
        self.blue = {self.X1:self.Y2, self.X2:self.Y2}
        self.white = {self.X1:self.Y2, self.X2:self.Y2}

        self.redLED = {}
        self.greenLED = {}
        self.blueLED = {}
        self.whiteLED = {}
        self.LEDs = [self.redLED, self.greenLED, self.blueLED, self.whiteLED]
        

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

        #if in the big box
        if (self.Y1 < event.y and event.y < self.Y2 and 
            self.X1 < event.x and event.x < self.X2):
            if self.color == "red":
                self.red[event.x] = event.y
            if self.color == "green":
                self.green[event.x] = event.y
            if self.color == "blue":
                self.blue[event.x] = event.y
            if self.color == "white":
                self.white[event.x] = event.y

        #if in dot

        
    def drawDots(self, canvas):
        r = 7
        for x in self.red:
            y = self.red[x]
            canvas.create_oval(x, y, x + r, y + r, fill = "red")
        for x in self.green:
            y = self.green[x]
            canvas.create_oval(x, y, x + r, y + r, fill = "green")
        for x in self.blue:
            y = self.blue[x]
            canvas.create_oval(x, y, x + r, y + r, fill = "blue")
        for x in self.white:
            y = self.white[x]
            canvas.create_oval(x, y, x + r, y + r, fill = "white")

    def drawLines(self, canvas):
        r = 7
        lastRedX = -1
        for x in sorted(self.red):
            if lastRedX == -1:
                lastRedX = x
            else:
                canvas.create_line(lastRedX + r/2, self.red[lastRedX] + r/2,
                                    x + r/2, self.red[x] + r/2, fill = "red")
                lastRedX = x
        lastGreenX = -1
        for x in sorted(self.green):
            if lastGreenX == -1:
                lastGreenX = x
            else:
                canvas.create_line(lastGreenX + r/2, self.green[lastGreenX]+r/2,
                                  x + r/2, self.green[x] + r/2, fill = "green")
                lastGreenX = x
        lastBlueX = -1
        for x in sorted(self.blue):
            if lastBlueX == -1:
                lastBlueX = x
            else:
                canvas.create_line(lastBlueX + r/2, self.blue[lastBlueX] + r/2,
                                    x + r/2, self.blue[x] + r/2, fill = "blue")
                lastBlueX = x
        lastWhiteX = -1
        for x in sorted(self.white):
            if lastWhiteX == -1:
                lastWhiteX = x
            else:
                canvas.create_line(lastWhiteX + r/2,self.white[lastWhiteX] +r/2,
                                   x + r/2, self.white[x] + r/2, fill = "black")
                lastWhiteX = x

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
        serial_ref = serial.Serial(port="/dev/cu.usbmodem1411",baudrate =230400)
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
        for index in range(len(brightnessList[0])):
            serial_ref.write(bytearray("r "+ str(int(brightnessList[0][index])), 
                                                                    'ascii'))
            serial_ref.write(bytearray("g "+ str(int(brightnessList[1][index])), 
                                                                    'ascii'))
            serial_ref.write(bytearray("b "+ str(int(brightnessList[2][index])), 
                                                                    'ascii'))
            serial_ref.write(bytearray("w "+ str(int(brightnessList[3][index])), 
                                                                    'ascii'))
            time.sleep(sleep)

def play(file):
    #from pyaudio demo
    CHUNK = 1024

    wf = wave.open(file, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()

def rgbString(red, green, blue):
    #taken from 112 notes
    return "#%02x%02x%02x" % (red, green, blue)

def init(data):
    data.create = [Background(), BigBox()]
    data.delete = False

def mousePressed(event, data):
    data.create[0].colorMousePressed(event)
    data.create[1].bigBoxMousePressed(event)

def redrawAll(canvas, data):
    for thing in data.create:
        thing.draw(canvas)

def keyPressed(event, data):
    if event.char == "d":
        data.delete = True
    if event.char == "h":
        data.delete = False
    if event.keysym == "space":
        data.create[1].fade()
    if event.char == "m":
        play("beats.wav")
        


def timerFired(data):
    pass

####################################
# use the run function as-is
####################################

def run(width=1000, height=1000):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
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

run()