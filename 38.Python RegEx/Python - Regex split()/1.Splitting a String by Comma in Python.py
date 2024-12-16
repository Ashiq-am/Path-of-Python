import re
s = "Geeks for Geeks"

# Regular expression to match one or more non-word characters
pattern = r'\W+'

 # Split the string using the pattern
words = re.split(pattern, s)
print(words)