# Python Programming illustrating
# numpy.tril method

import numpy as geek

# string input
a = geek.matrix([[1, 21, 30],
				[63 ,434, 3],
				[54, 54, 56]])

print("Main Diagonal elements : \n", geek.tril(a), "\n")

print("Diagonal above main Diagonal elements : \n", geek.tril(a, 1), "\n\n")

print("Main Diagonal elements : \n", geek.tril(a, -1))
