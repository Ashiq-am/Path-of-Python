# Python program to remove given element from the list
list1 = [1, 9, 8, 4, 9, 2, 9]

# Printing initial list
print("original list : " + str(list1))

# using List Comprehension
# to remove list element 9
list1 = [ele for ele in list1 if ele != 9]

# Printing list after removal
print("List after element removal is : " + str(list1))
