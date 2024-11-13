# Python code to demonstrate the working of
# logical_and(), logical_or(), logical_xor()
# and logical_invert()

# importing "decimal" module to use decimal functions
import decimal

# Initializing decimal number
a = decimal.Decimal(1000)

# Initializing decimal number
b = decimal.Decimal(1110)

# printing logical_and of two numbers
print ("The logical_and() of two numbers is : ",end="")
print (a.logical_and(b))

# printing logical_or of two numbers
print ("The logical_or() of two numbers is : ",end="")
print (a.logical_or(b))

# printing exclusive or of two numbers
print ("The exclusive or of two numbers is : ",end="")
print (a.logical_xor(b))

# printing logical inversion of number
print ("The logical inversion of number is : ",end="")
print (a.logical_invert())
