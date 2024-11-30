import textwrap

# Truncate using textwrap.shorten
s1 = "Welcome to Python programming!"
s2 = textwrap.shorten(s1, width=15, placeholder="...")
print(s2)