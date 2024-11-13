# Python3 code to demonstrate
# removal of bad_chars
# using filter()

# initializing bad_chars_list
bad_chars = [';', ':', '!', "*"]

# initializing test string
test_string = "Ge;ek*s:fo!r;Ge*e*k:s!"

# printing original string
print("Original String : " + test_string)

# using filter() to
# remove bad_chars
test_string = ''.join((filter(lambda i: i not in bad_chars, test_string)))
# printing resultant string
print("Resultant list is : " + str(test_string))
