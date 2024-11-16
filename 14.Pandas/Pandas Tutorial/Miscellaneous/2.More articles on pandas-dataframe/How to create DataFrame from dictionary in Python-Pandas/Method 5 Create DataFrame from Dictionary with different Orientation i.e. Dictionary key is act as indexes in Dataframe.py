# import pandas library
import pandas as pd

# dictionary with list object in values
details = {
	'Name' : ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
	'Age' : [23, 21, 22, 21],
	'University' : ['BHU', 'JNU', 'DU', 'BHU'],
}

# creating a Dataframe object in which dictionary
# key is act as index value and column value is
# 0, 1, 2...
df = pd.DataFrame.from_dict(details, orient = 'index')

df
