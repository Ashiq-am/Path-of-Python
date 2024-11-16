import pandas as pd

# Sample DataFrame with constant and non-constant columns
data = {
    'A': [1, 1, 1, 1],
    'B': [2, 3, 4, 5],
    'C': ['X', 'X', 'X', 'X'],
    'D': [10, 11, 12, 13]
}

df = pd.DataFrame(data)

# Identify constant columns
constant_columns = [col for col in df.columns if df[col].nunique() == 1]

# Display constant columns
print("Constant columns:", constant_columns)
