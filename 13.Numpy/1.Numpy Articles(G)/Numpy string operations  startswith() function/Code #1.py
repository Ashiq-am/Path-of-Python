# Python program explaining
# numpy.char.startswith() function

# importing numpy as geek
import numpy as geek

arr = "GeeksforGeeks - A computer science portal"
prefix = 'Geeks'

gfg = geek.char.startswith(arr, prefix, start=0, end=None)

print(gfg)
