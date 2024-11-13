# Python3 code to demonstrate
# removal of bad_chars
# using replace()

# initializing bad_chars_list
bad_chars = [';', ':', '!', "*"]

# initializing test string
test_string = "Ge;ek * s:fo ! r;Ge * e*k:s !"

# printing original string
print ("Original String : " + test_string)

# using replace() to
# remove bad_chars
for i in bad_chars :
	test_string = test_string.replace(i, '')

# printing resultant string
print ("Resultant list is : " + str(test_string))
