# Python3 code to demonstrate
# Tuple Column element frequency
# using map() + count()

# initializing list of tuples
test_list = [(1, 'Geeks'), (2, 'for'), (3, 'Geeks')]

# printing the original list
print ("The original list is : " + str(test_list))

# initializing K
K = 1

# using map() + count()
# Tuple Column element frequency
res = list(map(lambda i : i[K], test_list)).count('Geeks')

# printing result
print ("The frequency of element at Kth index is : " + str(res))
