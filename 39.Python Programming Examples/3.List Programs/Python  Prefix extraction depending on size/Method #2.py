# Python3 code to demonstrate
# Prefix extraction depending on size
# using filter() + lambda

# Initializing list
test_list = ['geeksforgeeks', 'is', 'best', 'for', 'geeks']

# Initializing K
K = 2

# Initializing N
N = 4

# printing original list
print("The original list is : " + str(test_list))

# Prefix extraction depending on size
# using filter() + lambda
res = [sub[:K] for sub in filter(lambda ele: len(ele) >= N, test_list)]

# printing result
print("List after prefix extraction : " + str(res))
