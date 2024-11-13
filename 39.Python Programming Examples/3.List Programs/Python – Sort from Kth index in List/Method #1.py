# Python3 code to demonstrate working of
# Perform sort from Kth index
# Using loop + list slicing

# initializing list
test_list = [8, 4, 7, 3, 2, 14, 6]

# printing original list
print("The original list : " + str(test_list))

# initialzing K
K = 3

# Using loop + list slicing
res = []

# Using loop to extract elements till K
for idx, ele in enumerate(test_list):
	if idx < K:
		res.append(ele)

# join sorted and unsorted segments
res = res + sorted(test_list[K:])

# printing result
print("Partially sorted list : " + str(res))
