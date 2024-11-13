# Python 3 code to demonstrate
# checking substring in string
# using str.find()

# initializing string
test_str = "GeeksforGeeks"

# using str.find() to test
# for substring
res = test_str.find("for")
if res >= 0:
	print ("for is present in GeeksforGeeks")
else :
	print ("for is not present in GeeksforGeeks")
