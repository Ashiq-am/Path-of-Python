# Python program explaining
# ipmt() function

import numpy as np
''' 
Question : 

monthly payment needed to pay off a $10, 000 loan 
in 12 years at an annual interest rate of 60 % 
'''

Solution = np.ipmt(0.6 / 12, 2 * 12, 1 * 12, 10000)

# Here fv = 0 ; Also Default value of fv = 0
print("Solution - ipmt value : ", Solution)
