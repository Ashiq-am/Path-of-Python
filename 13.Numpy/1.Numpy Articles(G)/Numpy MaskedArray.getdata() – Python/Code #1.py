# Python program explaining
# numpy.ma.getdata() function

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

arr = ma.masked_equal([[2, 4], [6, 8]], 4)
print("Input array : ", arr)

# applying numpy.ma.getdata() method
gfg = ma.getdata(arr)
print("Output array : ", gfg)
