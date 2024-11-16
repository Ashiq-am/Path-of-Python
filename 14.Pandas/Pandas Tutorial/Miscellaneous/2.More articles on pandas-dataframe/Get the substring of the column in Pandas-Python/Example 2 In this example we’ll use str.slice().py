# importing pandas as pd
import pandas as pd

# creating a dictionary
dict = {'Name':["John Smith", "Mark Wellington",
				"Rosie Bates", "Emily Edward"]}

# converting the dictionary to a
# dataframe
df = pd.DataFrame.from_dict(dict)

# storing first 3 letters of name as username
df['UserName'] = df['Name'].str.slice(0, 3)

df
