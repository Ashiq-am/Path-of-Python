# Python3 code to demonstrate
# clearing a list using
# del method

# Initializing lists
list1 = [1, 2, 3]
list2 = [5, 6, 7]

# Printing list1 before deleting
print ("List1 before deleting is : " + str(list1))

# deleting list1 using del
del list1[:]
print ("List1 after clearing using del : " + str(list1))


# Printing list2 before deleting
print ("List2 before deleting is : " + str(list2))

# deleting list using del
del list2[:]
print ("List2 after clearing using del : " + str(list2))
