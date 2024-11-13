# Python3 code to demonstrate working of
# Pair Kth character with each element
# Using loop

# initializing string
test_str = "geeksforgeeks"

# printing original string
print("The original string is : " + test_str)

# initializing K
K = 4

# Pair Kth character with each element
# Using loop
res = []
for ele in test_str:
		res.append(test_str[K] + ele)

# printing result
print("List after pairing : " + str(res))
