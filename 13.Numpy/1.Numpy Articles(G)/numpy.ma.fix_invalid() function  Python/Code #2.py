# Python program explaining
# numpy.ma.fix_invalid() function

# importing numpy as geek
import numpy as geek

arr = geek.ma.array([1., -1, geek.nan,
					geek.inf, -1, geek.nan],
						mask =[1] + [0]*5)

gfg = geek.ma.fix_invalid(arr)

print (gfg)
