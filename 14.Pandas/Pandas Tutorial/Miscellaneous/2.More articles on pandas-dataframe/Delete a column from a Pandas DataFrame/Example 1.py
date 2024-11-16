# importing the module
import pandas as pd

# creating a DataFrame
my_df = {'Name': ['Rutuja', 'Anuja'],
		'ID': [1, 2], 'Age': [20, 19]}
df = pd.DataFrame(my_df)
display("Original DataFrame")
display(df)

# deleting a column
del df['Age']

display("DataFrame after deletion")
display(df)
