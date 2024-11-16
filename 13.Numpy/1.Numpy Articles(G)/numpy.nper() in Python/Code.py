# Python program explaining
# pmt() function

import numpy as np

''' 
Question : 

how much time would it take to pay-off a loan of 
$10, 000 at 10 % annual rate of interest, if we had 
$100 to pay each month ? 
'''

# rate pmt pv
Solution = np.nper(0.1 / 12, -100, 10000)

# Here fv = 0 ; Also Default value of fv = 0
print("Solution - No. of periods : % f months" %(Solution))
