# import pandas module
import pandas as pd

# create dataframe with 3 columns
data = pd.DataFrame({
	"id": [7058, 7059, 7072, 7054],
	"name": ['sravan', 'jyothika', 'harsha', 'ramya'],
	"subjects": ['java', 'python', 'html/php', 'php/js']
}
)

# set the index values
data = data.set_index(
	[pd.Index(['student-1', 'student-2', 'student-3', 'student-4'])])

# display dataframe
print(data)


# drop the index columns
data.reset_index(drop=True, inplace=True)

# display
print(data)
