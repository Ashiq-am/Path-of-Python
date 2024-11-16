# import pandas module
import pandas as pd

# create food dataframe
data = pd.DataFrame({'food_id': [1, 2, 3, 4],
					'name': ['idly', 'dosa', 'poori', 'chapathi'],
					'city': ['delhi', 'goa', 'hyd', 'chennai'],
					'cost': [12, 34, 21, 23]})

# exclude name and food_id column
print(data.loc[:, ~data.columns.isin(['name', 'food_id'])])
