# import Pandas as pd
import pandas as pd

# create a new data frame
df = pd.DataFrame({'Name': ['John_Larter', 'Robert_Junior', 'Jonny_Depp'],
					'Age':[32, 34, 36]})

print("Given Dataframe is :\n",df)

print("\nSplitting Name column into two different columns :")

# splitting 'Name' column into Two columns
# i.e. 'First' and 'Last'respectively and
# Adding these columns to the existing dataframe.
df[['First','Last']] = df.Name.apply(
lambda x: pd.Series(str(x).split("_")))

print(df)
