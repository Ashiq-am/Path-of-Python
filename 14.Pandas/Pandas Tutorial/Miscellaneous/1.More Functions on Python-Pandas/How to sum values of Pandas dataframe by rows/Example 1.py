# importing pandas module as pd
import pandas as pd

# creating a dataframe using dictionary
df = pd.DataFrame({'X':[1, 2, 3, 4, 5],
				'Y':[54, 12, 57, 48, 96]})

# sum() method sums up the rows and columns of a dataframe
# axis = 1 sums up the rows
df = df.sum(axis = 1)
print(df)
