# Python program explaining
# irr() function

import numpy as np
''' 
Question : 

	Investmnt = 500 
	Withdrawls at regular interval : 50, 31, 3, 11 
'''

Solution = np.irr([-500, 50, 31, 3, 11])

print("Solution - Internal Rate of Return : ", Solution)
