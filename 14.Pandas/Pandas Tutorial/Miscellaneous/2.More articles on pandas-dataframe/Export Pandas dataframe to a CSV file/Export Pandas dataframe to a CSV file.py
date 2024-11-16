# importing the module
import pandas as pd

# making the data
scores = {'Name': ['a', 'b', 'c', 'd'],
		'Score': [90, 80, 95, 20]}

# creating the DataFrame
df = pd.DataFrame(scores)

# displaying the DataFrame
print(df)
