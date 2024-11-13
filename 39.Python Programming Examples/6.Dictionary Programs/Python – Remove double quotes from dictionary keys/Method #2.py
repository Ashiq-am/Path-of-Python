# Python3 code to demonstrate working of
# Remove double quotes from dictionary keys
# Using re.sub() + dictionary comprehension
import re

# initializing dictionary
test_dict = {'"Geeks"': 3, '"is" for': 5, '"g"eeks': 9}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# regex making replacement of double quotes with empty string
res = {re.sub(r'"', '', key): val for key, val in test_dict.items()}

# printing result
print("The dictionary after removal of double quotes : " + str(res))
