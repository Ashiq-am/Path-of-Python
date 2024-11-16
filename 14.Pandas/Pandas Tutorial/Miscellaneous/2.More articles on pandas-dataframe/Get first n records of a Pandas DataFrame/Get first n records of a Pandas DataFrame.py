# Import Required Library
import pandas as pd

# Create a dictionary for the dataframe
dict = {'Name' : ['Sumit Tyagi', 'Sukritin',
				'Akriti Goel', 'Sanskriti',
				'Abhishek Jain'],
		'Age':[22, 20, 45, 21, 22],
		'Marks':[90, 84, 33, 87, 82]}

# Converting Dictionary to Pandas Dataframe
df = pd.DataFrame(dict)

# Print Dataframe
print(df)
