# Python3 code to demonstrate working of
# Number of positions where Substrings Match of Length K
# Using list comprehension + min() + slicing

# initializing strings
test_str1 = 'geeksforgeeks'
test_str2 = 'peeksformeeks'

# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# initializing K
K = 3

# checking for substrings,
# using len() to get total count
res = len([test_str1[idx : idx + K] for idx in range(min(len(test_str1), len(test_str2)) - K - 1)
		if test_str1[idx : idx + K] == test_str2[idx : idx + K]])

# printing result
print("Number of positions of matching K length Substrings : " + str(res))
