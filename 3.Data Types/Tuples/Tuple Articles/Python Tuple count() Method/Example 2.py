# Creating tuples
Tuple = (0, 1, "GFG", (2, 3), (2, 3), 1,
		[3, 2], 'geeks', (0), ('G', 'F'))

# count the appearance of (2, 3)
res = Tuple.count((2, 3))
print('Count of (2, 3) in Tuple is:', res)

# count the appearance of [3, 2]
res = Tuple.count([3, 2])
print('Count of [3, 2] in Tuple is:', res)
