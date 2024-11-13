from collections import Counter

# Sample text
text = "Ram and Shyam are friends. Also, Ram and Ghanshyam are college friends. All of them Studies from GeeksforGeeks"

# Get the three most common words
common_words = Counter(text.split()).most_common(3)

print(common_words)
