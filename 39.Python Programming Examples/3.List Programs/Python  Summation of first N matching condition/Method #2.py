# Python 3 code to demonstrate
# Summation of first N matching condition
# using sum() + list comprehension

# initializing list
test_list = [3, 5, 1, 6, 7, 9, 8, 5]

# printing original list
print ("The original list is : " + str(test_list))

# using sum() + list comprehension
# to sum first N elements matching condition
# sum first 3 odd occurrences
res = sum([i for i in test_list if i % 2 != 0][:3])

# printing result
print ("The filtered list is : " + str(res))
