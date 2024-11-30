from collections import Counter

a = [1, 2, 3, 4, 5, 2, 6, 3]

# Use Counter to count
#the occurrences of each element in the list
counts = Counter(a)
duplicates = [item for item, count in counts.items() if count > 1]
print(duplicates)