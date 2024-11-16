# Python code explaining
# numpy.polyint()

# importing libraries
import numpy as np

# Constructing polynomial
p1 = np.poly1d([1, 2])
p2 = np.poly1d([4, 9, 5, 4])

print("P1 : ", p1)
print("\n p2 : \n", p2)

# Solve for x = 2
print("\n\np1 at x = 2 : ", p1(2))
print("p2 at x = 2 : ", p2(2))

a = np.polyint(p1, 1)
b = np.polyint(p2, 1)
print("\n\nUsing polyint")
print("p1 anti-derivative of order = 1 : \n", a)
print("p2 anti-derivative of order = 1 : \n", b)

a = np.polyint(p1, 2)
b = np.polyint(p2, 2)
print("\n\nUsing polyint")
print("p1 anti-derivative of order = 2 : \n", a)
print("p2 anti-derivative of order = 2 : \n", b)
