# Python3 code to demonstrate working of
# Append according to Kth character
# Using list comprehension

# initializing lists
test_list = ["geeksforgeeks", "best", "for", "geeks"]

# printing string
print("The original list : " + str(test_list))

# initializing K
K = 2

# initializing N
N = 'e'

# initializing i, j
i, j = "**", "##"

# shorthand to solve this problem
res = [sub + i if sub[K] == N else sub + j for sub in test_list]

# printing results
print("The resultant List : " + str(res))
