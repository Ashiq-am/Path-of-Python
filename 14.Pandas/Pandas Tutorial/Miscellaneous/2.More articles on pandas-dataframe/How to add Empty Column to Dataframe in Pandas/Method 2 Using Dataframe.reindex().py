# import pandas library
import pandas as pd

# create a dataframe
Mydataframe = pd.DataFrame({'FirstName': ['Preetika',
										'Tanya',
										'Akshita'],
							"Age": [25,21,22]})
# show the dataframe
print("---Original Dataframe---\n",
	Mydataframe)

# add an empty columns
Mydataframe = Mydataframe.reindex(columns = Mydataframe.columns.tolist()
								+ ['Gender','Roll Number'])

# show the dataframe
print("\n\n---Updated Dataframe---\n",
	Mydataframe)
