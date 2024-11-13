# initializing lists
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

# Using list comprehension with zip to create a list of pairs
pairs = [(elem1, elem2) for elem1, elem2 in zip(list1, list2)]

# Displaying the pairs
print(pairs)
