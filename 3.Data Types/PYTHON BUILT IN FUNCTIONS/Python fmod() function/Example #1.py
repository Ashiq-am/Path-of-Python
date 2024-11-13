# Python3 program to demonstrate fmod() function

import math

# Tuple Declaration
Tup = (15, 22, -2, -40 )

# List Declaration
Lis = [-89, 38, -39, 16]

# modulus of +ve integer number
print(math.fmod(4, 5))
print(math.fmod(43.50, 4.5))

# modulus of -ve integer number
print(math.fmod(-17, 5))
print('%.2f' %math.fmod(-10, 4.78))

# modulus of tuple item
print("\nModulus of tuple items:")
print(math.fmod(Tup[2], 5))
print(math.fmod(Tup[2], -6))

# modulus of list item
print("\nModulus of list items:")
print(math.fmod(Lis[3], 4))
print(math.fmod(Lis[0], -15))
