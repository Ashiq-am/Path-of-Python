# import pandas module
import pandas as pd

# create a dataframe
# with 5 rows and 3 columns
data = pd.DataFrame({
	'name': ['sravan', 'ojsawi', 'bobby', 'rohith', 'gnanesh'],
	'subjects': ['java', 'php', 'html/css', 'python', 'R'],
	'marks': [98, 90, 78, 91, 87]
})

# display dataframe
print(data)

# get the shape
data.shape
