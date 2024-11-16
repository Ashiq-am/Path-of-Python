# import pandas package
import pandas as pd

# defining a dictionary
d = {"Name": ["John", "Mary", "Helen"],
	"Marks": [95, 75, 99],
	"Roll No": [12, 21, 9]}

# creating the pandas dataframe
df = pd.DataFrame(d)

# displaying the columns before renaming
print(df.columns)

# renaming the columns
df.rename({"Name": "Student Name",
		"Marks": "Marks Obtained",
		"Roll No": "Roll Number"},
		axis = "columns", inplace = True)

# displaying the columns after renaming
print(df.columns)
