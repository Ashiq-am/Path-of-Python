# Python3 code to demonstrate
# to convert list of string and characters
# to list of characters
# using join()

# initializing list
test_list = [ 'gfg', 'i', 's', 'be', 's', 't']

# printing original list
print ("The original list is : " + str(test_list))

# using join()
# to convert list of string and characters
# to list of characters
res = list(''.join(test_list))

# printing result
print ("The list after conversion is : " + str(res))
