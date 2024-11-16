# import pandas library
import pandas as pd

# dictionary with list object in values
details = {
	'Name' : ['Ankit', 'Aishwarya', 'Shaurya',
			'Shivangi', 'Priya', 'Swapnil'],
	'Age' : [23, 21, 22, 21, 24, 25],
	'University' : ['BHU', 'JNU', 'DU', 'BHU',
					'Geu', 'Geu'],
}

# creating a Dataframe object
df = pd.DataFrame(details, columns = ['Name', 'Age',
									'University'],
				index = ['a', 'b', 'c', 'd', 'e',
						'f'])

df
