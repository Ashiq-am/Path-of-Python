# Python3 code to demonstrate working of
# Maximum difference tuple pair
# Using lambda + max()

# initialize list
test_list = [(3, 5), (1, 7), (10, 3), (1, 2)]

# printing original list
print("The original list : " + str(test_list))

# Maximum difference tuple pair
# Using lambda + max()
res = max(test_list, key = lambda sub: abs(sub[1] - sub[0]))

# printing result
print("Maximum difference among pairs : " + str(res))
