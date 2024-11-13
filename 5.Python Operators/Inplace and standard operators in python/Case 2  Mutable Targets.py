# Python code to demonstrate difference between
# Inplace and Normal operators in mutable Targets

# importing operator to handle operator operations
import operator

# Initializing list
a = [1, 2, 4, 5]

# using add() to add the arguments passed
z = operator.add(a,[1, 2, 3])

# printing the modified value
print ("Value after adding using normal operator : ",end="")
print (z)

# printing value of first argument
# value is unchanged
print ("Value of first argument using normal operator : ",end="")
print (a)

# using iadd() to add the arguments passed
# performs a+=[1, 2, 3]
p = operator.iadd(a,[1, 2, 3])

# printing the modified value
print ("Value after adding using Inplace operator : ",end="")
print (p)

# printing value of first argument
# value is changed
print ("Value of first argument using Inplace operator : ",end="")
print (a)
