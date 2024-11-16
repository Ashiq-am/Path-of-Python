import pandas as pd
data = {'Name': ['Tani', 'Saumya',
				'Ganesh', 'Kirti'],

		'Articles': [5, 3, 4, 3],

		'Location': ['Kanpur', 'Kolkata',
					'Kolkata', 'Bombay'],
		'Dates': ['2020-08-04', '2020-08-07', '2020-08-08', '2020-06-08']}

# Create DataFrame
df = pd.DataFrame(data)
display(df)
