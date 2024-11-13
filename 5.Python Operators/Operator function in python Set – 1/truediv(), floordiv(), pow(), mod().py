# Python code to demonstrate working of
# truediv(), floordiv(), pow(), mod()

# importing operator module
import operator

# Initializing variables
a = 5

b = 2

# using truediv() to divide two numbers
print ("The true division of numbers is : ",end="");
print (operator.truediv(a,b))

# using floordiv() to divide two numbers
print ("The floor division of numbers is : ",end="");
print (operator.floordiv(a,b))

# using pow() to exponentiate two numbers
print ("The exponentiation of numbers is : ",end="");
print (operator.pow(a,b))

# using mod() to take modulus of two numbers
print ("The modulus of numbers is : ",end="");
print (operator.mod(a,b))
