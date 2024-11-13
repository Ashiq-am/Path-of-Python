# Python3 code to demonstrate working of
# Remove index ranges from String
# Using any() + list comprehension + join()

# initializing strings
test_str1 = 'geeksforgeeks is best for geeks'

# printing original string
print("The original string 1 is : " + str(test_str1))

# initializing ranges list
range_list = [(3, 6), (7, 10), (14, 17)]

# using any() to check for strings in index ranges
res = ''.join(chr for idx, chr in enumerate(test_str1, 1) if not any(strt_idx <= idx <= end_idx
		for strt_idx, end_idx in range_list))

# printing result
print("The reconstructed string : " + str(res))
