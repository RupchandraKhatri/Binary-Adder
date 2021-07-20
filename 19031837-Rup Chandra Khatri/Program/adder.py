from gates import *

def binaryAdder(f_1, f_2):
	binary = [0,0,0,0,0,0,0,0]
	i = 7
	carry = 0
	while i >= 0:
		num_1 = f_1[i]
		num_2 = f_2[i]

		sum_1 = xorGate(xorGate(num_1,num_2),carry)
		binary[i] = sum_1

		bit_1 = andGate(xorGate(num_1,num_2),carry)
		bit_2 = andGate(num_1,num_2)
		carry = orGate(bit_1,bit_2)

		i = i-1

	return binary
