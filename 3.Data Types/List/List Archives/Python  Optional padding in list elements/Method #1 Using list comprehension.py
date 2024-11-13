# Python3 code to demonstrate
# to perform list element padding
# using list comprehension

# initializing list
test_list = [3, 54, 4, 1, 10]

# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension
# to perform list element padding
res = ["%02d" %i for i in test_list]

# printing result
print ("The list after element padding " + str(res))
