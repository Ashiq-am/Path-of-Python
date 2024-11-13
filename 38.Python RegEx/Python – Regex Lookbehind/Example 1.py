# importing regex
import re

# Regex Lookbehind example
example = re.search(r'(?<=geeks)\w', 'geeksforgeeks')

print(example.group())
print("Pattern found from index", example.start(), example.end())
