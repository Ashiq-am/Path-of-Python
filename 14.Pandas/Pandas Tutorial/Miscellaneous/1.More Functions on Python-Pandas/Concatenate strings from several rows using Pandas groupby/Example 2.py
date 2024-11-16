# import pandas library
import pandas as pd

# read a csv file
df = pd.read_csv("Book1.csv")

# concatenate the string
df['branch'] = df.groupby(['Name', 'year'])['branch'].transform(
											lambda x: ' '.join(x))

# drop duplicate data
df = df.drop_duplicates()

# show the dataframe
df
