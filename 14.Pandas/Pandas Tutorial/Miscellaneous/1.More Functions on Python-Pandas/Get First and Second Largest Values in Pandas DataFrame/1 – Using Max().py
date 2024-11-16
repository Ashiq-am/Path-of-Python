import pandas as pd

# Sample DataFrame
data = {'Scores': [85, 92, 75, 91, 88]}
df = pd.DataFrame(data)

# Get the highest value
highest_value = df['Scores'].max()
print("Highest Value:", highest_value)
