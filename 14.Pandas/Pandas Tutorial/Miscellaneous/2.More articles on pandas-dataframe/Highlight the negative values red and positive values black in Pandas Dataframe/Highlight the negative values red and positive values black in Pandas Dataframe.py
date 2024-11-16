# Import Required Libraries
import pandas as pd
import numpy as np


# Create a dictionary for the dataframe
dict = {
'Name': ['Sukritin', 'Sumit Tyagi',
		'Akriti Goel', 'Sanskriti',
		'Abhishek Jain'],
'Age': [22, 20, 45, 21, 22],
'Marks': [90, 84, -33, -87, 82]
}

# Converting Dictionary to
# Pandas Dataframe
df = pd.DataFrame(dict)

# Print Dataframe
print(df)
