# Python program explaining
# ppmt() function

import numpy as np

''' 
Question : 

monthly payment needed to pay off a $10, 000 loan 
in 12 years at an annual interest rate of 10 % 
'''

# rate	 np		 pv
Solution = np.ppmt(0.10 / 12, 12 * 12, 10, 000)

# Here fv = 0 ; Also Default value of fv = 0
print("Solution : ", Solution)
