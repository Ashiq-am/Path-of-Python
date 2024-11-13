# Python3 code to demonstrate
# conversion of list of tuple to list of list
# using list comprehension + join()

# initializing list
test_list = [('G', 'E', 'E', 'K', 'S'), ('F', 'O', 'R'),
							('G', 'E', 'E', 'K', 'S')]

# printing the original list
print ("The original list is : " + str(test_list))

# using list comprehension + join()
# conversion of list of tuple to list of list
res = [''.join(i) for i in test_list]

# printing result
print ("The list after conversion to list of string : " + str(res))
