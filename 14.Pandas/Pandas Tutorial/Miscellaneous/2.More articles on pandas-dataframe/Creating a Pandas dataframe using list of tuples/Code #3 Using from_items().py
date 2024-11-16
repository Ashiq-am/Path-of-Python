import pandas as pd

# data in the form of list of tuples
data = [
('Age', [18, 15, 17, 18, 17]),
('Team', ['A', 'B', 'A', 'C', 'B']),
('Score', [7, 6, 8, 7, 5]),
]

# create DataFrame using data
df = pd.DataFrame.from_items(data)

print(df)
