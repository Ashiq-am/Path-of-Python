# import pandas module
import pandas as pd

# create dataframe with 3 columns
data = pd.DataFrame({
	"id": [7058, 7059, 7072, 7054],
	"name": ['sravan', 'jyothika', 'harsha', 'ramya'],
	"subjects": ['java', 'python', 'html/php', 'php/js']
}
)

# get first row using iat() function of
# first row 2 nd column
print(data.iat[0, 1])

# get first row using iat() function of
# first row 1 st column
print(data.iat[0, 0])

# get first row using iat() function of
# first row 3 rd column
print(data.iat[0, 2])
