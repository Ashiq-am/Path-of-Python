# Python3 program to illustrate
# working of OR gate

def OR(a, b):
	if a == 1:
		return True
	elif b == 1:
		return True
	else:
		return False

# Driver code
if __name__=='__main__':
	print(OR(0, 0))

	print("+---------------+----------------+")
	print(" | OR Truth Table | Result |")
	print(" A = False, B = False | A AND B =",OR(False,False)," | ")
	print(" A = False, B = True | A AND B =",OR(False,True)," | ")
	print(" A = True, B = False | A AND B =",OR(True,False)," | ")
	print(" A = True, B = True | A AND B =",OR(True,True)," | ")
