# Python3 code to demonstrate
# finding frequency in list of tuples
# using map() + count()

# initializing list of tuples
test_list = [('Geeks', 1), ('for', 2), ('Geeks', 3)]

# printing the original list
print ("The original list is : " + str(test_list))

# using map() + count()
# finding frequency in list of tuples
res = list(map(lambda i : i[0], test_list)).count('Geeks')

# printing result
print ("The frequency of element is : " + str(res))
