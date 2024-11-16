# import required libraries
import numpy as np
import pandas as pd

# create a Dataframe
Mydataframe = pd.DataFrame({'FirstName': ['Vipul',
										'Ashish',
										'Milan'],
							"Age": [21,22,23]})
# show the dataframe
print("\n\n---Original Dataframe---\n",
	Mydataframe)

# add an empty columns
Mydataframe['Gender'] = ''
Mydataframe['Department'] = np.nan

# show the dataframe
print("---Updated Dataframe---\n",
	Mydataframe)
