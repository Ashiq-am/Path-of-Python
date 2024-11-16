# import pandas libraey
import pandas as pd

# dictionary
dict = {'Name': ['Martha', 'Tim',
				'Rob', 'Georgia'],
		'Marks': [87, 91,
				97, 95]}

# create a dataframe object
df = pd.DataFrame(dict)

# show the dataframe
print(df)

# list of values of 'Marks' column
marks_list = df['Marks'].tolist()

# show the list
print(marks_list)
