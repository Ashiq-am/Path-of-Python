# Python3 code to demonstrate working of
# Column Minimum in Tuple list
# using zip() + map() + min()

# initialize list
test_list = [(1, 2, 3), (6, 7, 6), (1, 6, 8)]

# printing original list
print("The original list : " + str(test_list))

# Column Minimum in Tuple list
# using zip() + map() + min()
res = list(map(min, zip(*test_list)))

# printing result
print("The Cummulative column minimum is : " + str(res))
