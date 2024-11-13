from collections import Counter

# Initial Counters
counter1 = Counter({'a': 3, 'b': 2})
counter2 = Counter({'a': 1, 'b': 4, 'c': 2})

# Combine counters
counter1.update(counter2)

print("Combined Counter:", counter1)
