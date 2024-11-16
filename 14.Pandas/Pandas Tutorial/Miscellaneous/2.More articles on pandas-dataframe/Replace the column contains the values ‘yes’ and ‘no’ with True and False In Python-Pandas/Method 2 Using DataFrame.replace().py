# import pandas library
import pandas as pd

# load csv file
df = pd.read_csv("supermarkets.csv")

# replace the ‘commissioned' column
# contains the values 'yes' and 'no'
# with True and False:
df = df.replace({'commissioned': {'yes': True,
								'no': False}})

# show the dataframe
df
