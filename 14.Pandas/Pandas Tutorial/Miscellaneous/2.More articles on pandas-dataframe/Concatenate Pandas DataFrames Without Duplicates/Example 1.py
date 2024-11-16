# Importing pandas library
import pandas as pd

# loading dataframes
dataframe1 = pd.DataFrame({'columnA': [20, 30, 40],
						'columnB': [200, 300, 400]})

dataframe2 = pd.DataFrame({'columnA': [50, 20, 60],
						'columnB': [500, 200, 600]})

# Concatenating dataframes without duplicates
new_dataframe = pd.concat([dataframe1, dataframe2]).drop_duplicates()

# Display concatenated dataframe
new_dataframe
