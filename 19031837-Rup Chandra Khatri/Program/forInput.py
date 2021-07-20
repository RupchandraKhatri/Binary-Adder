from conversion import * 

def forDecimal():
	print("\n Enter 1st decimal number.")
	print("Note: The number should lie between 0 and 256.")
	while True:
		while True:
			try:
				num_1 = int(input("\nEnter the first decimal number: "))
				if num_1 <= -1 or num_1 > 255:
					print("\nError!!!")
					print("\nThe number should lie between 0 and 256.")
					continue
				else:
					break
				break
			except ValueError:
				print("\nError!!!")
				print("Please enter the valid input.")
				continue
		while True:
			try:
				num_2 = int(input("\nEnter 2nd decimal number: "))
				if num_2 <= -1 or num_2 > 255 :
					print("\nError!!!")
					print("The number should lie between 0 and 256.")
					continue
				else:
					break
				break
			except ValueError:
				print("\nError!!!")
				print("Please enter the valid input.")
				continue

		total = num_1 + num_2

		if total > 255:
			print("\nError!!!")
			print("The sum of two numbers should be less than 256")
			continue
		else:
			break 
	return num_1, num_2


def forBinary():
	a = "\n Enter binary number."
	print(a)
	print("Note: The binary number should be maximum at 11111111 and minimum at 00000000")
	while True:
		while True:
			num_1 = input("\nEnter 1st binary number: ")
			count = 0
			num1 = 0
			size = len(num_1)
			if num_1 == "" or num_1 == " ":
				print("\nError!!!")
				print("please fill the field.")
				continue
			elif size > 8:
				print("\nError!!!")
				print("Entered binary number should be of 8 bits.")
				continue
			else:
				try:
					num1 = int(num_1)
					li =list(map(int,str(num1)))
					sets = set(li) 
					if sets == {0} or sets == {1} or sets == {0,1}:
						break
					else:			
						print("\nError!!!")
						print("Please make sure the input value must be 0-1")
						continue
				except ValueError:
					print("\nError!!!\nInvalid input")
					print("Entering alphabet, chatacter and negative value is disallowed.")
					continue

		while True: 
			num_2= input("\nEnter 2nd binary number: ")
			num2 = 0
			lenght = len(num_2)
			if num_2 == "" or num_2 == " ":
				print("\nError!!!")
				print("please fill the field.")
				continue
			elif lenght > 8:
				print("\nError!!!")
				print("Entered binary number must be of 8 bits")
				continue
			else:
				try:
					num2 = int(num_2)
					li = list(map(int,str(num2)))
					sets = set(li)
					if sets == {0} or sets == {1} or sets == {0,1}:
						break
					else:
						print("\nError!!!")
						print("Please make sure the input value must be 0-1")
						continue
				except ValueError:
					print("Please enter valid input")
					print("Alphabet, chatacter and negative value is not allowed.")
					continue
		a = stringToList(num_1)
		b = stringToList(num_2)

		x = binaryToDecimal(a)
		y = binaryToDecimal(b) 

		total = x + y
		if total > 255:
			print("Error!!!")
			print("The sum of two binary numbers is larger than a byte!!\n Please try again.")
			continue
		else:
			break

	return num_1, num_2
