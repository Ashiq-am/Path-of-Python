# Import the pandas library and alias it as 'pd'
import pandas as pd

# Create a sample DataFrame with two columns, 'Column1' and
# 'Column2', containing Boolean values
data = {'Column1': [True, False, True, False],
		'Column2': [False, True, False, True]}

# Create a DataFrame named 'df' using the provided data
df = pd.DataFrame(data)
print(df,"\n")

# We use .map() on a specific column and provide a dictionary to perform the mapping
df['Column1'] = df['Column1'].map({True: 1, False: 0})

# Print the updated 'Column1' in the original DataFrame
# 'df' where Boolean values are mapped to integers
print("\nUsing .map() method for 'Column1':")
print(df)
