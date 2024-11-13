# Python3 code to demonstrate working of
# Custom Consecutive Character Pairing
# Using join() + list comprehension
import string

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + test_str)

# initializing Delim
delim = '_'

# Custom Consecutive Character Pairing
# Using join() + list comprehension
res = [delim.join(test_str[idx : idx + 2]) for idx in range(len(test_str) - 1)]

# printing result
print("The List of joined Characters : " + str(res))
