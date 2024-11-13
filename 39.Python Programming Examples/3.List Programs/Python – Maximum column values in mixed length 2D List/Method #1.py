# Python code to demonstrate
# Maximum column values mixed length 2D List
# using max() + filter() + map() + list comprehension

# initializing list of lists
test_list = [[1, 5, 3], [4], [9, 8]]

# printing original list
print ("The original list is : " + str(test_list))

# using max() + filter() + map() + list comprehension
# Maximum column values mixed length 2D List
res = [max(filter(None, j)) for j in map(None, *test_list)]

# printing result
print ("The maximization of columns is : " + str(res))
