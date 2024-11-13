# Python 3 code to demonstrate
# checking substring in string
# using str.index()

# initializing string
test_str = "GeeksforGeeks"

# using str.index() to test
# for substring
try :
	res = test_str.index("forg")
	print ("forg exists in GeeksforGeeks")
except :
	print ("forg does not exists in GeeksforGeeks")
