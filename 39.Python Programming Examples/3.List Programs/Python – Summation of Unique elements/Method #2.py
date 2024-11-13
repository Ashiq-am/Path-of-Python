# Python 3 code to demonstrate
# Summation of Unique elements
# using set() + sum()

# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : " + str(test_list))

# using set() + sum()
# Summation of Unique elements
# from list
res = sum(list(set(test_list)))

# Summation of Unique elements
# using set() + sum()
print ("The unique elements summation : " + str(res))
