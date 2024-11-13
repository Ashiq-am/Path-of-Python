# Python3 code to demonstrate
# Test if K occurs N consecutive times
# using lambda + join()

# Initializing list
test_list = [1, 3, 4, 4, 4, 3, 3, 2, 2, 1]

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 4

# Initializing N
N = 3

# Test if K occurs N consecutive times
# using lambda + join()
res = bool(lambda ele: str(K) * N in ''.join(str(num) for num in test_list))

# printing result
print ("Does K occur N consecutive times ? : " + str(res))
