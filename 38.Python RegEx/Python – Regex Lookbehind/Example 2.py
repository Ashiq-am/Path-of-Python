# importing regex
import re

# Regex Lookbehind example
example = re.search(r'(?<=geeks)\d', 'geeksforgeeks')
print(example)
