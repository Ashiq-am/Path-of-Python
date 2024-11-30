# Removing multiple characters using list comprehension

s1 = "Welcome to Python programming!"

# Use a set for faster lookups
ch = {'o', 'm', ' '}

s2 = "".join([c for c in s1 if c not in ch])
print(s2)