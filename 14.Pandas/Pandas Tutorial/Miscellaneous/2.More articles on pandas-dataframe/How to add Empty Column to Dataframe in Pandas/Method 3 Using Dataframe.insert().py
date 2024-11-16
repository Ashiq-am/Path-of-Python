# import pandas library
import pandas as pd

# create a dataframe
Mydataframe = pd.DataFrame({'FirstName': ['Rohan',
										'Martin',
										'Mary'],
							"Age": [28,39,21]})
# show the dataframe
print("---Original Dataframe---\n",
	Mydataframe)

# add an empty column
Mydataframe.insert(0,'Roll Number','')

# show the dataframe
print("\n\n---Updated Dataframe---\n",
	Mydataframe)
