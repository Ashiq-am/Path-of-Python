import re
# Input text containing a mix of
# alphabetic characters and digits
Text = "Mango,Orange1Banana"
P = re.split(r'\d', Text)
# Printing the resulting list of substrings
print(P)
