# Python3 code to demonstrate working of
# Record Point with Minimum difference
# Using lambda + min()

# initialize list
test_list = [(3, 5), (1, 7), (10, 3), (1, 2)]

# printing original list
print("The original list : " + str(test_list))

# Record Point with Minimum difference
# Using lambda + min()
res = min(test_list, key = lambda sub: abs(sub[1] - sub[0]))

# printing result
print("Minimum difference among pairs : " + str(res))
