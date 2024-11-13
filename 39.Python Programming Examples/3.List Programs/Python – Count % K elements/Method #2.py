# Python 3 code to demonstrate
# Count % K elements
# using sum()+ map()

# initializing list
test_list = [3, 5, 1, 6, 7, 9]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 3

# using sum()+ map()
# to get count of elements matching condition
# Count % K elements
res = sum(map(lambda i: i % K != 0, test_list))

# printing result
print ("The number of % K elements: " + str(res))
