# Python 3 code to demonstrate
# Nth smallest Greater than K
# using min() + sort() + lambda

# Initializing list
test_list = [1, 4, 7, 5, 10]

# Initializing k
k = 6

# Initializing N
N = 2

# Printing original list
print ("The original list is : " + str(test_list))

# Nth smallest Greater than K
# using min() + sort() + lambda
res = list(filter(lambda i: i > k, test_list))
res.sort()

# Printing result
print ("The Nth minimum value greater than 6 is : " + str(res[N - 1]))
