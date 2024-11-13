# importing re module for creating
# regex expression
import re

# string for passing
text = "Welcome to geeks for geeks [GFG] A (computer science portal)"

# creating the regex pattern & use re.sub()
# [\([{})\]] is a RE pattern for selecting
# '{', '}', '[', ']', '(', ')' brakcets.
patn = re.sub(r"[\([{})\]]", "", text)

print(patn)
