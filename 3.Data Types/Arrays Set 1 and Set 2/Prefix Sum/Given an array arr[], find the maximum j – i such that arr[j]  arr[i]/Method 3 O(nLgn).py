# Python3 implementation of the above approach
n = 9
a = [34, 8, 10, 3, 2, 80, 30, 33, 1]

# To store the index of an element.
index = dict()
for i in range(n):
	if a[i] in index:

		# append to list (for duplicates)
		index[a[i]].append(i)
	else:

		# if first occurrence
		index[a[i]] = [i]

# sort the input array
a.sort()
maxDiff = 0

# Temporary variable to keep track of minimum i
temp = n
for i in range(n):
	if temp > index[a[i]][0]:
		temp = index[a[i]][0]
	maxDiff = max(maxDiff, index[a[i]][-1]-temp)

print(maxDiff)
