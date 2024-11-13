# Python3 code to demonstrate
# Consecutive Product list
# using list comprehension

# initializing list
test_list = [1, 4, 5, 3, 6]


# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension
# Consecutive Product list
res = [test_list[i] * test_list[i + 1] for i in range(len(test_list)-1)]

# printing result
print ("The computed successive product list is : " + str(res))
