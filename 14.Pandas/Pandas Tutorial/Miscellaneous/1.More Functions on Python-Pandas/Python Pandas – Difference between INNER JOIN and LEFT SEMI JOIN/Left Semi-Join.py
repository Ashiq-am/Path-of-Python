# importing pandas as pds
import pandas as pds

# Creating dataframe for the data_set first
data_Set1 = pds.DataFrame()

# Creating data list for the table 1
schema = {'Id': [101, 102, 106, 112],
	'DATA 1': ['Abhilash', 'Raman', 'Pratap', 'James']}
data_Set1= pds.DataFrame(schema)
print(data_Set1,"\n")

# Creating dataframe data_set second
data_Set2 = pds.DataFrame()

# Creating data list for the table 2
schema2 = {'Id': [101, 102, 109, 208],
	'DATA 2': ['Abhirav', 'Abhigyan', 'John', 'Peter']}
data_Set2= pds.DataFrame(schema2)

print(data_Set2,"\n")

# setting the base for the left semi-join in python
semi=data_Set1.merge(data_Set2,on='Id')
print(semi,"\n")
data_Set1['Id'].isin(data_Set2['Id'])
semi=data_Set1.merge(data_Set2,on='Id')

# our left semi join
new_semi=data_Set1[data_Set1['Id'].isin(semi['Id'])]
pds.DataFrame(new_semi)
