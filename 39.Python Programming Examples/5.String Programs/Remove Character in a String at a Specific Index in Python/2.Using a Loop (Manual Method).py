s1 = "Python"

# Index of the character to remove
idx = 3

# Use a loop to build a new string without the character
res = ''.join(char for i, char in enumerate(s1) if i != idx)
print(res)