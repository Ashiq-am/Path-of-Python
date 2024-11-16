# importing pandas as pd
import pandas as pd

# creating a dictionary
dict = {'Name':["John Smith", "Mark Wellington",
				"Rosie Bates", "Emily Edward"]}

# converting the dictionary to a
# dataframe
df = pd.DataFrame.from_dict(dict)

# storing first 3 letters of name
for i in range(0, len(df)):
	df.iloc[i].Name = df.iloc[i].Name[:3]

df
