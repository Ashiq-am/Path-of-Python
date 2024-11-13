# Python3 code to demonstrate
# to check for strictly increasing list
# using zip() + all()

# initializing list
test_list = [1, 4, 5, 7, 8, 10]

# printing original lists
print ("Original list : " + str(test_list))

# using zip() + all()
# to check for strictly increasing list
res = all(i < j for i, j in zip(test_list, test_list[1:]))

# printing result
print ("Is list strictly increasing ? : " + str(res))
