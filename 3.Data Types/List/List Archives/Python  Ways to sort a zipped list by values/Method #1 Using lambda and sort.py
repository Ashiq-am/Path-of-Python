# Python code to demonstrate
# sort zipped list by values
# using lambda and sorted

# Declaring initial lists
list1 = ['geeks', 'for', 'Geeks']
list2 = [3, 2, 1]
zipped = zip(list1, list2)

# Converting to list
zipped = list(zipped)

# Printing zipped list
print("Initial zipped list - ", str(zipped))

# Using sorted and lambda
res = sorted(zipped, key=lambda x: x[1])

# printing result
print("final list - ", str(res))
