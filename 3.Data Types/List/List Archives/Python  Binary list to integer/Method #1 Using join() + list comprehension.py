# Python3 code to demonstrate
# converting binary list to integer
# using join() + list comprehension

# initializing list
test_list = [1, 0, 0, 1, 1, 0]

# printing original list
print ("The original list is : " + str(test_list))

# using join() + list comprehension
# converting binary list to integer
res = int("".join(str(x) for x in test_list), 2)

# printing result
print ("The converted integer value is : " + str(res))
