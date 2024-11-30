a = [1, 2, 3, 4, 5, 2, 6, 3]

# Create a list of duplicates using list comprehension
duplicates = [i for i in set(a) if a.count(i) > 1]
print(duplicates)