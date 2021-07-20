def decToBin(decimal):
	list_1 = [0,0,0,0,0,0,0,0]
	i = 7
	while decimal > 0:
		rem = decimal % 2
		list_1[i] = rem
		decimal = int(decimal / 2)
		i = i - 1
	return list_1

def listToStr(list_1):
	binary = ""
	for b in range(8):
		binary = binary + str(list_1[b])
	return binary

def stringToList(num):
	bin1 = [0,0,0,0,0,0,0,0]
	n = 7
	for i in range(len(num)-1, -1, -1):
		bin1[n] = int(num[i])
		n = n - 1
	return bin1

def binaryToDecimal(binary):
	count = 0
	i = 7
	decimal = 0
	while i >= 0:
		decimal = decimal + ( binary[i] * (2**count))
		count = count + 1
		i = i - 1
	return decimal







