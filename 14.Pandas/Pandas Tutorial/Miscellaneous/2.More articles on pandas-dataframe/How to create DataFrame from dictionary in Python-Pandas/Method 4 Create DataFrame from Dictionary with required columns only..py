# import pandas library
import pandas as pd

# dictionary with list object in values
details = {
	'Name' : ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
	'Age' : [23, 21, 22, 21],
	'University' : ['BHU', 'JNU', 'DU', 'BHU'],
}

# creating a Dataframe object with skipping
# one column i.e skipping age column.
df = pd.DataFrame(details, columns = ['Name', 'University'])

df
