import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Sub-Category': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Values': [10, 20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

# Group by 'Category' and 'Sub-Category', then sum the 'Values'
grouped = df.groupby(['Category', 'Sub-Category'])['Values'].sum()
print(grouped)
