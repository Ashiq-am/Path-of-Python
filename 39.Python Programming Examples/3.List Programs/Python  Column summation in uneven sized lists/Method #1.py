# Python code to demonstrate
# Column summation in uneven sized lists
# using sum() + filter() + map() + list comprehension

# initializing list of lists
test_list = [[1, 5, 3], [4], [9, 8]]

# printing original list
print ("The original list is : " + str(test_list))

# using sum() + filter() + map() + list comprehension
# Column summation in uneven sized lists
res = [sum(filter(None, j)) for j in map(None, *test_list)]

# printing result
print ("The summation of columns is : " + str(res))
