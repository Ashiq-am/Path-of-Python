# Python 3 code to demonstrate
# checking substring in string
# using operator.contains()
import operator

# initializing string
test_str = "GeeksforGeeks"

# using operator.contains() to test
# for substring
if operator.contains(test_str, "for"):
	print ("for is present in GeeksforGeeks")
else :
	print ("for is not present in GeeksforGeeks")
