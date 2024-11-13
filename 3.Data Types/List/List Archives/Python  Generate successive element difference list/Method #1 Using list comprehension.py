# Python3 code to demonstrate
# to generate successive difference list
# using list comprehension

# initializing list
test_list = [1, 4, 5, 3, 6]


# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension
# generate successive difference list
res = [test_list[i + 1] - test_list[i] for i in range(len(test_list)-1)]

# printing result
print ("The computed successive difference list is : " + str(res))
