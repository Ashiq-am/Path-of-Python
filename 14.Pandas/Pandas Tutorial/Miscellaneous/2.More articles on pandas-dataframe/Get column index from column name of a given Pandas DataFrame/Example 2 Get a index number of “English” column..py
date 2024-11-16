# import pandas library
import pandas as pd

# dictionary
record = {'Math': [10, 20, 30,
				40, 70],
		'Science': [40, 50, 60,
					90, 50],
		'English': [70, 80, 66,
					75, 88]}

# create a dataframe
df = pd.DataFrame(record)

# give column name
col_name = "English"

# find the index no
index_no = df.columns.get_loc(col_name)

print("Index of {} column in given dataframe is : {}".format(col_name, index_no))
