# Python 3 code to demonstrate
# False values Frequency
# using sum()+ map()

# initializing list
test_list = [3, False, False, 6, False, 9]

# printing original list
print ("The original list is : " + str(test_list))

# using sum()+ map()
# False values Frequency
# checks for False
res = sum(map(lambda i: not i, test_list))

# printing result
print ("The number of False elements: " + str(res))
