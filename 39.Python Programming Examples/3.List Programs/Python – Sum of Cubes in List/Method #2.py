# Python3 code to demonstrate
# Cube Summation in List
# using sum() + map()

# initializing list
test_list = [3, 5, 7, 9, 11]

# printing original list
print ("The original list is : " + str(test_list))

# using sum() + map()
# Cube Summation in List
res = sum(map(lambda i : i * i * i, test_list))

# printing result
print ("The sum of cubes of list is : " + str(res))
