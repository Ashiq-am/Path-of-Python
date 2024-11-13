# Python code explaining
# numpy.polyint()

# importing libraries
import numpy as np

# Constructing polynomial
p1 = np.poly1d([2, 6])
p2 = np.poly1d([4, 8])

a = np.polyint(p1, 1)
b = np.polyint(p2, 2)

print("\n\nUsing polyint")
print("p1 anti-derivative of order = 2 : \n", a)
print("p2 anti-derivative of order = 2 : \n", b)
