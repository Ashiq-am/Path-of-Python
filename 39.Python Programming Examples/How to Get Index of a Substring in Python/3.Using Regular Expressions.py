import re

s1 = "Welcome to Python programming"
s2 = "Python"

# Using regex to find the substring
match = re.search(s2, s1)
if match:
    print("Found at index:", match.start())
else:
    print("Substring not found")