# Python code to demonstrate the working of
# isub() and imul()

# importing operator to handle operator operations
import operator

# using isub() to subtract and assign value
x = operator.isub(2, 3);

# printing the modified value
print ("The value after subtracting and assigning : ", end="")
print (x)

# using imul() to multiply and assign value
x = operator.imul(2, 3);

# printing the modified value
print ("The value after multiplying and assigning : ", end="")
print (x)
