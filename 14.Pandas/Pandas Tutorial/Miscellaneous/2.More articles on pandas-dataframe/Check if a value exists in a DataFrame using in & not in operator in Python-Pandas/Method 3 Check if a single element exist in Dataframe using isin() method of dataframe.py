# import pandas library
import pandas as pd

# dictionary with list object in values
details = {
	'Name' : ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi', 'Priya', 'Swapnil'],
	'Age' : [23, 21, 22, 21, 24, 25],
	'University' : ['BHU', 'JNU', 'DU', 'BHU', 'Geu', 'Geu'],
}

# creating a Dataframe object
df = pd.DataFrame(details, columns = ['Name', 'Age', 'University'],
				index = ['a', 'b', 'c', 'd', 'e', 'f'])

print("Dataframe: \n\n", df)

# isin() methods return Boolean
# Dataframe of given Dimension
# first any() will return boolean series
# and 2nd any() will return single bool value
res = df.isin(['Ankit']).any().any()

if res :
	print("\nThis value exists in Dataframe")

else :
	print("\nThis value does not exists in Dataframe")
