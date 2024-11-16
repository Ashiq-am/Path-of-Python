import pandas as pd

# Creating a data frame
df = pd.DataFrame([['Animal', 'Baby', 'Cat', 'Dog',
					'Elephant', 'Frog', 'Gragor']])

# Itering over the data frame rows
# using df.iterrows()
itr = next(df.iterrows())[1]
itr
