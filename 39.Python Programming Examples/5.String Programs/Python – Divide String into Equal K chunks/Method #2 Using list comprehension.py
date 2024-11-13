# Python3 code to demonstrate working of
# Divide String into Equal K chunks
# Using list comprehension

# initializing strings
test_str = 'geeksforgeeks 1'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 5

# compute chunk length
chnk_len = len(test_str) // K

# one-liner to perform the task
res = [test_str[idx : idx + chnk_len] for idx in range(0, len(test_str), chnk_len)]

# printing result
print("The K len chunked list : " + str(res))
