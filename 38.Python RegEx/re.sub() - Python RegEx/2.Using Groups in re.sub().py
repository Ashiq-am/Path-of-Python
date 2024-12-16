import re

a = "John 25, Jane 30, Jack 22"

# Match name and age
pattern = r"(\w+) (\d+)"

# Use age first, then name
repl = r"\2 years old, \1"

# Swap names and ages
result = re.sub(pattern, repl, a)

print(result)