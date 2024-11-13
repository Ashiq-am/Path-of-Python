# Defining a list
l = [1, 4, 3, 7, 8, 10, 2]

# Calculating the maximum element
# in the list
m = max(l)

# Finding the index of the maximum
# element
i = 0
while(i < len(l)):
	if l[i] == m:
		print("Index of the max element in a list is", i)
		break
	i += 1
