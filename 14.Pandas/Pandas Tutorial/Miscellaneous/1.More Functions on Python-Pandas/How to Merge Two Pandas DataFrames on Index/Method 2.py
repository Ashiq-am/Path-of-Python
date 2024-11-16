# import pandas module
import pandas as pd

# create student dataframe
data1 = pd.DataFrame({'id': [1, 2, 3, 4],
					'name': ['manoj', 'manoja', 'manoji', 'manij']},
					index=['one', 'two', 'three', 'four'])


# create marks dataframe
data2 = pd.DataFrame({'s_id': [1, 2, 3, 6, 7],
					'marks': [98, 90, 78, 86, 78]},
					index=['one', 'two', 'three', 'siz', 'seven'])

# join two dataframes with merge
print(pd.merge(data1, data2, left_index=True, right_index=True))
