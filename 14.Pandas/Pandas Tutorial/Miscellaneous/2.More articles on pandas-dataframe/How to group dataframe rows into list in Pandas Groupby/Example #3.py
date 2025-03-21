# importing pandas as pd
import pandas as pd


# Create the data frame
df = pd.DataFrame({'column1': ['A', 'B', 'C', 'A', 'C',
							'C', 'B', 'D', 'D', 'A'],
				'column2': [5, 10, 15, 20, 25, 30,
							35, 40, 45, 50]})

# Use groupby method and agg method
# with list as argument on the dataframe
df = df.groupby('column1').agg(list)

df
