# Python3 code to demonstrate
# to convert the list of string to list of list
# using list slicing + split()

# initializing list
test_list = [ '[1, 4, 5]', '[4, 6, 8]' ]

# printing original list
print ("The original list is : " + str(test_list))

# using list slicing + split()
# to convert list of string to list of list
res = [i[1 : -1].split(', ') for i in test_list]

# printing result
print ("The list after conversion is : " + str(res))
