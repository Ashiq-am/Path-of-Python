import pandas as pd

# Sample data
data = {
    'fruits': ["apple,orange,banana", "banana,apple", "grape,banana,apple", "orange"]
}

df = pd.DataFrame(data)

# Split cells and count unique values
unique_values = set()
for values in df['fruits'].str.split(','):
    unique_values.update(values)

print(f"Unique values: {unique_values}")
print(f"Count of unique values: {len(unique_values)}")
