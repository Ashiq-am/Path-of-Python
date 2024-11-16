# Import the pandas library and alias it as 'pd'
import pandas as pd

# Create a sample DataFrame with two columns, 'Column1'
# and 'Column2', containing Boolean values
data = {'Column1': [True, False, True, False],
		'Column2': [False, True, False, True]}

# Create a DataFrame named 'df' using the provided data
df = pd.DataFrame(data)

# Print the original DataFrame 'df' containing Boolean values
print(df,'/n')

# Convert the 'Column1' and 'Column2' columns from
# Boolean (True/False) to integers (1/0)
df['Column1'] = df['Column1'].astype(int)
df['Column2'] = df['Column2'].astype(int)

# Print the updated DataFrame 'df' where Boolean
# values are now represented as integers
print(df)
