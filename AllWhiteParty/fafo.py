import serial
import itertools
import string
import time

def generate_combinations(length=5):
    letters = string.ascii_letters #+ string.digits
    one = letters
    two = letters[0]
    three = letters[0]
    four = letters[7:8]
    five = ['A']
    # find highest voltage using signal pin and ground on haptic feedback
        # then add a letter and repeat until username is found
    output = itertools.product(one)
    # output = itertools.product(one, two, letters, four, five)
    # output = itertools.product(letters, repeat=2)
    return output

def generate_experiment():
    #return ['hollywood', 'AllWhiteParty', 'Margot Robie', 'Beyonce']
    return ['glamour']
    #return string.ascii_uppercase[:10]
    #return ['A', 'BAA', 'A', 'BCC', 'g']
    #return string.digits# + string.ascii_uppercase + string.ascii_lowercase
    #return ['g', 'BAB', 'g', 'BBA', 'g', 'BCB', 'g', 'BDB', 'g', 'BBB', 'g'] # all of these resulted in 7.7s
    #return ['g', 'BAA', 'g', 'ABB', 'g'] # BAA was special. ABB was not.
    #return ['BB', 'BB', 'BB', 'BB']
    #return ['AB', 'AB', 'AB', 'AB']
    #return ['C', 'D', 'A', 'B']
    #return ['D', 'B', 'D', 'B', 'D', 'B']
    #return ['AB', 'BB', 'CB', 'DD']
    #return ['ABA', 'ABB', 'ABC', 'ABD']
    #return ['A', 'BA', 'BB', 'BC', 'BD', 'BA']
    #return ['a', 'AB', 'a', 'BB', 'a', 'CB', 'a']
    #return ['A'] * 7
    #return ['A', 'AB', 'AC', 'AD']# 'BD', 'BA']
    #return ['B'] * 7
    #return ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']
    #return ['andreas', 'akellas', 'user', 'l', 'password']
    #return ['s', 't', 'u', 'v', 'w']
    #return ['a'] * 27
    #return ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    #return ['*', '#', 'abcd', 'bcda', 'cdab', 'dabc']
    #return ['aaaaa', 'aaaaaaaaaa', 'a' * 15, 'a' * 20]

    # 'BB{digit}: not special
    #return ['g', 'BAB', 'g', 'BBA', 'g', 'BCB', 'g', 'BDB', 'g', 'BBB', 'g'] # all of these resulted in 7.7s
    #return ['g', 'BAA', 'g', 'ABB', 'g'] # BAA was special. ABB was not.
    #return ['g', 'BBg', 'g'] # BBg is special
    #return ['g', 'BgB', 'g'] # BgB is special
    #Ba is special

def main():

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


    #for combo in generate_combinations():
    for msg in generate_experiment():
        prefix = ''
        data = prefix + msg
        print("Current test: ", data)
        #data = ''.join(combo)

        ser.write(data.encode('utf-8'))
        start = time.time()

        time.sleep(5)

        response = ser.readline().decode('utf-8').strip()
        end = time.time()

        if response:
            print(f"Received: {response} - time: {end - start}")


    ser.close()

if __name__ == '__main__':
    main()
