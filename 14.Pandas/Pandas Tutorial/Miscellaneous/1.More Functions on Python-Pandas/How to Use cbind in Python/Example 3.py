# import pandas module
import pandas as pd

# create dataframe
data1 = pd.DataFrame({'name': ['sravan', 'harsha', 'jyothika'],
					'subject1': ['python', 'R', 'php'],
					'marks': [96, 89, 90]}, index=[0, 1, 2])


# create dataframe
data2 = pd.DataFrame({'name': ['sravan', 'harsha', 'jyothika'],
					'subject2': ['html', '.net', 'jsp'],
					'marks': [89, 79, 80]}, index=[3, 4, 5])

# remove dataframe 1 indices
data1.reset_index(drop=True, inplace=True)

# remove dataframe 2 indices
data2.reset_index(drop=True, inplace=True)

# concat dataframes
pd.concat([data1, data2], axis=1)
