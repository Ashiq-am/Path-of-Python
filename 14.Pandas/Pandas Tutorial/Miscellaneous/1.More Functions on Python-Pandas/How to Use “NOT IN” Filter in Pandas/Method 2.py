# import pandas module
import pandas as pd

# create dataframe
data1 = pd.DataFrame({'name': ['sravan', 'harsha', 'jyothika'],
					'subject1': ['python', 'R', 'php'],
					'marks': [96, 89, 90]}, index=[0, 1, 2])

# consider a list
list1 = ['harsha', 'jyothika', 96]

# filter in name and marks column
print(data1[~data1[['name', 'marks']].isin(list1).any(axis=1)])
print("============")

# consider a list
list2 = ['R', 'sravan']

# filter in name and subject1 column
print(data1[~data1[['subject1', 'name']].isin(list2).any(axis=1)])
