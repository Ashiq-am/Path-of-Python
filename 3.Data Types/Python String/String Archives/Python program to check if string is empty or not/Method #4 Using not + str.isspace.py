# Python 3 code to demonstrate
# to check if string is empty
# using not + isspace()

# inilializing string
test_str1 = ""
test_str2 = " "

# checking if string is empty
print ("The zero length string without spaces is empty ? : ", end = "")
if(not (test_str1 and not test_str1.isspace())):
	print ("Yes")
else :
	print ("No")

# prints Yes
print ("The zero length string with just spaces is empty ? : ", end = "")
if(not (test_str2 and not test_str2.isspace())):
	print ("Yes")
else :
	print ("No")
