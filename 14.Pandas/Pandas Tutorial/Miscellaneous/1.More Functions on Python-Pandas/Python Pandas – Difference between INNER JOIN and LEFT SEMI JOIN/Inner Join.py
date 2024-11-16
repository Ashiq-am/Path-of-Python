# importing pandas as pds
import pandas as pds

# Creating dataframe for the data_set first
data_Set1 = pds.DataFrame()

# Creating data list for the table 1
# here Id 101 and 102 will be same like
# in data set 2
schema = {'Id': [101, 102, 106, 112],
		'DATA 1': ['Abhilash', 'Raman', 'Pratap', 'James']}
data_Set1 = pds.DataFrame(schema)

print("Data Set-1 \n", data_Set1, "\n")

# Creating dataframe data_set second
data_Set2 = pds.DataFrame()

# Creating data list for the table 2
# here Id 101 and 102 will be same like
# in data set 1
schema = {'Id': [101, 102, 109, 208],
		'DATA 2': ['Abhirav', 'Abhigyan', 'John', 'Peter']}
data_Set2 = pds.DataFrame(schema)

print("Data Set-2 \n", data_Set2, "\n")

# inner join in python
inner_join = pds.merge(data_Set1, data_Set2, on='Id', how='inner')

# display dataframe
pds.DataFrame(inner_join)
