# Python3 code to demonstrate working of
# Slice from Last Occurrence of K
# Using rfind() + string slicing

# initializing string
test_str = 'geeksforgeeks-is-best-for-geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = "-"

# Slice from Last Occurrence of K
# Using rfind() + string slicing
idx = test_str.rfind(K)
res = test_str[:idx]

# printing result
print("Sliced String is : " + str(res))
