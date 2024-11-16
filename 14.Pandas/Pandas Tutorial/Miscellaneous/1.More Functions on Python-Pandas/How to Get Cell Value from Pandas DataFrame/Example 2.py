# import pandas module
import pandas as pd

# create dataframe with 3 columns
data = pd.DataFrame({
	"id": [7058, 7059, 7072, 7054],
	"name": ['sravan', 'jyothika', 'harsha', 'ramya'],
	"subjects": ['java', 'python', 'html/php', 'php/js']
}
)

# get the cell value using iloc() function
# in id column and 1 row
print(data['id'].iloc[0])

# get the cell value using iloc() function
# in id column and 2 row
print(data['id'].iloc[1])

# get the cell value using iloc() function
# in name column and 1 row
print(data['name'].iloc[0])

# get the cell value using iloc() function
# in id column and 4 row
print(data['name'].iloc[3])

# get the cell value using iloc() function
# in subjects column and 1 row
print(data['subjects'].iloc[0])

# get the cell value using iloc() function
# in subjects column and 4 row
print(data['subjects'].iloc[3])
