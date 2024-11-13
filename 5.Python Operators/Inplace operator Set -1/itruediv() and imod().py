# Python code to demonstrate the working of
# itruediv() and imod()

# importing operator to handle operator operations
import operator

# using itruediv() to divide and assign value
x = operator.itruediv(10, 5)

# printing the modified value
print ("The value after dividing and assigning : ", end="")
print (x)

# using imod() to modulus and assign value
x = operator.imod(10, 6)

# printing the modified value
print ("The value after modulus and assigning : ", end="")
print (x)
