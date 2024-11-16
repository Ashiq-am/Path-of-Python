# import Pandas library
import pandas as pd

# create dataframe with a column (names) having list-like elements
data = {'id': [1, 2, 3],
		'names': ["Tom,Rick,Hardy", "Ritu,Shalini,Anjana", "Ali,Amir"]}

df = pd.DataFrame(data)

print(df)
