# Python3 code to demonstrate
# to return true value indices.
# using enumerate() + list comprehension

# initializing list
test_list = [True, False, True, False, True, True, False]

# printing original list
print ("The original list is : " + str(test_list))

# using enumerate() + list comprehension
# to return true indices.
res = [i for i, val in enumerate(test_list) if val]

# printing result
print ("The list indices having True values are : " + str(res))
