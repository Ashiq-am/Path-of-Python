import re

# Using lookbehind
example1 = re.search(r'(?<=[a-z])\d', "geeks12")
print(example1.group())

# Without using lookbehind
example2 = re.search(r'([a-z])\d', "geeks12")
print(example2.group())
