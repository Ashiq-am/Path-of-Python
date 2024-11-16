# import pandas module
import pandas as pd

# create student daatframe with 3 columns
# and 4 rows
data = pd.DataFrame({'id': [1, 2, 3, 4],
					'name': ['sai', 'navya', 'reema', 'thanuja'],
					'age': [21, 22, 21, 22]})


# drop first row
data.drop(index=0)
