''' czNXdTNuYzM Possible Steps:
1) Flash challenge to arduino
2) Play high pitch audio to "harmonize" with challenge
3) Record video of LED screen
4) Automate grabbing numbers from video or manually write down numbers in txt file
5) Put number characters in python data structure
6) Predict next number in sequence using https://oeis.org/
	- maybe web query?
7) Write flag to Serial Monitor
'''

# Gets each digit series(w/o "." or "_")inside of phrase and puts it in a list
def get_data(filename):
	lines = []
	with open(filename, 'r', encoding='UTF-8') as file:
		while line := file.readline():
			lines.append(line.rstrip()[:-1].replace("_",""))
	return lines

def main():
	print ("\n")
	digits = get_data("csaw-embedded-security-challenge/czNxdTNuYzM/digits.txt")
		
	

if __name__ == '__main__':
	main()