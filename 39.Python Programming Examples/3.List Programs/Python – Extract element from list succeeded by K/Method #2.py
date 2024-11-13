# Python3 code to demonstrate working of
# Extract elements succeeded by K
# Using list comprehension

# initializing list
test_list = [2, 3, 5, 7, 8, 5, 3, 5]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# List comprehension used as shorthand
res = [test_list[idx]
	for idx in range(len(test_list) - 1) if test_list[idx + 1] == K]

# printing result
print("Extracted elements list : " + str(res))
