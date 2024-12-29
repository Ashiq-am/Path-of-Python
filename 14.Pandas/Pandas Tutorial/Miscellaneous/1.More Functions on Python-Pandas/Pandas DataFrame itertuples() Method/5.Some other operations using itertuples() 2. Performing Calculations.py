import pandas as pd

# Sample data with columns A and B
data = {
    'A': [10, 20, 30, 40, 50],
    'B': [5, 15, 25, 35, 45],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Perform addition using itertuples
print("Sum of A and B for each row:")
for row in df.itertuples(name='Pandas'):  # Using plain tuples
    sum_ab = row.A + row.B  # 'A' is at index 0, 'B' is at index 1
    print(f"Row {row.Index}: {sum_ab}")