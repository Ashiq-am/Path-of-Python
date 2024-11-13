# Python3 code to demonstrate working of
# Remove all control characters
# Using unicodedata library
import unicodedata

# initializing string
test_str = 'Geeks\0\r for \n\bge\tee\0ks\f'

# printing original string
print("The original string is : " + str(test_str))

# surpassing all control characters
# checking for starting with C
res = "".join(char for char in test_str if unicodedata.category(char)[0]!="C")

# printing result
print("String after removal of control characters : " + str(res))
