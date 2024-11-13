# Python3 code to demonstrate
# removal of bad_chars
# using translate()
import string
# initializing bad_chars_list
bad_chars = [';', ':', '!', "*"]

# initializing test string
test_string = "Ge;ek * s:fo ! r;Ge * e*k:s !"

# printing original string
print ("Original String : " + test_string)

# using translate() to
# remove bad_chars
delete_dict = {sp_character: '' for sp_character in string.punctuation}
delete_dict[' '] = ''
table = str.maketrans(delete_dict)
test_string = test_string.translate(table)

# printing resultant string
print ("Resultant list is : " + str(test_string))
