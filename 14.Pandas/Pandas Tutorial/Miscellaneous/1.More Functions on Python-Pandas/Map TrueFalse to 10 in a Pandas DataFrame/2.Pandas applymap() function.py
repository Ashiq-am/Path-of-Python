# Import the pandas library and alias it as 'pd'
import pandas as pd

# Create a sample DataFrame with two columns,
# 'Column1' and 'Column2', containing Boolean values
data = {'Column1': [True, False, True, False],
		'Column2': [False, True, False, True]}

# Create a DataFrame named 'df' using the provided data
df = pd.DataFrame(data)

# Print the original DataFrame 'df' containing Boolean values
print(df, '\n')

# Use .applymap() with a lambda function to map True/False to 1/0
df = df.applymap(lambda x: 1 if x else 0)

# Print the updated DataFrame 'df' where Boolean
# values are now represented as integers (1/0)
print(df)
