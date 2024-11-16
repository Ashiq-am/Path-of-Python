# importing pandas as pd
import pandas as pd

# Creating a dict of lists
data = {'name':["Akash", "Geeku", "Pankaj", "Sumitra", "Ramlal"],
	'Branch':["B.Tech", "MBA", "BCA", "B.Tech", "BCA"],
	'Score':["80", "90", "60", "30", "50"],
	'Result': ["Pass", "Pass", "Pass", "Fail", "Fail"]}

df = pd.DataFrame(data)

# pivoting the dataframe
df.pivot(index ='Result', columns ='name')

df
