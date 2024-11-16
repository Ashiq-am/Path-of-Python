def ProjectPro_Ex_136():

	print()
	print('**How we can do string munging in Pandas**')

	# loading libraries
	import pandas as pd
	import numpy as np
	import re as re

	# Creating dataframe
	raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
				'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
				'email': ['jas203@gmail.com', 'momomolly@gmail.com', np.NAN,
						'battler@milner.com', 'Ames1234@yahoo.com']}

	df = pd.DataFrame(raw_data, columns=['first_name', 'last_name', 'email'])
	print()
	print(df)

	# Let us find Which string within the
	# email column contains ‘gmail’
	print()
	print(df['email'].str.contains('gmail'))

	# Create a daily expression pattern that
	# breaks apart emails
	pattern = '([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.([A-Z]{2,4})'

	# Find everything in df.email that contains
	# that pattern
	print()
	print(df['email'].str.findall(pattern, flags=re.IGNORECASE))


ProjectPro_Ex_136()
