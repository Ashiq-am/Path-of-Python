# Python3 code to demonstrate working of
# Remove Punctuation Tuples
# Using regex() + filter() + lambda + string.punctuation
import string
import re

# initializing list
test_list = [('.', ', '), ('!', '8'), ('5', '6'), (';', '10')]

# printing original list
print("The original list is : " + str(test_list))

# Remove Punctuation Tuples
# Using regex() + filter() + lambda + string.punctuation
temp = re.compile('[{}]'.format(re.escape(string.punctuation)))
res = list(filter(lambda tup: not temp.search(tup[0]), test_list))

# printing result
print("Tuples after punctuation removal : " + str(res))
