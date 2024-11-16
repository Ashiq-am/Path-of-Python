import pandas as pd

# Data
my_data = {"views": [12, 13, 100, 80, 91],
		"likes": [3, 8, 23, 17, 56]}
my_df = pd.DataFrame(my_data)

# Printing the DataFrame
print(my_df.to_string())

# Printing the number of views greater
# than 30
print("View greater than 30: ",
	sum(my_df.views > 30))
