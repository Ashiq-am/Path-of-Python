import itertools

# Sample data
data = ["apple,orange,banana", "banana,apple", "grape,banana,apple", "orange"]

# Split cells and count unique values
split_values = itertools.chain.from_iterable(cell.split(',') for cell in data)
unique_values = set(split_values)

print(f"Unique values: {unique_values}")
print(f"Count of unique values: {len(unique_values)}")
