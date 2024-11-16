# NO ERROR IS RAISED

# import pandas package
import pandas as pd

# defining a dictionary
d = {"A": [1, 2, 3],
	"B": [4, 5, 6]}

# creating the pandas dataframe
df = pd.DataFrame(d)

# displaying the columns before renaming
print(df.columns)

# renaming the columns
# column "C" is not in
# the original dataframe
# errors parameter is
# set to 'ignore' by default
df.rename(columns = {"A": "a", "B": "b",
					"C": "c"},
		inplace = True)

# displaying the columns
# after renaming
print(df.columns)
