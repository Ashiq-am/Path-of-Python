import re

# Sample string with HTML tags
s1 = "<h1>Welcome to Python Programming</h1>"

# Removing HTML tags using regex
s2 = re.sub(r"<.*?>", "", s1)
print(s2)