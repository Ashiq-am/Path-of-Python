# import pandas package
import pandas as pd

# defining a dictionary
d = {"Name": ["John", "Mary", "Helen"],
	"Marks": [95, 75, 99],
	"Roll No": [12, 21, 9]}

# creating the pandas data frame
df = pd.DataFrame(d)

# displaying the columns
# before renaming
print(df.columns)

# renaming the column "A"
df.rename(columns = {"Name": "Names"},
		inplace = True)

# displaying the columns after renaming
print(df.columns)
