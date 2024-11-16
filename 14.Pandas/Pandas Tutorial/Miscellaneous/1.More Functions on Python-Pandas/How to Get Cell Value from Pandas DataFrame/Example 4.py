# import pandas module
import pandas as pd

# create dataframe with 3 columns
data = pd.DataFrame({
	"id": [7058, 7059, 7072, 7054],
	"name": ['sravan', 'jyothika', 'harsha', 'ramya'],
	"subjects": ['java', 'python', 'html/php', 'php/js']
}
)

# get the cell value using at() function
# in id column and 1 row
print(data.at[0, 'id'])

# get the cell value using at() function
# in id column and 2 row
print(data.at[1, 'id'])

# get the cell value using at() function
# in name column and 1 row
print(data.at[0, 'name'])

# get the cell value using at() function
# in id column and 4 row
print(data.at[3, 'name'])

# get the cell value using at() function
# in subjects column and 1 row
print(data.at[0, 'subjects'])

# get the cell value using values() function
# in subjects column and 4 row
print(data.at[3, 'subjects'])
