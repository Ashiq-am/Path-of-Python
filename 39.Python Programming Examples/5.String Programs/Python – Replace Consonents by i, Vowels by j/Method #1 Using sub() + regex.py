# Python3 code to demonstrate working of
# Replace Consonents by i, Vowels by j
# Using Using sub() + regex
import re

# initializing strings
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing i, j
i, j = "V", "C"

# the negation of vowel regex is a consonent, denoted by "^"
res = re.sub("[^aeiouAEIOU]", j, test_str)
res = re.sub("[aeiouAEIOU]", i, res)

# printing result
print("The string after required replacement : " + str(res))
