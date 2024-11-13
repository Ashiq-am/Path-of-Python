# Python3 code to demonstrate working of
# Slice from Last Occurrence of K
# Using string slicing and loop

# initializing string
test_str = 'geeksforgeeks-is-best-for-geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = "-"

# Slice from Last Occurrence of K
# Using string slicing and loop
idx = None
for i in range(len(test_str)):
	if K == test_str[i]:
		idx = i
res = test_str[:idx]

# printing result
print("Sliced String is : " + str(res))
