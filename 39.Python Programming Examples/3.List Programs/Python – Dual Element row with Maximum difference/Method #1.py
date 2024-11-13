# Python3 code to demonstrate
# Dual Element row with Maximum difference
# using loop

# Initializing list
test_list = [[5, 10], [1, 3], [4, 11], [1, 2]]

# printing original list
print("The original list is : " + str(test_list))

# Dual Element row with Maximum difference
# using loop
max_till = -float('inf')
res = []
for sub in test_list:
	if abs(sub[0] - sub[1]) > max_till:
		max_till = abs(sub[0] - sub[1])
		res = sub

# printing result
print ("The maximum difference row is : " + str(res))
