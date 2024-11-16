# import pandas module
import pandas as pd

# create a dataframe
# with 5 rows and 4 columns
data = pd.DataFrame({
	'name': ['sravan', 'bobby', 'sravan', 'sravan', 'ojaswi'],
	'subjects': ['java', 'php', 'java', 'html/css', 'python'],
	'marks': [98, 90, 78, 91, 87],
	'age': [11, 23, 23, 21, 21]
})

# get all count
data.apply(pd.value_counts)
