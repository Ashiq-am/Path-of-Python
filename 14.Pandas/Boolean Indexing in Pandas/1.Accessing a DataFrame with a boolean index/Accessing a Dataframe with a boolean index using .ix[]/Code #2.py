# importing pandas as pd
import pandas as pd

# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
		'degree': ["MBA", "BCA", "M.Tech", "MBA"],
		'score':[90, 40, 80, 98]}

# creating a dataframe with boolean index
df = pd.DataFrame(dict, index = [True, False, True, False])


# accessing a dataframe using .ix[] function
print(df.ix[1])
