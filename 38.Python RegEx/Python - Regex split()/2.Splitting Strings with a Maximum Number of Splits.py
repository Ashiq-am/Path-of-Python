import re

s = "Geeks for Geeks"

#Using re.split() to split the string
#by spaces with a maximum of 2 splits
result = re.split(r' ', s, maxsplit=2)
print(result)