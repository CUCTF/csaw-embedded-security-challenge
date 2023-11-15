import serial
import itertools
import string
import time

def generate_combinations(length=1):
    #letters = string.ascii_uppercase + string.digits
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    #digits = string.digits
    return itertools.product(lowercase, repeat=length)
    # return ['Z', 'Y', 'X' ,'W', 'A', 'B', 'C', 'D']
    #return ['z', 'Barr', 'z', 'Barq', 'z']



def main():
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

    for i in range(6):
        ser.readline()

    for combo in generate_combinations():

        data = 'Barr' + ''.join(combo) 
        print("Current test: ", ''.join(data))
        # data = combo
        start = time.time()
        ser.write(data.encode('utf-8'))
        
        time.sleep(5)

        response = ser.readline().decode("utf-8")
        end = time.time() - start

        print("Test", data, "took", end, "seconds")
        # print("Hit enter to send the next input")
        # pressed = False

        if response:
            print(f"Received: {response}")

    ser.close()

if __name__ == '__main__':
   main()
