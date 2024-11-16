import pandas as pd


df = pd.DataFrame({'Roll Number': ['20CSE29', '20CSE49', '20CSE36', '20CSE44'],
				'Name': ['Amelia', 'Sam', 'Dean', 'Jessica'],
				'Marks In Percentage': [97, 90, 70, 82],
				'Grade': ['A', 'A', 'C', 'B'],
				'Subject': ['Physics', 'Physics', 'Physics', 'Physics']})

# Printing the dataframe
df['index'] = df.index
df
