import re

# Using regular expressions to remove a substring
s = "Hello, world! Hello, Python!"

sub = re.sub(r"Hello, ", "", s)
print(sub)