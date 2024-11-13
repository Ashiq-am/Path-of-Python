# Python 3 code to demonstrate
# to get count of elements matching condition
# using sum()+ map()

# initializing list
test_list = [3, 5, 1, 6, 7, 9]

# printing original list
print ("The original list is : " + str(test_list))

# using sum()+ map()
# to get count of elements matching condition
# checks for odd
res = sum(map(lambda i: i % 2 != 0, test_list))

# printing result
print ("The number of odd elements: " + str(res))
