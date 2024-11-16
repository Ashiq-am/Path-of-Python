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

# filtering on the basis of rows
df = df[df.sum(axis=1) > 0]

# filtering on the basis of columns
df = df.loc[:, df.sum(axis=0) > 0]

print("\nDataframe after filtering\n")
print(df)
