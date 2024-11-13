from collections import Counter

# Initial Counter
word_counter = Counter({'apple': 2, 'banana': 1})

# Update counts from a generator expression
words = ('apple', 'banana', 'apple', 'orange', 'apple')
word_counter.update((word.lower() for word in words))

print("Updated Counter:", word_counter)
