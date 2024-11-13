# Python3 code to demonstrate
# test for values in tuple of tuple
# using any()

# initializing tuple of tuple
test_tuple = (("geeksforgeeks", "gfg"), ("CS_Portal", "best"))

# printing tuple
print ("The original tuple is " + str(test_tuple))

# using any()
# to test for value in tuple of tuple
if (any('geeksforgeeks' in i for i in test_tuple)) :
	print("geeksforgeeks is present")
else :
	print("geeksforgeeks is not present")
