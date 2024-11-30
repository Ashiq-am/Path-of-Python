import re

# Removing multiple characters using regex

s1 = "Welcome to Python programming!"
ch = "om "

# Creating a regex pattern to match all characters to remove

p = f"[{ch}]"
s2 = re.sub(p, "", s1)

print(s2)