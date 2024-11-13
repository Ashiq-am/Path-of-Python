# Python3 code to demonstrate working of
# Extracting Priority Elements in Tuple List
# loop

# initializing list
test_list = [(5, 1), (3, 4), (9, 7), (10, 6)]

# printing original list
print("The original list is : " + str(test_list))

# initializing Priority list
prior_list = [6, 4, 7, 1]

# Extracting Priority Elements in Tuple List
# loop
res = []
for sub in test_list:
	for val in prior_list:
		if val in sub:
			res.append(val)

# printing result
print("The extracted elements are : " + str(res))
