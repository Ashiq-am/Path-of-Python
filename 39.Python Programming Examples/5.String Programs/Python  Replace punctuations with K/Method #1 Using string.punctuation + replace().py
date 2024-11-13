# Python3 code to demonstrate working of
# Replace punctuations with K
# Using string.punctuation + replace()
from string import punctuation

# initializing string
test_str = 'geeksforgeeks, is : best for ; geeks !!'

# printing original string
print("The original string is : " + str(test_str))

# initializing replace character
repl_char = '*'

# Replace punctuations with K
# Using string.punctuation + replace()
for chr in punctuation:
	test_str = test_str.replace(chr, repl_char)

# printing result
print("The strings after replacement : " + test_str)
