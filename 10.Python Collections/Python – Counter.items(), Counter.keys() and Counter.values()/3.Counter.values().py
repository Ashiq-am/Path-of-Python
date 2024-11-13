# importing the module
from collections import Counter

# making a list
list = [1, 1, 2, 3, 4, 5,
		6, 7, 9, 2, 3, 4, 8]

# instatiating a Counter object
ob = Counter(list)

# Counter.values()
values = ob.values()

print("The datatype is "
	+ str(type(values)))

# displaying the dict_items
print(values)

# iterating over the dict_items
for i in values:
	print(i)
