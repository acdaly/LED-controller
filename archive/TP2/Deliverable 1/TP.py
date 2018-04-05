#Ariana Daly + acdaly + B
#references pyaudio demo

import pyaudio
import wave
import audioop
import serial

#basic LED controlling code

def inputOnOff():
    #turn on/off an LED by entering 1 (on) or 0 (off)
    serial_ref = serial.Serial(port="/dev/cu.usbmodem1411", baudrate = 115200)
    while True:
        data = input("> ")
        dc
        serial_ref.write(bytearray(data, 'ascii'))

def blink():
    #make the LED blink
    serial_ref = serial.Serial(port="/dev/cu.usbmodem1411", baudrate = 115200)
    data = "0"
    delay = 10 * (10**6)
    count = 0
    while True:
        if count % delay == 0:
            if data == "1": data = "0" #off
            else: data = "1" #on
            print(data, count)
            serial_ref.write(bytearray(data, 'ascii'))
        count +=1

def fade():
    pass


def getRMS(file):
    #print RMS of every frame (power of the audio, measure of volume)
    wav = wave.open(file) #open file

    frames = wav.getnframes()
    width = wav.getsampwidth()
    for frame in range(frames):
        print(audioop.rms(wav.readframes(frame), width))

def play(file):
    #exmaple code - https://people.csail.mit.edu/hubert/pyaudio/docs/
    CHUNK = 1024

    wf = wave.open(file, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)
    count = 0
    while data != "":
        lastData = data
        stream.write(data)
        data = wf.readframes(CHUNK)
        if data == lastData: count +=1
        if count > 5: break

    stream.stop_stream()
    stream.close()
    p.terminate()

#play("cello.wav")
#getRMS("cello.wav")

def getMaxRMS(file):
    wav = wave.open(file) #open file
    frames = wav.getnframes()

    width = wav.getsampwidth()
    maxRMS = 0
    for frame in range(frames):
        currentRMS = audioop.rms(wav.readframes(frame), width)
        if currentRMS > maxRMS: 
            maxRMS = currentRMS
    return maxRMS

def sendBrightness(file):
    wav = wave.open(file) #open file
    width = wav.getsampwidth()

    maxRMS = getMaxRMS(file)
    maxBrightness = 255
    rmsToBrightness = maxBrightness/maxRMS

    frames = wav.getnframes()
    for frame in range(frames):
        data = audioop.rms(wav.readframes(frame), width) #RMS
        data = data * rmsToBrightness #brightness
        assert(data < maxBrightness)
        serial_ref.write(bytearray(int(data), 'ascii')) 

def sendBrightnessWithStream(file):
    seconds = 4
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

    maxRMS = getMaxRMS(file)
    maxBrightness = 255
    rmsToBrightness = maxBrightness/maxRMS

    for i in range(0, int(rate / chunk * seconds)):
        data = stream.read(chunk)
        rms = audioop.rms(data, 2)
        print(rms)

    frames = wav.getnframes()

    stream.stop_stream()
    stream.close()

    p.terminate()

inputOnOff()


