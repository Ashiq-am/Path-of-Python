# Python code to demonstrate the working of
# ixor() and ipow()

# importing operator to handle operator operations
import operator

# using ixor() to exclusive or and assign value
x = operator.ixor(10,5);

# printing the modified value
print ("The value after xoring and assigning : ",end="")
print (x)

# using ipow() to exponentiate and assign value
x = operator.ipow(5,4);

# printing the modified value
print ("The value after exponentiating and assigning : ",end="")
print (x)
