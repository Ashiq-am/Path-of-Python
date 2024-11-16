# import pandas module
import numpy as np
import pandas as pd

# create dataframe
data1 = pd.DataFrame({'name': ['sravan', 'harsha', 'jyothika'],
					'subject1': ['python', 'R', 'php'],
					'marks': [96, 89, 90]}, index=[0, 1, 2])

# consider a list
list1 = ['harsha', 'jyothika', 96]

# filter in name column
data1[~np.isin(data1['name'], list1)]
