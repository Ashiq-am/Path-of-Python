# Python3 code to demonstrate working of
# Overlapping consecutive K splits
# Using list comprehension + slicing

# initializing string
test_str = 'Geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 4

# extracting window using slicing
res = [test_str[idx:idx + K] for idx in range(len(test_str) - K + 1)]

# printing result
print("Overlapping windows : " + str(res))
