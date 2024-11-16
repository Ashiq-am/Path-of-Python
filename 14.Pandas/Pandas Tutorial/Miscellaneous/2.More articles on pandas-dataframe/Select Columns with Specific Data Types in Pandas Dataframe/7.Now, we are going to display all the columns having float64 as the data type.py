# import required module
import pandas as pd
from vega_datasets import data

# assign dataset
df = data.seattle_weather()

# display description
# of dataset
df.info()

# store columns with specific data type
columns = df.select_dtypes(include=['float64']).columns

# display columns
print('\nColumns:\n', columns)
