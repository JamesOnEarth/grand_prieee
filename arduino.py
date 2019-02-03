import serial

def main():
	string = ""
	string2 = ""
	result = ""
	list = [None] * 128
	
	ser = serial.Serial('/dev/cu.usbmodem14201',9600)
	for i in range(128):
		list[i] = int( ser.readline().strip('\n').strip('\r') )
		string = string + ' ' + str(list[i])
	print string + '\n'
	list = median(list)
	for i in list:
		string2 = string2 + ' ' + str(i)
	print string2 + '\n'
	list = gradient(list)
	for i in list:
		result = result + ' ' + str(i)
	print result

def median(list):
	temp = [None] * 128
	temp[0] = int( ( list[0] + list[1] ) / 2 )
	for i in range(1,127):
		numbers = [list[i-1],list[i],list[i+1]]
		numbers.sort()
		temp[i] = numbers[1]
	temp[127] = int( ( list[126] + list[127] ) / 2 )
	return temp

def gradient(list):
	temp = [None] * 128
	for i in range(0,127):
		temp[i] = list[i+1] - list[i]
	temp[127] = 0
	return temp

if __name__ == "__main__":
	main()
