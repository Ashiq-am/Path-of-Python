# Python3 code to demonstrate
# min and max in list of tuples
# using min() and max()

# initializing list
test_list = [(2, 3), (4, 7), (8, 11), (3, 6)]

# printing original list
print ("The original list is : " + str(test_list))

# using min() and max()
# to get min and max in list of tuples
res1 = min(test_list)[0], max(test_list)[0]
res2 = min(test_list)[1], max(test_list)[1]

# printing result
print ("The min and max of index 1 : " + str(res1))
print ("The min and max of index 2 : " + str(res2))
