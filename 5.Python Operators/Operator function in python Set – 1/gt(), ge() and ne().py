# Python code to demonstrate working of
# gt(), ge() and ne()

# importing operator module
import operator

# Initializing variables
a = 4

b = 3

# using gt() to check if a is greater than b
if (operator.gt(a,b)):
	print ("4 is greater than 3")
else : print ("4 is not greater than 3")

# using ge() to check if a is greater than or equal to b
if (operator.ge(a,b)):
	print ("4 is greater than or equal to 3")
else : print ("4 is not greater than or equal to 3")

# using ne() to check if a is not equal to b
if (operator.ne(a,b)):
	print ("4 is not equal to 3")
else : print ("4 is equal to 3")
