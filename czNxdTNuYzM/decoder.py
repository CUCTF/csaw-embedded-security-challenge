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
	return (str (res))

def writeOut(data, filename):
	f = open(filename, "w")
	for x in data:	
		f.write(x)
	f.close()

def main():
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

	res = ascii_sum(b32digits)
	print(f"Position Summation (B32): {res}\n")

	res = ascii_sum(b64digits)
	print(f"Position Summation (B64): {res}\n")

	# writeOut(b64digits, "csaw-embedded-security-challenge/czNxdTNuYzM/base64_translated.txt")
	

if __name__ == '__main__':
	main()