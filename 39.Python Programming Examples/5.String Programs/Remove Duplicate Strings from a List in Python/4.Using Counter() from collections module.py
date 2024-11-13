from collections import Counter

# Sample list with duplicate strings
original_list = ['apple', 'orange', 'banana', 'apple', 'grape', 'banana']

# Remove duplicates using Counter
unique_list = list(Counter(original_list).keys())

print(unique_list)
