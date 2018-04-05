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
    while True:
        if data > 254 or data < 1:
            direction *= -1
        data += direction
        print(data)
        serial_ref.write(bytearray("r " + str(data), 'ascii'))
        serial_ref.write(bytearray("b " + str(data), 'ascii'))
        time.sleep(.001)

def inputBrightness():
    #turn on/off an LED by entering 1 (on) or 0 (off)
    serial_ref = serial.Serial(port="/dev/cu.usbmodem1411", baudrate = 230400)
    while True:
        data = input("> ")
        serial_ref.write(bytearray(data, 'ascii'))

inputBrightness()

#below used to be in the classes in my TP3

def play(file, data, canvas):
    t1 = time.time()
    #modified pyaudio demo https://people.csail.mit.edu/hubert/pyaudio/docs/
    CHUNK = 1024

    wf = wave.open(file, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    playData = wf.readframes(CHUNK)
    t1 = time.time()
    count = 0
    while len(playData) > 0:
        count += 1
        stream.write(playData)
        playData = wf.readframes(CHUNK)
        t2 = time.time()
        
        if count == 1: total_time = t2-t1
        redrawAll(canvas, data)
    data.lineX += 50
    time.sleep(1)
    print("yay!")
        #print(data.lineX)

    stream.stop_stream()
    stream.close()

    p.terminate()

def weirdPlay(file, data, canvas):
    dataList = []
    CHUNK = 1024

    wf = wave.open(file, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    playData = wf.readframes(CHUNK)
    dataList.append(playData)
    t1 = time.time()
    count = 0
    while len(playData) > 0:
        stream.write(playData)
        playData = wf.readframes(CHUNK)
        dataList.append(playData)
    stream.stop_stream()
    stream.close()
    return dataList

def callback(in_data, frame_count, time_info, status):
    #from pyaudio demo https://people.csail.mit.edu/hubert/pyaudio/docs/
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)

def newPlay(file, data, canvas):
    dataList = weirdPlay(file, data, canvas)
    p = pyaudio.PyAudio()
    
    wf = wave.open(file, 'rb')

    # stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
    #                 channels=wf.getnchannels(),
    #                 rate=wf.getframerate(),
    #                 output=True)
    count = 0
    for audioData in dataList:
        data.lineX += 1
        time.sleep(.1)


    # stream.stop_stream()
    # stream.close()