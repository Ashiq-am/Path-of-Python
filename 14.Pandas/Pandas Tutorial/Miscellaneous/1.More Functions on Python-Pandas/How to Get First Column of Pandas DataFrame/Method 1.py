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

# get first column by returning series
print(data.iloc[:, 0])

print("--------------")

# get first column by returning dataframe
print(data.iloc[:, :1])
