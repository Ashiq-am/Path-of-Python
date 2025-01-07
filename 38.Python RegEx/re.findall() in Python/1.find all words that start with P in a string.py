import re

s = "Python is Powerful and Great"
result = re.findall(r'\bP\w+', s)
print(result)