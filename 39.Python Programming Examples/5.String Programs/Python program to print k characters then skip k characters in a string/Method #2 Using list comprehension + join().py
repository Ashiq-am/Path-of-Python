# Python3 code to demonstrate working of
# Alternate K Length characters
# Using list comprehension + join()

# initializing string
test_str = 'geeksgeeksisbestforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 4

# slicing K using slicing, join for converting back to string
res = ''.join([test_str[idx : idx + K] for idx in range(0, len(test_str), K * 2)])

# printing result
print("Transformed String : " + str(res))
