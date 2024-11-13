# Python3 code to demonstrate working of
# Number of positions where Substrings Match of Length K
# Using map() + list comprehension

# initializing strings
test_str1 = 'geeksforgeeks'
test_str2 = 'peeksformeeks'

# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# initializing K
K = 3

# Extracting Substrings
subs_str = [test_str1[idx : idx + K] for idx in range(len(test_str1) - K - 1)]

# checking in other string
# using count() to get number
res = list(map(lambda ele: ele in test_str2, subs_str)).count(True)

# printing result
print("Number of positions of matching K length Substrings : " + str(res))
