# Python 3 code to demonstrate
# application of popitem()

# initializing dictionary
test_dict = { "Nikhil" : 7, "Akshat" : 1, "Akash" : 2 }

# Printing initial dict
print ("The dictionary before deletion : " + str(test_dict))

n = len(test_dict)

# using popitem to assign ranks
for i in range(0, n) :
	print ("Rank " + str(i + 1) + " " + str(test_dict.popitem()))

# Printing end dict
print ("The dictionary after deletion : " + str(test_dict))
