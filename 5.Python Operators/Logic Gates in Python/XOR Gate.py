# Python3 program to illustrate
# working of Xor gate

def XOR (a, b):
	if a != b:
		return 1
	else:
		return 0

# Driver code
if __name__=='__main__':
	print(XOR(5, 5))

	print("+---------------+----------------+")
	print(" | XOR Truth Table | Result |")
	print(" A = False, B = False | A AND B =",XOR(False,False)," | ")
	print(" A = False, B = True | A AND B =",XOR(False,True)," | ")
	print(" A = True, B = False | A AND B =",XOR(True,False)," | ")
	print(" A = True, B = True | A AND B =",XOR(True,True)," | ")
