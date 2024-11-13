# Python 3 code to demonstrate
# techniques of deep and shallow copy
import copy

# Initializing list
lis1 = [ 1, 2, 3, 4 ]

# Using shallow copy techniques to create a shallow copy
lis2 = lis1.copy()
lis3 = copy.copy(lis1)
lis4 = lis1[:]

# Adding new element to new lists
lis2.append(5)
lis3.append(5)
lis4.append(5)

# Printing lists after adding new element
# No change in old list
print ("The new list created using copy.copy() : " + str(lis2))
print ("The new list created using list.copy() : " + str(lis3))
print ("The new list created using slicing : " + str(lis4))
print ("The old list after adding new element to new list : " + str(lis1))

print ("\n")

# Using deep copy techniques to create a deep copy
lis2 = lis1
lis3 = copy.deepcopy(lis1)

# Adding new element to new lists
lis2.append(5)
lis3.append(5)


# Printing lists after adding new element
# changes reflected in old list
print ("The new list created using copy.deepcopy() : " + str(lis2))
print ("The new list created using = : " + str(lis3))
print ("The old list after adding new element to new list : " + str(lis1))
