# importing pandas library
import pandas as pd

# creating dataframe
df = pd.DataFrame({'Apple': [1, 1, 0, 0, 0, 0],
				'Orange': [0, 1, 1, 0, 0, 1],
				'Grapes': [1, 1, 0, 0, 1, 1],
				'Peach': [1, 1, 0, 0, 1, 1],
				'Watermelon': [0, 0, 0, 0, 0, 0],
				'Guava': [1, 0, 0, 0, 0, 0],
				'Mango': [1, 0, 1, 0, 1, 0],
				'Kiwi': [0, 0, 0, 0, 0, 0]})

print("Dataframe before filtering\n")
print(df)

# list of columns to be considered
columns = ['Grapes', 'Guava', 'Peach']

# filtering rows on basis of certain columns
df = df[df[columns].sum(axis=1) > 0]

print("\nDataframe after filtering\n")
print(df)
