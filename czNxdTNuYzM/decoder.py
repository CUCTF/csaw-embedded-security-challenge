import base64
from binascii import b2a_base64
import os

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
		temp = hex(int(i))
		if (len(temp)%2 == 0):
			temp = temp.replace("0x","")
		else:
			temp = temp.replace("0x","0")
		hexed.append (bytes.fromhex(temp))
	return hexed
	
def generateB64(toB64):
	b64digits = []
	for i in toB64:
		b64digits.append ( b2a_base64(i).decode())
	return b64digits

def generateB32(toB32):
	b32digits = []
	for i in toB32:
		b32digits.append(base64.b32encode(bytearray(i, 'ascii')).decode('utf-8'))
	return b32digits

def writeOut(data, filename):
	f = open(filename, "w")
	for x in data:	
		f.write(x)
	f.close()

def main():
	digits = get_data("csaw-embedded-security-challenge/czNxdTNuYzM/digits.txt")
	print(f"Original: {digits}\n")
	hexed = generate_hex(digits)
	print(f"Hex: {hexed}\n")

	b64digits = generateB64(hexed)
	print(f"Hex to B64: {b64digits}\n")

	b32digits = generateB32(b64digits)
	print(f"B64 to B32: {b32digits}\n")


	# writeOut(b64digits, "csaw-embedded-security-challenge/czNxdTNuYzM/base64_translated.txt")
	

if __name__ == '__main__':
	main()