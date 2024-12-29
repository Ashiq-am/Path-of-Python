import pandas as pd

# Sample fruit data
data = {
    'name': ['Apple', 'Banana', 'Cherry'],
    'color': ['Red', 'Yellow', 'Red'],
    'price': [1.2, 0.5, 2.5]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Iterate over rows using itertuples
for row in df.itertuples(index=False):
    print(row)