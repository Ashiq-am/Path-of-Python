# Python code to map Boolean values to integer using .replace() method
import pandas as pd

# Create a sample DataFrame with two columns, 'Column1'
# and 'Column2', containing Boolean values
data = {'Column1': [True, False, True, False],
		'Column2': [False, True, False, True]}

# Create a DataFrame named 'df' using the provided data
df = pd.DataFrame(data)

# Print the original DataFrame 'df' containing Boolean values
print(df, '\n')

# Use the .replace() method to map True/False to 1/0
df = df.replace({True: 1, False: 0})

# Print the updated DataFrame 'df' where Boolean values
# are now represented as integers (1/0)
print(df)
