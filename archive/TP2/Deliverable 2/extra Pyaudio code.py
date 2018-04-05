#Ariana Daly + B + acdaly

#This code was made before I switched my term project.
#With exception of fade() and inputBrightness(), they're all related to 
#the music files. A modified version of fade() will be used in my TP

import serial
import time
import pyaudio
import wave
import audioop

def getMaxRMS(file):
    #gets max RMS in order to make a correlation between rms and brightness
    wav = wave.open(file) #open file
    frames = wav.getnframes()

    width = wav.getsampwidth()
    maxRMS = 0
    for frame in range(frames):
        currentRMS = audioop.rms(wav.readframes(frame), width)
        if currentRMS > maxRMS: 
            maxRMS = currentRMS
    return maxRMS

def getMaxRMSWithStream(file):
    seconds = 10
    wav = wave.open(file) #open file
    width = wav.getsampwidth()
    chunk = 2048
    rate = 44100
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wav.getsampwidth()),
                channels = 1,
                rate = 44100,
                input = True,
                frames_per_buffer = chunk)
    maxRMS = 0
    rmsList = []
    for i in range(0, int(rate / chunk * seconds)):
        data = stream.read(chunk)
        rms = audioop.rms(data, 2)
        if rms > maxRMS: 
            maxRMS = rms
        rmsList.append(data)
    return (rmsList, maxRMS)

    stream.stop_stream()
    stream.close()
    p.terminate()

def sendBrightness(file):
    #uses the RMS sends the corresponding brightness to the LEDs
    wav = wave.open(file) #open file
    width = wav.getsampwidth()
    serial_ref = serial.Serial(port="/dev/cu.usbmodem1411", baudrate = 230400)
    maxRMS = getMaxRMS(file)
    maxBrightness = 255
    rmsToBrightness = maxBrightness/maxRMS

    frames = wav.getnframes()
    for frame in range(frames):
        data = audioop.rms(wav.readframes(frame), width) #RMS
        data = data * rmsToBrightness #brightness
        print(data)
        assert(data <= maxBrightness)
        serial_ref.write(bytearray("r " + str(data), 'ascii')) 

def getRMSWithStream(file):
    #uses chunks instead of single frames in order to save on processing power
    seconds = 5
    wav = wave.open(file) #open file
    width = wav.getsampwidth()
    chunk = 1028
    rate = 44100
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wav.getsampwidth()),
                channels = 1,
                rate = 44100,
                input = True,
                frames_per_buffer = chunk)
    for i in range(0, int(rate / chunk * seconds)):
        width = wav.getsampwidth()
        data = stream.read(chunk)
        rms = audioop.rms(data, width)
        print(rms, width)

    stream.stop_stream()
    stream.close()
    p.terminate()

def sendBrightnessWithStream(file):
    serial_ref = serial.Serial(port="/dev/cu.usbmodem1411", baudrate = 230400)
    seconds = 10
    wav = wave.open(file) #open file
    width = wav.getsampwidth()
    chunk = 2048
    rate = 44100
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wav.getsampwidth()),
                channels = 1,
                rate = 44100,
                input = True,
                frames_per_buffer = chunk)
    (rmsList, maxRMS) = getMaxRMSWithStream(file)
    maxBrightness = 255
    rmsToBrightness = maxBrightness/maxRMS
    for i in range(0, int(rate / chunk * seconds)):
        rms = audioop.rms(rmsList[i], 2)
        print(rms)
        data = rms * rmsToBrightness #brightness
        serial_ref.write(bytearray("b " + str(int(data)), 'ascii'))
        time.sleep(.05)

    stream.stop_stream()
    stream.close()
    p.terminate()

def ready():
    serial_ref = serial.Serial(port="/dev/cu.usbmodem1411", baudrate = 115200)
    data = input("> ")
    serial_ref.write(bytearray(data, 'ascii'))

def fade():
    serial_ref = serial.Serial(port="/dev/cu.usbmodem1411", baudrate = 230400)
    data = 5
    direction = 5
    L = []
    D = []
    for i in range(1000): L.append(i)
    for x in L:
        if data > 254 or data < 1:
            direction *= -1
        data += direction

        D.append(data)
    for element in D:
        print(element)
        serial_ref.write(bytearray("r " + str(data), 'ascii'))
        time.sleep(.01)

def inputBrightness():
    #turn on/off an LED by entering 1 (on) or 0 (off)
    serial_ref = serial.Serial(port="/dev/cu.usbmodem1411", baudrate = 230400)
    while True:
        data = input("> ")
        serial_ref.write(bytearray(data, 'ascii'))
L = [0, 6.313907284768212, 12.627814569536424, 18.941721854304635, 25.25562913907285, 31.56953642384106, 37.88344370860927, 44.19735099337748, 50.5112582781457, 56.82516556291391, 63.13907284768212, 69.45298013245034, 75.76688741721854, 82.08079470198675, 88.39470198675495, 94.70860927152316, 101.02251655629136, 107.33642384105957, 113.65033112582778, 119.96423841059598, 126.27814569536419, 132.5920529801324, 138.9059602649006, 145.21986754966883, 151.53377483443705, 157.84768211920527, 164.1615894039735, 170.4754966887417, 176.78940397350993, 183.10331125827815, 189.41721854304637, 195.7311258278146, 202.04503311258281, 208.35894039735103, 214.67284768211925, 220.98675496688747, 227, 223.4557620817844, 219.9115241635688, 216.3672862453532, 212.8230483271376, 209.278810408922, 205.7345724907064, 202.1903345724908, 198.6460966542752, 195.1018587360596, 191.557620817844, 188.0133828996284, 184.4691449814128, 180.9249070631972, 177.3806691449816, 173.836431226766, 170.2921933085504, 166.7479553903348, 163.2037174721192, 159.6594795539036, 156.115241635688, 152.5710037174724, 149.0267657992568, 145.4825278810412, 141.9382899628256, 138.39405204461, 134.8498141263944, 131.3055762081788, 127.76133828996318, 124.21710037174756, 120.67286245353195, 117.12862453531633, 113.58438661710072, 110.0401486988851, 106.49591078066949, 102.95167286245388, 99.40743494423826, 95.86319702602265, 92.31895910780703, 88.77472118959142, 85.2304832713758, 81.68624535316019, 78.14200743494457, 74.59776951672896, 71.05353159851335, 67.50929368029773, 63.965055762082116, 60.4208178438665, 56.87657992565089, 53.33234200743527, 49.78810408921966, 46.24386617100404, 42.69962825278843, 39.155390334572814, 35.6111524163572, 32.066914498141585, 28.52267657992597, 24.978438661710356, 21.434200743494742, 17.889962825279127, 14.345724907063515, 10.801486988847902, 7.257249070632289, 3.713011152416676, 0.16877323420106283]

def fadeHardCode(list):
    serial_ref = serial.Serial(port="/dev/cu.usbmodem1411", baudrate = 230400)
    for element in L:
        print(element)
        serial_ref.write(bytearray("r " + str(element), 'ascii'))
        time.sleep(.1)

inputBrightness()
#fadeHardCode(L)
