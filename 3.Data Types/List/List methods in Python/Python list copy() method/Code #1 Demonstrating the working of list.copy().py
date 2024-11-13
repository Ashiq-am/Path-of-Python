# Python 3 code to demonstrate
# working of list.copy()

# Initializing list
lis1 = [ 1, 2, 3, 4 ]

# Using copy() to create a shallow copy
lis2 = lis1.copy()

# Printing new list
print ("The new list created is : " + str(lis2))

# Adding new element to new list
lis2.append(5)

# Printing lists after adding new element
# No change in old list
print ("The new list after adding new element : " + str(lis2))
print ("The old list after adding new element to new list : " + str(lis1))
