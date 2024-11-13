# Python3 code to demonstrate
# to convert list of string and characters
# to list of characters
# using list comprehension

# initializing list
test_list = [ 'gfg', 'i', 's', 'be', 's', 't']

# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension
# to convert list of string and characters
# to list of characters
res = [i for ele in test_list for i in ele]

# printing result
print ("The list after conversion is : " + str(res))
