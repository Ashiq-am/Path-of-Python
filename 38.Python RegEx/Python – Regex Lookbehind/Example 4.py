import re

# Lookbehind
example1 = re.search('(?<=[a-z])geeks', 'geeksforgeeks')
print(example1.group())

# Negative Lookbehind
example2 = re.search('(?<![a-z])123', 'geeks123')

# Output is None because 123
# is preceded by a character i.e 's'
print(example2)
