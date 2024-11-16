# import Pandas as pd
import pandas as pd

# create a new data frame
df = pd.DataFrame({'Name': ['John_Larter', 'Robert_Junior', 'Jonny_Depp'],
					'Age':[32, 34, 36]})

print("Given Dataframe is :\n",df)

# Adding two new columns to the existing dataframe.
# splitting is done on the basis of underscore.
df[['First','Last']] = df.Name.str.split("_",expand=True)

print("\n After adding two new columns : \n",df)
