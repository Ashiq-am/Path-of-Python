# Python3 program to illustrate
# working of Not gate

def NOT(a):
	if(a == 0):
		return 1
	elif(a == 1):
		return 0
# Driver code
if __name__=='__main__':
	print(NOT(0))

	print("+---------------+----------------+")
	print(" | NOT Truth Table | Result |")
	print(" A = False | A NOT =",NOT(False)," | ")
	print(" A = True, | A NOT =",NOT(True)," | ")

