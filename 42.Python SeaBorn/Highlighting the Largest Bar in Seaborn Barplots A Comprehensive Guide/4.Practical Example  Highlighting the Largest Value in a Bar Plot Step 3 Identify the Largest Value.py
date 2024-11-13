# Find the index of the largest value
max_index = df['Values'].idxmax()
print(f"Largest value index: {max_index}, value: {df['Values'][max_index]}")
