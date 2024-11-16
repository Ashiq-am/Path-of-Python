# import pandas module
import pandas as pd

# create dataframe with 3 columns
data = pd.DataFrame({
	"id": [7058, 7059, 7072, 7054],
	"name": ['sravan', 'jyothika', 'harsha', 'ramya'],
	"subjects": ['java', 'python', 'html/php', 'php/js']
}
)

# get first row using loc() function
print(data.values[:1])

# get first row using loc() function
print(data.values[:1])

# get particular column
print(data['name'].values[:1])
