# Defining the list
l = [12, 22, 4, 3, 7, 8, 10, 22]

# Finding maximum element
m = max(l)

# iterating over the list like index,
# item pair
for i, j in enumerate(l):

	if j == m:
		print("Index of the max element in a list is", i)
