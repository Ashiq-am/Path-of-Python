# Python3 code to demonstrate
# to get key and value
# using dict.items()

# initializing dictionary
test_dict = {"Geeks" : 1, "for" : 2, "geeks" : 3}

# Printing dictionary
print ("Original dictionary is : " + str(test_dict))

# using dict.items() to
# get key and value
print ("Dict key-value are : ")
for key, value in test_dict.items():
	print (key, value)
