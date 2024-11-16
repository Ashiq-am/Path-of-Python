# import pandas library
import pandas as pd

# dictionary with list object in values
details = {
	'Name' : ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
	'Age' : [23, 21, 22, 21],
	'University' : ['BHU', 'JNU', 'DU', 'BHU'],
}

# creating a Dataframe object
df = pd.DataFrame(details, columns = ['Name', 'Age', 'University'],
				index = ['a', 'b', 'c', 'd'])

# droppping a row 'c' & 'd' from actual dataframe
df.drop(['c', 'd'], inplace = True )

df
