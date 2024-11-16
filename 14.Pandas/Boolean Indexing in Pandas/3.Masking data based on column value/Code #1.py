# importing pandas as pd
import pandas as pd

# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
		'degree': ["BCA", "BCA", "M.Tech", "BCA"],
		'score':[90, 40, 80, 98]}

# creating a dataframe
df = pd.DataFrame(dict)

# using a comparsion operator for filtering of data
print(df['degree'] == 'BCA')
