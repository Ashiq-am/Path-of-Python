# Python program to remove given element from the list
list1 = [1, 9, 8, 4, 9, 2, 9]

# Printing initial list
print("original list : " + str(list1))

# using discard() method to remove list element 9
list1 = set(list1)
list1.discard(9)

list1 = list(list1)

# Printing list after removal
print("List after element removal is : " + str(list1))
