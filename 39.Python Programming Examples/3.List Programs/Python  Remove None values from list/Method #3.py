# Python3 code to demonstrate
# removing None values in list
# using filter()

# initializing list
test_list = [1, None, 4, None, None, 5, 8, None]

# printing original list
print ("The original list is : " + str(test_list))

# using filter()
# to remove None values in list
res = list(filter(None, test_list))

# printing result
print ("List after removal of None values : " + str(res))
