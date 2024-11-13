# Python3 code to demonstrate
# adding K to each element
# using list comprehension

# initializing list
test_list = [4, 5, 6, 3, 9]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 4

# using list comprehension
# adding K to each element
res = [x + K for x in test_list]

# printing result
print ("The list after adding K to each element : " + str(res))
