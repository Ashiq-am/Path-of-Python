# Python 3 code to demonstrate
# Test for strictly decreasing list
# using zip() + all()

# initializing list
test_list = [10, 8, 7, 5, 4, 1]

# printing original lists
print ("Original list : " + str(test_list))

# using zip() + all()
# Test for strictly decreasing list
res = all(i > j for i, j in zip(test_list, test_list[1:]))

# printing result
print ("Is list strictly decreasing ? : " + str(res))
