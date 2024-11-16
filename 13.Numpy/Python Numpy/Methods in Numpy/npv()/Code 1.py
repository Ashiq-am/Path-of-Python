## Python program explaining pv() function
import numpy as np

#		 rate		 values
a = np.npv(0.281,[-100, 19, 49, 58, 200])
print("Net Present Value(npv) : ", a)
