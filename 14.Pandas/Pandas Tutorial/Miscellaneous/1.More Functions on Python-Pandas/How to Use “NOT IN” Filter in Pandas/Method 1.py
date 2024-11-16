# import pandas module
import pandas as pd

# create dataframe
data1 = pd.DataFrame({'name': ['sravan', 'harsha', 'jyothika'],
					'subject1': ['python', 'R', 'php'],
					'marks': [96, 89, 90]}, index=[0, 1, 2])

# consider a list
list1 = ['harsha', 'jyothika']

# filter in name column
print(data1[~data1['name'].isin(list1)])
print("============")

# consider a list
list2 = ['R']


# filter in name column
print(data1[~data1['subject1'].isin(list2)])
print("============")

# consider a list
list3 = [96, 89]

# filter in name column
print(data1[~data1['marks'].isin(list3)])
