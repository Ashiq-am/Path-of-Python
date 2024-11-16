# Python program explaining
# numpy.real_if_close() function

# importing numpy as geek
import numpy as geek

arr = [3.6 + 4e-14j]
tol = 1000

gfg = geek.real_if_close(arr, tol)

print(gfg)
