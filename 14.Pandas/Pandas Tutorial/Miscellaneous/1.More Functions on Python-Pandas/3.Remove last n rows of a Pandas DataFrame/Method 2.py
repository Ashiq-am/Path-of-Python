# Import Required Libraries
import pandas as pd

# Create a dictionary for the dataframe
dict = {
'Name': ['Sukritin', 'Sumit Tyagi', 'Akriti Goel',
		'Sanskriti', 'Abhishek Jain'],
'Age': [22, 20, 45, 21, 22],
'Marks': [90, 84, -33, -87, 82]
}

# Converting Dictionary to
# Pandas Dataframe
df = pd.DataFrame(dict)

# Number of rows to drop
n = 3

# Removing last n rows
df_dropped_last_n = df.iloc[:-n]

# Printing dataframe
print(df_dropped_last_n)
