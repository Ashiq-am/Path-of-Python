# Python3 program to illustrate
# working of NOR gate

def NOR(a, b):
	if(a == 0) and (b == 0):
		return 1
	elif(a == 0) and (b == 1):
		return 0
	elif(a == 1) and (b == 0):
		return 0
	elif(a == 1) and (b == 1):
		return 0

# Driver code
if __name__=='__main__':
	print(NOR(0, 0))

	print("+---------------+----------------+")
	print(" | NOR Truth Table | Result |")
	print(" A = False, B = False | A AND B =",NOR(False,False)," | ")
	print(" A = False, B = True | A AND B =",NOR(False,True)," | ")
	print(" A = True, B = False | A AND B =",NOR(True,False)," | ")
	print(" A = True, B = True | A AND B =",NOR(True,True)," | ")
