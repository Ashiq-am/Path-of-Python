# import pandas module
import pandas as pd

# create dataframe with 3 columns
data = pd.DataFrame({
	"id": [7058, 7059, 7072, 7054],
	"name": ['sravan', 'jyothika', 'harsha', 'ramya'],
	"subjects": ['java', 'python', 'html/php', 'php/js']
}
)

# display dataframe
print(data)

print("--------------")


# get first column by returning dataframe
# using column_name
# display 1 row
print(data.id.head(1))
print("--------------")

# get first column by returning dataframe
# using column_name
# display 2 rows
print(data.id.head(2))
print("--------------")

# get first column by returning dataframe
# using column_name
# display 4 rows
print(data.id.head(4))
