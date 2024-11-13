# Python code to demonstrate
# sort zipped list by values
# using operator and sorted

import operator

# Declaring initial lists
list1 = ['akshat', 'Manjeet', 'nikhil']
list2 = [3, 2, 1]
zipped = zip(list1, list2)

# Converting to list
zipped = list(zipped)

# Printing zipped list
print("Initial zipped list - ", str(zipped))

# Using sorted and operator
res = sorted(zipped, key=operator.itemgetter(1))

# printing result
print("final list - ", str(res))
