# Python 3 code to demonstrate
# False values Frequency
# using sum() + generator expression

# initializing list
test_list = [3, False, False, 6, False, 9]

# printing original list
print ("The original list is : " + str(test_list))

# using sum() + generator expression
# False values Frequency
# checks for False
res = sum(1 for i in test_list if not i)

# printing result
print ("The number of False elements: " + str(res))
