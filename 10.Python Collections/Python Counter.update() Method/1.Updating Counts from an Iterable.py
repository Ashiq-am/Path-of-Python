from collections import Counter

# Initial Counter
fruit_counter = Counter({'apple': 2, 'banana': 1})

# Update counts from an iterable
fruits = ['apple', 'banana', 'apple', 'orange', 'apple']
fruit_counter.update(fruits)

print("Updated Counter:", fruit_counter)
