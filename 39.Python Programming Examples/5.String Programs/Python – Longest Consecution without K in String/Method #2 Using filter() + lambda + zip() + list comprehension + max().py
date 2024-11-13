# Python3 code to demonstrate working of
# Longest Consecution without K in String
# Using filter() + lambda + zip() + list comprehension + max()

# initializing string
test_str = 'geeksforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 'e'

# getting all indices using filter + lambda
indxs = list(filter(lambda ele: test_str[ele] == 'e', range(len(test_str))))

# getting difference using zip()
# negative index, for getting successive elements
diffs = [j - i for i, j in zip(indxs[: -1], indxs[1 :])]

# getting max diff
res = max(diffs)

# printing result
print("Longest run : " + str(res))
