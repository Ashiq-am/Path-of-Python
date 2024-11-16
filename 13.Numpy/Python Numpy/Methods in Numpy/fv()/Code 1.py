# Python program explaining fv() function

import numpy as np
''' 
Question : 

Future value after 10 years of saving $100 now, 
with an additional monthly savings of $100. 
Assume the interest rate is 5% (annually) 
compounded monthly ? 
'''

#				 rate	 np	 pmt pv
Solution = np.fv(0.05/12, 10*12, -100, -100)

print("Solution : ", Solution)
