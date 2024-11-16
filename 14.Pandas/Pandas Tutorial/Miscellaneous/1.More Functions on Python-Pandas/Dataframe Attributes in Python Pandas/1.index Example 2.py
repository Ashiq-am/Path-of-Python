# Python program to implement
# index attribute in a dataframe object
import pandas as pd

# creating a 2D dictionary
dict = {"Student": ["Arnav", "Neha",
					"Priya", "Rahul"],
		"Marks": [85, 92, 78, 83],
		"Sports": ["Cricket", "Volleyball",
				"Hockey", "Badminton"]}

# creating a DataFrame
df = pd.DataFrame(dict, index=['I', 'II', 'III', 'IV'])

# printing this DataFrame on the
# output screen
display(df)

# Implementing index attribute on
# this DataFrame
print(df.index)
