# Python program explaining
# numpy.ndarray.fill() function
import numpy as geek

a = geek.empty([3, 3])

# Initializing each element of the array
# with 1 by using nested loops
for i in range(3):
    for j in range(3):
        a[i][j] = 1

print("a is : \n", a)

# now we are initializing each element
# of the array with 1 using fill() function.
a.fill(1)

print("\nAfter using fill() a is : \n", a)

