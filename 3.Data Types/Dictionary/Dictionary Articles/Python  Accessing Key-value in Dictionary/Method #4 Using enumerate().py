# Python3 code to demonstrate
# to get key and value
# using enumerate()

# initializing dictionary
test_dict = {"Geeks" : 1, "for" : 2, "geeks" : 3}

# Printing dictionary
print ("Original dictionary is : " + str(test_dict))

# using enumerate() to
# get key and value
print ("Dict key-value are : ")
for i in enumerate(test_dict.items()):
	print (i)
