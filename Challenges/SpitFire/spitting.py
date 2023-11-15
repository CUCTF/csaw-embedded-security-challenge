import serial
import string
import time

def generate_message():
	chars = ["FLAG", "END"]
	hexed = []
	for i in chars:
		hexed.append( i.encode("utf-8").hex() )

	return (hexed)

def confirmSound(serVar):
	userConfirm = input("Confirm when arduino is done clickig (y)\t")
	if (userConfirm == "y"):
		response = serVar.readline().decode('utf-8')
		while response:
			print(f"{response}")
			response = serVar.readline().decode('utf-8')
	else:
		response = serVar.readline().decode('utf-8')
		while response:
			print(f"{response}")
			response = serVar.readline().decode('utf-8')
def main():

	## LINUX:
	# ser = serial.Serial('/dev/ttyUSB0', baudrate=115200 , timeout=1)

	## Windows
	with serial.Serial() as ser:
	    ser.baudrate=115200
	    ser.port='COM10'
	    ser.timeout=1

	ser.open()

	# ## get beginning lines
	time.sleep(2)
	response = ser.readline().decode('utf-8')
	while response:
	    print(f"{response}")
	    response = ser.readline().decode('utf-8')

	confirmSound(ser)
	
	for msg in generate_message():
		print("Current test: ", msg)

		ser.write(bytes(msg,"utf-8"))

		time.sleep(2)

		confirmSound(ser)

	ser.close()



if __name__ == '__main__':
	main()