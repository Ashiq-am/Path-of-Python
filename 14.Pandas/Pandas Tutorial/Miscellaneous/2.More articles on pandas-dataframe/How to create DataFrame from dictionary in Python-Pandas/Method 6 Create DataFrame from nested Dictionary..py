# import pandas library
import pandas as pd

# dictionary with dictionary object
# in values i.e. nested dictionary
details = {
	0 : {
		'Name' : 'Ankit',
		'Age' : 22,
		'University' : 'BHU'
		},
	1 : {
		'Name' : 'Aishwarya',
		'Age' : 21,
		'University' : 'JNU'
		},
	2 : {
		'Name' : 'Shaurya',
		'Age' : 23,
		'University' : 'DU'
		}
}

# creating a Dataframe object
# from nested dictionary
# in which inside dictionary
# key is act as index value
# and column value is 0, 1, 2...
df = pd.DataFrame(details)

# swap the columns with indexes
df = df.transpose()

df
