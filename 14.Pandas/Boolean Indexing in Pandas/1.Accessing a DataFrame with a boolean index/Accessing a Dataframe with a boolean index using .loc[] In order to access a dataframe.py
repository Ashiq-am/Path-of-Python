'''
with a boolean index using .loc[], we simply pass a boolean value
(True or False) in a .loc[] function.

'''


# importing pandas as pd
import pandas as pd

# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
		'degree': ["MBA", "BCA", "M.Tech", "MBA"],
		'score':[90, 40, 80, 98]}

# creating a dataframe with boolean index
df = pd.DataFrame(dict, index = [True, False, True, False])

# accessing a dataframe using .loc[] function
print(df.loc[True])
