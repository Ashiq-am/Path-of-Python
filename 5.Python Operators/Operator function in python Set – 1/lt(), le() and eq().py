# Python code to demonstrate working of
# lt(), le() and eq()

# importing operator module
import operator

# Initializing variables
a = 3

b = 3

# using lt() to check if a is less than b
if(operator.lt(a,b)):
	print ("3 is less than 3")
else : print ("3 is not less than 3")

# using le() to check if a is less than or equal to b
if(operator.le(a,b)):
	print ("3 is less than or equal to 3")
else : print ("3 is not less than or equal to 3")

# using eq() to check if a is equal to b
if (operator.eq(a,b)):
	print ("3 is equal to 3")
else : print ("3 is not equal to 3")
