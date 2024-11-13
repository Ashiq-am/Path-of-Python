# Python3 code to demonstrate
# min and max in list of tuples
# using map() + zip()

# initializing list
test_list = [(2, 3), (4, 7), (8, 11), (3, 6)]

# printing original list
print ("The original list is : " + str(test_list))

# using map() + zip()
# to get min and max in list of tuples
res1 = list(map(max, zip(*test_list)))
res2 = list(map(min, zip(*test_list)))

# printing result
print ("The indices wise maximum number : " + str(res1))
print ("The indices wise minimum number : " + str(res2))
