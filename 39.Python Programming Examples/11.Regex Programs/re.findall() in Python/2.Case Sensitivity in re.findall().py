import re

s = "Python is fun. python is cool."
result = re.findall(r'python', s, re.IGNORECASE)
print(result)