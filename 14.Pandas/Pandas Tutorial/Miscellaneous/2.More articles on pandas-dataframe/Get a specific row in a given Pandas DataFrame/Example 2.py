# importing the module
import pandas as pd

# creating a DataFrame
data = {'Name' : ['Simon', 'Marsh', 'Gaurav',
				'Alex', 'Selena'],
		'Maths' : [8, 5, 6, 9, 7],
		'Science' : [7, 9, 5, 4, 7],
		'English' : [7, 4, 7, 6, 8]}
df = pd.DataFrame(data)
print("Original DataFrame")
display(df)

print("Value of row 3 (Alex)")
display(df.iloc[3])
