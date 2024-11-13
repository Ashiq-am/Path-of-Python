from collections import Counter

# Sample string
string = "abracadabra"

# Get the most common character and its count
common_char = Counter(string).most_common(1)

print(common_char)
