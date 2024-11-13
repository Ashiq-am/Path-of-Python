# Sample data
data = ["apple,orange,banana", "banana,apple", "grape,banana,apple", "orange"]

# Split cells and count unique values
unique_values = set()
for cell in data:
    values = cell.split(',')
    unique_values.update(values)

print(f"Unique values: {unique_values}")
print(f"Count of unique values: {len(unique_values)}")
