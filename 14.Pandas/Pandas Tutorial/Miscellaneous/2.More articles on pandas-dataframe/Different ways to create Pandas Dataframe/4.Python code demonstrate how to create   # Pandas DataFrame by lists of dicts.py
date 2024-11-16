# Python code demonstrate how to create
# Pandas DataFrame by lists of dicts.
import pandas as pd

# Initialise data to lists.
data = [{'a': 1, 'b': 2, 'c':3}, {'a':10, 'b': 20, 'c': 30}]

# Creates DataFrame.
df = pd.DataFrame(data)

# Print the data
df
