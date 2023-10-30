import base64
from binascii import b2a_base64
# import os
import math


# Gets each digit series(w/o "." or "_")inside of phrase and puts it in a list
def get_data(filename):
	lines = []
	with open(filename, 'r', encoding='UTF-8') as file:
		while line := file.readline():
			lines.append(line.rstrip()[:-1].replace("_",""))
	return lines

def generate_hex(toHex):
	hexed = []
	for i in toHex:
		b_length = (int(i).bit_length()+ 7) // 8
		bytes_val = int(i).to_bytes(b_length, 'big')
		hexed.append (bytes_val)
	return hexed
	
def generateB64(toB64):
	b64digits = []
	for i in toB64:
		b64digits.append ( b2a_base64(i).decode('utf-8'))
	return b64digits

def generateB32(toB32):
	b32digits = []
	for i in toB32:
		b32digits.append(base64.b32encode(bytearray(i, 'utf-8')).decode('utf-8'))
	return b32digits

def ascii_sum (str_list):
	res = []
	for sub in str_list:
		res.append(sum(map(ord, sub)))
	return (res)

def freq_to_note(freq):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    note_number = 12 * math.log2(freq / 440) + 49  
    note_number = round(note_number)
        
    note = (note_number - 1 ) % len(notes)
    note = notes[note]
    
    octave = (note_number + 8 ) // len(notes)
    
    return note, octave
''' 1
# https://oeis.org/search?q=1%2C++2%2C++6%2C++24%2C++120%2C++20%2C++140%2C++1120%2C[…]%2C++3879876%2C++176358%2C+4056234%2C&language=english&go=Search
# def algorithm (n):
# 	a(n+1) = a(n)/n if n|a(n) else a(n)*n, a(1) = 1.
'''

def writeOut(data, filename):
	f = open(filename, "w")
	for x in data:	
		f.write(x)
	f.close()

def main():
	print ("\n")
	digits = get_data("csaw-embedded-security-challenge/czNxdTNuYzM/digits.txt")
	print(f"Original: {digits}\n")
	
	my_bytes = generate_hex(digits)
	print(f"Bytes: {my_bytes}\n")

	hexed = []
	for x in range (len(my_bytes)):
		hexed.append(my_bytes[x].hex())
	print(f"Hex: {hexed}\n")


	b64digits = generateB64(my_bytes)
	print(f"Hex to B64: {b64digits}\n")

	b32digits = generateB32(b64digits)
	print(f"B64 to B32: {b32digits}\n")

	# res32 = ascii_sum(b32digits)
	# print(f"~~~~~~\nPosition Summation (B32): {res32}\n")

	# hertz32 = []
	# for i in res32:
	# 	hertz32.append(freq_to_note(i))
	# print(f"hertz (B32): {hertz32}\n")

	res64 = ascii_sum(b64digits)
	print(f"~~~~~~\n Position Summation (B64): {res64}\n")

	hertz64 = []
	for i in res64:
		hertz64.append(freq_to_note(i))
	print(f"hertz (B64): {hertz64}\n")

	

	# writeOut(b64digits, "csaw-embedded-security-challenge/czNxdTNuYzM/base64_translated.txt")
	

if __name__ == '__main__':
	main()