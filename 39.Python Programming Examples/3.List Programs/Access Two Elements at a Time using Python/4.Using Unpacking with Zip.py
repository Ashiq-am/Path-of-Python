# initializing Lists
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

# Unpacking pairs using zip and asterisk
for pair in zip(list1, list2):
	elem1, elem2 = pair
	print(elem1, elem2)
