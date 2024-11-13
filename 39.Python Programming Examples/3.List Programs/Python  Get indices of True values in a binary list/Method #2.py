# Python3 code to demonstrate
# to return true value indices.
# using lambda + filter() + range()

# initializing list
test_list = [True, False, True, False, True, True, False]

# printing original list
print ("The original list is : " + str(test_list))

# using lambda + filter() + range()
# to return true indices.
res = list(filter(lambda i: test_list[i], range(len(test_list))))

# printing result
print ("The list indices having True values are : " + str(res))
