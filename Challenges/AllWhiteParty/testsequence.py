import serial
import itertools
import string
import time

MODE_UPPER='upper'
MODE_LOWER='lower'
MODE_DIGIT='digits'

def generate_sequence(mode=MODE_UPPER):
    if mode == MODE_UPPER:
        return string.ascii_uppercase
    elif mode == MODE_LOWER:
        return string.ascii_lowercase
    else:
        return string.digits

def search(prefix, mode=MODE_UPPER, period=5, padding="g"):

    # LINUX:
    ser = serial.Serial('/dev/ttyUSB0', baudrate=115200 , timeout=1)

    # Windows
    #with serial.Serial() as ser:
    #    ser.baudrate=115200
    #    ser.port='COM7'
    #    ser.timeout=1

    if (ser.isOpen() == False):
        ser.open()

    ## get beginning lines
    time.sleep(2)
    response = ser.readline().decode('utf-8')
    while response:
        print(f"{response}")
        response = ser.readline().decode('utf-8')


    for msg in generate_sequence(mode):

        print("Sending padding character: ", padding)
        start = time.time()
        ser.write(padding.encode('utf-8'))
        time.sleep(period)
        response = ser.readline().decode('utf-8').strip()
        end = time.time()
        if response:
            print(f"Received: {response} - time: {end - start}")

        data = prefix + msg
        print("Current test: ", data)

        start = time.time()
        ser.write(data.encode('utf-8'))
        time.sleep(period)
        response = ser.readline().decode('utf-8').strip()
        end = time.time()

        if response:
            print(f"Received: {response} - time: {end - start}")

    ser.close()

if __name__ == '__main__':
    search('', MODE_UPPER, period=5, padding='g')
