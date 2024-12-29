import pandas as pd

# Sample data
data = {
    'Group': ['A', 'B', 'A', 'B', 'A', 'C'],
    'Value': [10, 20, 30, 40, 50, 60]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group data by the 'Group' column and calculate the sum of 'Value'
grouped_data = {}

for row in df.itertuples(name=None):  # Use plain tuples
    group = row[1]  # 'Group' column at index 1
    value = row[2]  # 'Value' column at index 2

    # Aggregate the values by group
    if group not in grouped_data:
        grouped_data[group] = 0
    grouped_data[group] += value

# Print the grouped results
for group, total in grouped_data.items():
    print(f"Group: {group}, Total Value: {total}")