# Python3 code to demonstrate
# to check if string is empty
# using len()

# inilializing string
test_str1 = ""
test_str2 = " "

# checking if string is empty
print ("The zero length string without spaces is empty ? : ", end = "")
if(len(test_str1) == 0):
	print ("Yes")
else :
	print ("No")

# prints No
print ("The zero length string with just spaces is empty ? : ", end = "")
if(len(test_str2) == 0):
	print ("Yes")
else :
	print ("No")
