# Python3 code to demonstrate working of
# Mid occurrence of K in string
# Using find() + max() + slice

# initializing string
test_str = "geeksforgeeks is best for all geeks"

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 'e'

# getting all the indices of K
indices = [idx for idx, ele in enumerate(test_str) if ele == K]

# getting mid index
res = indices[len(indices) // 2]

# printing result
print("Mid occurrence of K : " + str(res))
