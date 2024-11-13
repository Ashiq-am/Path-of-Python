# Python3 code to demonstrate
# Common Row elements Summation
# using map() + intersection() + sum()

# initializing list of lists
test_list = [[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]]

# printing original list
print ("The original list is : " + str(test_list))

# Common Row elements Summation
# using map() + intersection() + sum()
res = sum(list(set.intersection(*map(set, test_list))))

# printing result
print ("The common row elements sum is : " + str(res))
