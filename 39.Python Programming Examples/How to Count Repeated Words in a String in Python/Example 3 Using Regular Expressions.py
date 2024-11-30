import re
from collections import Counter

# Using regular expressions to count words
s = "Python is great. Python is fun!"

# Extract words and convert to lowercase
word = re.findall(r'\b\w+\b', s.lower())
count = Counter(word)

print(count)