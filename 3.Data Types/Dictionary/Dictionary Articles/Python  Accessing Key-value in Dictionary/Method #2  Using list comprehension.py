# Python3 code to demonstrate
# to get key and value
# using list comprehension

# initializing dictionary
test_dict = {"Geeks" : 1, "for" : 2, "geeks" : 3}

# Printing dictionary
print ("Original dictionary is : " + str(test_dict))

# using list comprehension to
# get key and value
print ("Dict key-value are : ")
print([(k, test_dict[k]) for k in test_dict])
