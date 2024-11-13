# Python code to demonstrate the working of
# ior() and iand()

# importing operator to handle operator operations
import operator

# using ior() to or, and assign value
x = operator.ior(10,5);

# printing the modified value
print ("The value after bitwise or, and assigning : ",end="")
print (x)

# using iand() to and, and assign value
x = operator.iand(5,4);

# printing the modified value
print ("The value after bitwise and, and assigning : ",end="")
print (x)
