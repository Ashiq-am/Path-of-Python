# Python3 program to illustrate
# working of Not gate

def XNOR(a,b):
	if(a == b):
		return 1
	else:
		return 0
# Driver code
if __name__=='__main__':
	print(XNOR(1,1))

	print("+---------------+----------------+")
	print(" | XNOR Truth Table | Result |")
	print(" A = False, B = False | A AND B =",XNOR(False,False)," | ")
	print(" A = False, B = True | A AND B =",XNOR(False,True)," | ")
	print(" A = True, B = False | A AND B =",XNOR(True,False)," | ")
	print(" A = True, B = True | A AND B =",XNOR(True,True)," | ")
