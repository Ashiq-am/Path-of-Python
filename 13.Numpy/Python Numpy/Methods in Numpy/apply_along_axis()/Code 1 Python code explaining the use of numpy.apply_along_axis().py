# Python Program illustarting
# apply_along_axis() in NumPy

import numpy as geek


# 1D_func is "geek_fun"
def geek_fun(a):
    # Returning the sum of elements at start index and at last index
    # inout array
    return (a[0] + a[-1])


arr = geek.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

''' 
			-> [1,2,3] <- 1 + 7 
				[4,5,6]	 2 + 8 
			-> [7,8,9] <- 3 + 9 
'''
print("axis=0 : ", geek.apply_along_axis(geek_fun, 0, arr))
print("\n")

'''			 | | 
			[1,2,3] 1 + 3 
			[4,5,6] 4 + 6 
			[7,8,9] 7 + 9 
				^ ^			 
'''
print("axis=1 : ", geek.apply_along_axis(geek_fun, 1, arr))
