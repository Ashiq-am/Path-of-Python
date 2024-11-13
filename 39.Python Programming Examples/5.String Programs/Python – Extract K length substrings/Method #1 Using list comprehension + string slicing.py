# Python3 code to demonstrate working of
# Extract K length substrings
# Using list comprehension + string slicing

# initializing string
test_str = "Geeks"

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 3

# Extract K length substrings
# Using list comprehension + string slicing
res = [test_str[i: j] for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1) if len(test_str[i:j]) == K]

# printing result
print("All K length substrings of string are : " + str(res))
