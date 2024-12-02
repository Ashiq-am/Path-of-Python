from collections import Counter

s = "GeeksforGeeks"

# Create a Counter object to count occurrences
# of each character in string
d = Counter(s)

# Create a list of characters that occur more than once
res = [c for c, cnt in d.items() if cnt > 1]

print(res)