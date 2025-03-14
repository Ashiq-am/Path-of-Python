# import pandas module
import pandas as pd

# create dataframe with 3 columns
data = pd.DataFrame({
	"id": [7058, 7059, 7072, 7054],
	"name": ['sravan', 'jyothika', 'harsha', 'ramya'],
	"subjects": ['java', 'python', 'html/php', 'php/js']
}
)

# get the cell value using values() function
# in id column and 1 row
print(data['name'].values[0])

# get the cell value using values() function
# in id column and 2 row
print(data['id'].values[1])

# get the cell value using values() function
# in name column and 1 row
print(data['name'].values[0])

# get the cell value using values() function
# in id column and 4 row
print(data['name'].values[3])

# get the cell value using values() function
# in subjects column and 1 row
print(data['subjects'].values[0])

# get the cell value using values() function
# in subjects column and 4 row
print(data['subjects'].values[3])
