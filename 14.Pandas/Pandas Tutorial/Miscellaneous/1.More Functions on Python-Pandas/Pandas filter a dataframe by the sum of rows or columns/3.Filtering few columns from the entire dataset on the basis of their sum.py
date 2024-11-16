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
columns = ['Apple', 'Mango', 'Guava', 'Watermelon']

# iterating through the columns and dropping
# columns with sum less than equals to 0
for column in columns:
	if (df[column].sum() <= 0):
		df.drop(column, inplace=True, axis=1)

print("\nDataframe after filtering\n")
print(df)
