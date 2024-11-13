from collections import Counter

# Sample data
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Create a Counter object
counter = Counter(data)

# elements according to the frequency in decreasing order
most_common_elements = counter.most_common()

print(most_common_elements)
