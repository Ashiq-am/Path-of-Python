# Python code to demonstrate the working of
# iadd() and iconcat()

# importing operator to handle operator operations
import operator

# using iadd() to add and assign value
x = operator.iadd(2, 3);

# printing the modified value
print ("The value after adding and assigning : ", end="")
print (x)

# initializing values
y = "geeks"

z = "forgeeks"

# using iconcat() to concat the sequences
y = operator.iconcat(y, z)

# using iconcat() to concat sequences
print ("The string after concatenation is : ", end="")
print (y)
