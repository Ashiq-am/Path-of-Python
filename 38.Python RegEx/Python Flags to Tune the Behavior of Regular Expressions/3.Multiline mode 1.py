import re


match = re.search(r'^Geeks', 'Hello,\nGeeks', re.MULTILINE)
print(match)
