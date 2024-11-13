# Python3 code to demonstrate working of
# Remove Non-English characters Strings from List
# Using regex + findall() + list comprehension
import re

# initializing list
test_list = ['Gfg', 'Good| ????', "for", '??Geeks???']

# printing original list
print("The original list is : " + str(test_list))

# using findall() to neglect unicode of Non-English alphabets
res = [idx for idx in test_list if not re.findall("[^\u0000-\u05C0\u2100-\u214F]+", idx)]

# printing result
print("The extracted list : " + str(res))
