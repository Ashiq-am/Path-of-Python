import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'bar'] * 3,
    'B': [1, 2, 3, 4, 5, 6],
    'C': [7, 8, 9, 10, 11, 12]
})

# Group by column A
gb = df.groupby('A')

# Iterate over the groups
for name, group in gb:
    print(f"Group: {name}")
    print(group)
    print()
