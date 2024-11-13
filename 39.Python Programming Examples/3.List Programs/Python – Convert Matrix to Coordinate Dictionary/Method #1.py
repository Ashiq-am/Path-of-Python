# Python3 code to demonstrate working of
# Convert Matrix to Coordinate Dictionary
# Using loop + enumerate()

# initializing list
test_list = [['g', 'f', 'g'], ['i', 's', 'g'], ['b', 'e', 's', 't']]

# printing original list
print("The original list is : " + str(test_list))

# Convert Matrix to Coordinate Dictionary
# Using loop + enumerate()
res = dict()
for idx, sub in enumerate(test_list):
	for j, ele in enumerate(sub):
		if ele in res:
			res[ele].add((idx, j))
		else:
			res[ele] = {(idx, j)}

# printing result
print("The Coordinate Dictionary : " + str(res))
