# Import the pandas library and alias it as 'pd'
import pandas as pd

# Create a sample DataFrame with two columns, 'Column1'
# and 'Column2', containing Boolean values
data = {'Column1': [True, False, True, False],
		'Column2': [False, True, False, True]}

# Create a DataFrame named 'df' using the provided data
df = pd.DataFrame(data)
print(df,"\n")

# We define a lambda function that converts True to 1 and False
# to 0 and apply it to each column using .apply()
df_apply = df.apply(lambda x: x.apply(lambda y: 1 if y else 0))

# Print the DataFrame 'df_apply' with the mapping applied
# using .apply() and a lambda function
print("\nUsing .apply() method with lambda function:")
print(df_apply)
