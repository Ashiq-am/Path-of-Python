# Python code to demonstrate
# Uneven Sized Matrix Column Minimum
# using min() + filter() + map() + list comprehension

# initializing list of lists
test_list = [[1, 5, 3], [4], [9, 8]]

# printing original list
print ("The original list is : " + str(test_list))

# using min() + filter() + map() + list comprehension
# Uneven Sized Matrix Column Minimum
res = [min(filter(None, j)) for j in map(None, *test_list)]

# printing result
print ("The minimum of columns is : " + str(res))
