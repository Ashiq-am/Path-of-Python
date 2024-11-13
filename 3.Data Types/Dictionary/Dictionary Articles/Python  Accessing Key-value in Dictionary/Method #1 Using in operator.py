# Python3 code to demonstrate
# to get key and value
# using in operator

# initializing dictionary
test_dict = {"Geeks" : 1, "for" : 2, "geeks" : 3}

# Printing dictionary
print ("Original dictionary is : " + str(test_dict))

# using in operator to
# get key and value
print ("Dict key-value are : ")
for i in test_dict :
	print(i, test_dict[i])
