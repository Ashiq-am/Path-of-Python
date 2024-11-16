# importing pandas as pd
import pandas as pd

# creating a dictionary
dict = {'Name':["John Smith", "Mark Wellington",
				"Rosie Bates", "Emily Edward"]}

# converting the dictionary to a dataframe
df = pd.DataFrame.from_dict(dict)

# storing lastname of each person
df['LastName'] = df.Name.str.extract(r'\b(\w+)$',
									expand = True)

df



"""
In this example we ll store last name of each person in LastName column

"""
