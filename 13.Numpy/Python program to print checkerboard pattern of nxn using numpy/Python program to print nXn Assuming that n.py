# Python program to print nXn Assuming that n
# is always even as a checkerboard was

import numpy as np
def printcheckboard(n):
	final = []
	for i in range(n):
		final.append(list(np.tile([0,1],int(n/2))) if i%2==0 else list(np.tile([1,0],int(n/2))))
	print(np.array(final))


# driver code
n = 8
printcheckboard(n)
