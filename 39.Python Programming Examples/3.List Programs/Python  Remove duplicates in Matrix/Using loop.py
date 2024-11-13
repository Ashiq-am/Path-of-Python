# Python3 code to demonstrate working of
# Removing duplicates in Matrix
# using loop

# initialize list
test_list = [[5, 6, 8], [8, 5, 3], [9, 10, 3]]

# printing original list
print("The original list is : " + str(test_list))

# Removing duplicates in Matrix
# using loop
res = []
track = []
count = 0

for sub in test_list:
	res.append([])
	for ele in sub:
		if ele not in track:
			res[count].append(ele)
			track.append(ele)
	count += 1

# printing result
print("The Matrix after duplicates removal is : " + str(res))
