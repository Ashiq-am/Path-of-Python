# Python code demonstrate to create
# Pandas DataFrame by passing lists of
# Dictionaries and row indices.
import pandas as pd

# Intitialise data of lists
data = [{'b': 2, 'c':3}, {'a': 10, 'b': 20, 'c': 30}]

# Creates padas DataFrame by passing
# Lists of dictionaries and row index.
df = pd.DataFrame(data, index =['first', 'second'])

# Print the data
df
