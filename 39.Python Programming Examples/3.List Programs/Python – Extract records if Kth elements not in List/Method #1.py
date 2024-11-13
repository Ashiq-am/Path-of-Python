# Python3 code to demonstrate working of
# Extract records if Kth elements not in List
# Using loop

# initializing list
test_list = [(5, 3), (7, 4), (1, 3), (7, 8), (0, 6)]

# printing original list
print("The original list : " + str(test_list))

# initializing arg. list
arg_list = [4, 8, 4]

# initializing K
K = 1

# Using set() to shorten arg list
temp = set(arg_list)

# loop to check for elements and append
res = []
for sub in test_list:
	if sub[K] not in arg_list:
		res.append(sub)

# printing result
print("Extracted elements : " + str(res))
