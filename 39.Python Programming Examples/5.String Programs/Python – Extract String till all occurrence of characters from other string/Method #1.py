# Python3 code to demonstrate working of
# Extract String till all occurrence of characters from other string
# Using all() + slicing + loop

# initializing string
test_str = "geeksforgeeks is best for all geeks"

# printing original string
print("The original string is : " + str(test_str))

# initializing check string
check_str = "freak"

for idx in range(1, len(test_str)):
	temp = test_str[:idx]

	# checking for all chars of check_str in substring
	if all([char in temp for char in check_str]):
		res = temp
		break

# printing result
print("String till all characters occurred : " + str(res))
