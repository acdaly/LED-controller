import serial


def blink():
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

