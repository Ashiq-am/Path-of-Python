# Python3 code to demonstrate
# to convert list of string to list of list
# using strip() + split()

# initializing list
test_list = [ '[1, 4, 5]', '[4, 6, 8]' ]

# printing original list
print ("The original list is : " + str(test_list))

# using strip() + split()
# to convert list of string to list of list
res = [i.strip("[]").split(", ") for i in test_list]

# printing result
print ("The list after conversion is : " + str(res))
