import codecs
import os

# Gets each digit series(w/o "." or "_")inside of phrase and puts it in a list
def get_data(filename):
	lines = []
	with open(filename, 'r', encoding='UTF-8') as file:
		while line := file.readline():
			lines.append(line.rstrip()[:-1].replace("_",""))
	return lines


digits = get_data("csaw-embedded-security-challenge/czNxdTNuYzM/digits.txt")
# print (digits)

# print (os.getcwd())
# decode_hex = codecs.getdecoder("hex_codec")

# # for an array
# msgs = [decode_hex(msg)[0] for msg in msgs]

# # for a string
# string = decode_hex(string)[0]