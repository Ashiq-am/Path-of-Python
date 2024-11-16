# importing pandas as pd
import pandas as pd

# Creating a dict of lists
data = {'Name':["Akash", "Geeku", "Pankaj", "Sumitra","Ramlal"],
	'Branch':["B.Tech", "MBA", "BCA", "B.Tech", "BCA"],
	'Score':["80","90","60", "30", "50"],
	'Result': ["Pass","Pass","Pass","Fail","Fail"]}

# Creating a dataframe
df = pd.DataFrame(data)

# Using set_index() method on 'Name' column
df = df.set_index('Name')

df
