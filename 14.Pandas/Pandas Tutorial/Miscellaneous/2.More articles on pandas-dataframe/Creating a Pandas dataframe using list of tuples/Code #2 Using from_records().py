import pandas as pd

# data in the form of list of tuples
data = [('Peter', 18, 7),
		('Riff', 15, 6),
		('John', 17, 8),
		('Michel', 18, 7),
		('Sheli', 17, 5) ]


# create DataFrame using data
df = pd.DataFrame.from_records(data, columns =['Team', 'Age', 'Score'])

print(df)
