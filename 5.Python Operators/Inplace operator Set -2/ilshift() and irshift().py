# Python code to demonstrate the working of
# ilshift() and irshift()

# importing operator to handle operator operations
import operator

# using ilshift() to bitwise left shift and assign value
x = operator.ilshift(8,2);

# printing the modified value
print ("The value after bitwise left shift and assigning : ",end="")
print (x)

# using irshift() to bitwise right shift and assign value
x = operator.irshift(8,2);

# printing the modified value
print ("The value after bitwise right shift and assigning : ",end="")
print (x)
