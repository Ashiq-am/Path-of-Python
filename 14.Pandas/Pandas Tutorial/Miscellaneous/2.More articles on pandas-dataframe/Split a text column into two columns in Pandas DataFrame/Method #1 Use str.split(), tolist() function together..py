# import Pandas as pd
import pandas as pd

# create a new data frame
df = pd.DataFrame({'Name': ['John_Larter', 'Robert_Junior', 'Jonny_Depp'],
					'Age':[32, 34, 36]})

print("Given Dataframe is :\n",df)

print("\nSplitting Name column into two different columns :")
print(pd.DataFrame(df.Name.str.split('_',1).tolist(),
						columns = ['first','Last']))
