# Python program explaining
# mirr() function

import numpy as np
''' 
Question : 

	Investmnt = 500 
	Withdrawls at regular interval : 50, 31, 3, 11 
'''

Solution = np.mirr([-500, 50, 31, 3, 11], .34, .21)

print("Solution - Modified Internal Rate of Return : ", Solution)
