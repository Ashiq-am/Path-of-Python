# Python code to demonstrate the working of
# min() and max()

# importing "decimal" module to use decimal functions
import decimal

# Initializing decimal number
a = decimal.Decimal(9.53)

# Initializing decimal number
b = decimal.Decimal(7.43)

# printing minimum of both values
print ("The minimum of two numbers is : ",end="")
print (a.min(b))

# printing maximum of both values
print ("The maximum of two numbers is : ",end="")
print (a.max(b))
