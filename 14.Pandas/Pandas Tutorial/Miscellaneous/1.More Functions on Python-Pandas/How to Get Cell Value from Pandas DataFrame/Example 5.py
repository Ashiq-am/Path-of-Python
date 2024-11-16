# import pandas module
import pandas as pd

# create dataframe with 3 columns
data = pd.DataFrame({
	"id": [7058, 7059, 7072, 7054],
	"name": ['sravan', 'jyothika', 'harsha', 'ramya'],
	"subjects": ['java', 'python', 'html/php', 'php/js']
}
)

# get the cell value using iat() function
# in id column and 1 row
print(data.iat[0, 0])

# get the cell value using iat() function
# in name column and 1 row
print(data.iat[0, 1])

# get the cell value using iat() function
# in id column and 2 row
print(data.iat[1, 0])
