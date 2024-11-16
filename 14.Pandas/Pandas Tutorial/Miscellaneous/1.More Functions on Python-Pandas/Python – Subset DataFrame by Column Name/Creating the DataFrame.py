#import pandas
import pandas as pd

# create dataframe
data = {'Name': ['John', 'Emily', 'Lara', 'Lucas', 'Katy', 'Jordan'],
		'Gender': [30, 27, 21, 21, 16, 20],
		'Branch': ['Arts', 'Arts', 'Commerce', 'Science',
				'Science', 'Science'],
		'pre_1': [9, 9, 10, 7, 6, 9],
		'pre_2': [8, 7, 10, 6, 8, 8]}

df = pd.DataFrame(data)
df
