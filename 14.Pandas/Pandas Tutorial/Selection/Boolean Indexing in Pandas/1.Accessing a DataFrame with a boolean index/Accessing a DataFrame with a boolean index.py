# importing pandas as pd
import pandas as pd

# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
		'degree': ["MBA", "BCA", "M.Tech", "MBA"],
		'score':[90, 40, 80, 98]}

df = pd.DataFrame(dict, index = [True, False, True, False])

print(df)




"""
In order to access a dataframe with a boolean index, 
we have to create a dataframe in which index of dataframe contains 
a boolean value that is “True” or “False”

"""
