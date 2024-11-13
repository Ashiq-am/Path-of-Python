# Python 3 code to demonstrate
# working of popitem()

# initializing dictionary
test_dict = { "Nikhil" : 7, "Akshat" : 1, "Akash" : 2 }

# Printing initial dict
print ("The dictionary before deletion : " + str(test_dict))

# using popitem() to return + remove arbitrary
# pair
res = test_dict.popitem()

# Printing the pair returned
print ('The arbitrary pair returned is : ' + str(res))

# Printing dict after deletion
print ("The dictionary after removal : " + str(test_dict))
