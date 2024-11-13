# Creating a dictionary of lists
# using list comprehension
d = dict((val, range(int(val), int(val) + 2))
				for val in ['1', '2', '3'])

print(d)
