# import required libraries
import numpy as np
import pandas as pd

# create a Dataframe
Mydataframe = pd.DataFrame({'FirstName': ['Vipul', 'Ashish', 'Milan'],
							"Gender": ["", "", ""],
							"Age": [0, 0, 0]})

Mydataframe['Department'] = np.nan
display(Mydataframe)

nan_value = float("NaN")
Mydataframe.replace("", nan_value, inplace=True)

Mydataframe.dropna(how='all', axis=1, inplace=True)

# show the dataframe
display(Mydataframe)
