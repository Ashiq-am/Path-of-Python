# Python program to demonstrate the use of
# of symmetric_difference() method


list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [3, 4, 5]

# Convert list to sets
set1 = set(list1)
set2 = set(list2)

# Prints the symmetric difference when
# set is passed as a parameter
print(set1.symmetric_difference(set2))

# Prints the symmetric difference when list is
# passed as a parameter by converting it to a set
print(set2.symmetric_difference(list3))
