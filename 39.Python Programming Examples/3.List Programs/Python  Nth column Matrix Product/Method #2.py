# Python3 code to demonstrate working of
# Nth column Matrix Product
# Using loop

# initialize list
test_list = [[5, 6, 7],
			[9, 10, 2],
			[10, 3, 4]]

# printing original list
print("The original list is : " + str(test_list))

# initialize N
N = 2

# Nth column Matrix Product
# Using loop
res = 1
for sub in test_list:
	for idx in range(0, len(sub)):
		if idx == N:
			res = res * sub[idx]

# printing result
print("Product of Nth column is : " + str(res))
