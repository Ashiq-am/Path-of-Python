import re


match = re.search(r'.+','Hello,\nGeeks', re.DOTALL)
print(match)
