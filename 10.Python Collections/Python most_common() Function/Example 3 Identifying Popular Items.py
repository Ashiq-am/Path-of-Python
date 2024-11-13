from collections import Counter

# Sample data
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Get the most common item and its count
popular_item = Counter(items).most_common(1)

print(popular_item)
