# importing the module
import pandas as pd

# creating a DataFrame
data = {'1' : ['g', 'e', 'e'],
		'2' : ['k', 's', 'f'],
		'3' : ['o', 'r', 'g'],
		'4' : ['e', 'e', 'k']}
df = pd.DataFrame(data)
print("Original DataFrame")
display(df)

print("Value of row 1")
display(df.iloc[1])
