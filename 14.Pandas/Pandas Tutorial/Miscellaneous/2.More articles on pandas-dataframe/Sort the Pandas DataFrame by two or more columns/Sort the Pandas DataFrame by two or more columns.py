#import python library
import pandas as pd

# dictionary
data_frame = {
	'name': ['Akash Kumar', 'Diksha Tewari',
				'Bhawna Gourh', 'Ayush Sharma'],
		'age': [20, 21, 22, 23],
		'favorite_color': ['black', 'Yellow',
						'Pink', "Orange"],
		'grade': [88, 92, 95, 70]
}

# create data frame with indexing
df = pd.DataFrame(data_frame,
				index = [1, 2, 3, 4])

# printing the dataframe
df
