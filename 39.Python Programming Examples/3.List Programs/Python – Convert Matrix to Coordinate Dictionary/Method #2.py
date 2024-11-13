# Python3 code to demonstrate working of
# Convert Matrix to Coordinate Dictionary
# Using setdefault() + loop

# initializing list
test_list = [['g', 'f', 'g'], ['i', 's', 'g'], ['b', 'e', 's', 't']]

# printing original list
print("The original list is : " + str(test_list))

# Convert Matrix to Coordinate Dictionary
# Using setdefault() + loop
res = dict()
for idx, ele in enumerate(test_list):
	for j, sub in enumerate(ele):
		res.setdefault(sub, set()).add((idx, j))

# printing result
print("The Coordinate Dictionary : " + str(res))
