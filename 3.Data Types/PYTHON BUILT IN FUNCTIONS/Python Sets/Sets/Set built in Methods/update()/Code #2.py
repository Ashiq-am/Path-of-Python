# Python program to demonstrate the
# use of update() method

list1 = [1, 2, 3, 4]
list2 = [1, 4, 2, 3, 5]
alphabet_set = {'a', 'b', 'c'}

# lists converted to sets
set1 = set(list2)
set2 = set(list1)

# Update method
set1.update(set2)

# Print the updated set
print(set1)

set1.update(alphabet_set)
print(set1)
