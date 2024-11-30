from collections import Counter

s = "Geeks for Geeks"
word = s.split()

# Using Counter to count words
count = Counter(word)

print(count)