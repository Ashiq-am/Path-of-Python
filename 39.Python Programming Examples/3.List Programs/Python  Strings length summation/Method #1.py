# Python3 code to demonstrate
# string lengths summation
# using sum() + list comprehension

# initializing list of tuples
test_list = ['Geeks', 'for', 'Geeks']

# printing the original list
print ("The original list is : " + str(test_list))

# using sum() + list comprehension
# string lengths summation
res = sum(len(i) for i in test_list)

# printing result
print ("The summation of strings is : " + str(res))
