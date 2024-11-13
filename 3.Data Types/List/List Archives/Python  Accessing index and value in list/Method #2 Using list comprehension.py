# Python3 code to demonstrate
# to get index and value
# using list comprehension

# initializing list
test_list = [1, 4, 5, 6, 7]

# Printing list
print ("Original list is : " + str(test_list))

# using list comprehension to
# get index and value
print ("List index-value are : ")
print ([list((i, test_list[i])) for i in range(len(test_list))])
