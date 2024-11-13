import re

print(re.search(r"z(?=a)", "pizza"))
print(re.search(r"z(?!a)", "pizza"))
