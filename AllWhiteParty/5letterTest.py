import serial
import itertools
import string
import time

def generate_combinations(length=5):
    letters = string.ascii_letters #+ string.digits
    four = letters[7:8]
    # AF_upper = ['A','B','C','D','E','F']
    five = ['A']
    output = itertools.product(letters, letters, letters,four,five)
    # output = itertools.combinations_with_replacement(AF_upper,5)

    # output = itertools.product(letters, repeat=length)
    return output

def main():

    # LINUX:
    # ser = serial.Serial('/dev/ttyUSB0', baudrate=115200 , timeout=1)

    # Windows
    with serial.Serial() as ser:
        ser.baudrate=115200 
        ser.port='COM5'
        ser.timeout=1
    
    ser.open()

    ## get beginning lines
    time.sleep(2)
    response = ser.readline().decode('utf-8')
    while response:
        print(f"{response}")
        response = ser.readline().decode('utf-8')


    for combo in generate_combinations():
        print("Current test: ", combo)
        data = ''.join(combo)

        ser.write(data.encode('utf-8'))

        time.sleep(5)

        response = ser.readline().decode('utf-8').strip()
        if response:
            print(f"Received: {response}")

    ser.close()

if __name__ == '__main__':
    main()