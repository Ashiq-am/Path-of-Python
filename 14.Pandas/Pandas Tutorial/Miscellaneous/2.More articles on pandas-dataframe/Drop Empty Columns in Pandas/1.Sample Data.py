# import required libraries
import numpy as np
import pandas as pd

# create a Dataframe
Mydataframe = pd.DataFrame({'FirstName': ['Vipul', 'Ashish', 'Milan'],
							"Gender": ["", "", ""],
							"Age": [0, 0, 0]})
Mydataframe['Department'] = np.nan

# show the dataframe
print(Mydataframe)
