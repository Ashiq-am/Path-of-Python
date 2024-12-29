import pandas as pd

# Sample flower data
data = {

    'color': ['Red', 'Yellow', 'White', 'Yellow'],

    'bloom_season': ['Spring', 'Spring', 'Summer', 'Summer']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Iterate over rows using itertuples (with plain tuple, no namedtuples)
for row in df.itertuples(name=None):  # `name=None` ensures plain tuple instead of namedtuple
    print(f"Index: {row[0]}, Color:{row[1]}, Bloom Season: {row[2]}")