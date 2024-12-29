import pandas as pd

# Sample flower data
data = {
    'name': ['Rose', 'Tulip', 'Daisy'],
    'color': ['Red', 'Yellow', 'White'],

}

# Create a DataFrame
df = pd.DataFrame(data)

# Iterate over rows using itertuples
for row in df.itertuples():
    print(f"Flower: {row.name}, Color: {row.color}")