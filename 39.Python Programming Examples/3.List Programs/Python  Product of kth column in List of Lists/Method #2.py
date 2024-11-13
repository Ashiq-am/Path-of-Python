# Python3 code to demonstrate working of
# Column Product in List of Lists
# Using loop

# initialize list
test_list = [[5, 6, 7],
			[9, 10, 2],
			[10, 3, 4]]

# printing original list
print("The original list is : " + str(test_list))

# initialize K
K = 2

# Column Product in List of Lists
# Using loop
res = 1
for sub in test_list:
	for idx in range(0, len(sub)):
		if idx == K:
			res = res * sub[idx]

# printing result
print("Product of Kth column is : " + str(res))
