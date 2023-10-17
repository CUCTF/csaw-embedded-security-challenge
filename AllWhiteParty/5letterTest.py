import serial
import itertools
import string
import time

def generate_combinations(length=5):
    letters = string.ascii_letters + string.digits
    return itertools.product(letters, repeat=length)

def main():
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

    time.sleep(2)

    for combo in generate_combinations():
        print("Current test: ", combo)
        data = ''.join(combo)

        ser.write(data.encode('utf-8'))

        time.sleep(0.1)

        response = ser.readline().decode('utf-8').strip()
        if response:
            print(f"Received: {response}")

    ser.close()

if __name__ == '__main__':
    main()