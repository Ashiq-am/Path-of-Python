# Python program to illustrate
# Matching regex objects
# with multiple Groups with the Pipe
import re
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
