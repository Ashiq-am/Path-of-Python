# Python code explaining
# numpy.polysub ()

# importing libraries
import numpy as np

p1 = np.poly1d([1, 2])
p2 = np.poly1d([9, 5, 4])

print ("P1 : ", p1)
print ("\nP2 : \n", p2)

a = np.polysub(p1, p2)

print ("\nP1 - P2 : \n", a)
