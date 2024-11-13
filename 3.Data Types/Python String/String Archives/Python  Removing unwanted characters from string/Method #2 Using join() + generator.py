# Python3 code to demonstrate
# removal of bad_chars
# using join() + generator

# initializing bad_chars_list
bad_chars = [';', ':', '!', "*"]

# initializing test string
test_string = "Ge;ek * s:fo ! r;Ge * e*k:s !"

# printing original string
print ("Original String : " + test_string)

# using join() + generator to
# remove bad_chars
test_string = ''.join(i for i in test_string if not i in bad_chars)

# printing resultant string
print ("Resultant list is : " + str(test_string))
