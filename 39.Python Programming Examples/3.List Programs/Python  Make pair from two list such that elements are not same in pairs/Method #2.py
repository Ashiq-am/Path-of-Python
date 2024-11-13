# Python code to create pair of element
# from two list such that element
# in pairs are not equal.

# Importing
import itertools

# List initialization
list1 =[11, 22, 33, 44]
list2 =[22, 44, 66]

# using itertools
temp = list(itertools.product(list1, list1))

# output list initialization
out = []

# iteration
for elem in temp:
	if elem[0]!= elem[1]:
		out.append(elem)

# printing output
print(out)
