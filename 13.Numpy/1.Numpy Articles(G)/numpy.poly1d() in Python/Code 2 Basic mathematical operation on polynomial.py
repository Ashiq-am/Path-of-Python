# Python code explaining
# numpy.poly1d()

# importing libraries
import numpy as np

# Constructing polynomial
p1 = np.poly1d([1, 2])
p2 = np.poly1d([4, 9, 5, 4])

print ("P1 : ", p1)
print ("\n p2 : \n", p2)

print ("\n\np1 ^ 2 : \n", p1**2)
print ("p2 ^ 2 : \n", np.square(p2))

p3 = np.poly1d([1, 2], variable = 'y')
print ("\n\np3 : ", p3)


print ("\n\np1 * p2 : \n", p1 * p2)
print ("\nMultiplying two polynimials : \n", np.poly1d([1, -1]) * np.poly1d([1, -2]))
