# Python 3 code to
# remove an item from list
# using function pop()

lst = ['Iris', 'Orchids', 'Rose', 'Lavender',
	'Lily', 'Carnations']
print("Original List is :", lst)

# using pop()
# to delete item ('Orchids' at index 1)
# from the list
a = lst.pop(1)
print("Item popped :", a)
print("After deleting the item :", lst)
