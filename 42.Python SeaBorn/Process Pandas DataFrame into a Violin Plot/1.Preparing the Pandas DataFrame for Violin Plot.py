import pandas as pd

# Expanded DataFrame with more complex numerical and categorical data
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D'],
    'Subgroup': ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z'],
    'Values': [10, 12, 15, 20, 22, 19, 25, 27, 30, 35, 37, 33],
    'Scores': [75, 88, 92, 65, 78, 80, 83, 95, 90, 50, 68, 55],
    'Age': [21, 24, 22, 35, 32, 30, 27, 28, 29, 41, 39, 42]
}

df = pd.DataFrame(data)
print(df)
