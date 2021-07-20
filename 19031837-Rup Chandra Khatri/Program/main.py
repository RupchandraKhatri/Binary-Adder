from forInput import *
from conversion import *
from adder import *

while True:
	x = input("Enter d for decimal number and b for binary number : ")

	if x == "d":
		num_1, num_2 = forDecimal()
		bin_1 = decToBin(num_1)
		bin_2 = decToBin(num_2)
		output = binaryAdder(bin_1, bin_2)
		
	elif x == "b":
		str_1, str_2 = forBinary()
		bin_1 = stringToList(str_1)
		bin_2 = stringToList(str_2)
		output = binaryAdder(bin_1,bin_2)

		num_1 = binaryToDecimal(bin_1)
		num_2 = binaryToDecimal(bin_2)
		
	elif x == "" or x == " " :
		print("please fill the field.")
		print("please fill the field properly.")
		continue

	else:
		print("please give valid input")
		print(" Please fill the field with valid input.\n")
		continue

	print("")
	print("  1st binary value  :  ", listToStr(bin_1), "   |  1st decimal value  :  ", num_1)
	print("  2nd binary value :  ", listToStr(bin_2), "   |  2nd decimal value :  ", num_2)
	print("         ")
	print(" Sum in binary  :  ", listToStr(output), "   | Sum in integer  :  ", (num_1 + num_2))

	print("\nDo you want to continue or exit the program?")
	while True:
		print("  Enter 'C' to continue and 'E' to exit the program.")
		y = input("Enter: ")
		if y == "C" or y == "E":
			break
		elif y == " " or y == "" :
			print("\nError!")
			print("Please fill the field with valid input.")
			continue
		else:
			print("\nError!")
			print("Please enter the valid input.")
			continue
	if  y == "C":
		continue
	else:
		break
		



