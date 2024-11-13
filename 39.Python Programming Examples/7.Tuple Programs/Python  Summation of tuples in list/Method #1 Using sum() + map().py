# Python3 code to demonstrate working of
# Summation of tuples in list
# using sum() + map()

# initialize list of tuple
test_list = [(1, 3), (5, 6, 7), (2, 6)]

# printing original tuples list
print("The original list : " + str(test_list))

# Summation of tuples in list
# using sum() + map()
res = sum(map(sum, test_list))

# printing result
print("The summation of all tuple elements are : " + str(res))
