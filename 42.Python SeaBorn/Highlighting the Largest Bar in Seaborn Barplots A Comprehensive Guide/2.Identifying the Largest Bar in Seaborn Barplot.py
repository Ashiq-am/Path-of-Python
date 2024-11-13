import pandas as pd

# Sample data
data = {'Category': ['A', 'B', 'C', 'D'], 'Values': [4, 20, 1, 15]}
df = pd.DataFrame(data)

# Find the index of the largest value
max_index = df['Values'].idxmax()
max_index
