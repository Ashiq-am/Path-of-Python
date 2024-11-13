# initializing string
test_str = 'geeksforgeeks best for geeks'

# printing original string
print("The original string is : " + test_str)

# initializing K
K = 2

# joining Kth index of each word
res = ''.join([sub[K] for sub in test_str.split()])

# printing result
print("The K joined String is : " + str(res))
