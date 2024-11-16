# import pandas module
import pandas as pd

#import numpy
import numpy

# create a dataframe
# with 5 rows and 4 columns
data = pd.DataFrame({
	'name': ['sravan', 'ojsawi', 'bobby', 'rohith', 'gnanesh',
			'sravan', 'sravan', 'ojaswi', numpy.nan],
	'subjects': ['java', 'php', 'java', 'php', 'java', 'html/css',
				'python', 'R', numpy.nan],
	'marks': [98, 90, 78, 91, 87, 78, 89, 90, numpy.nan],
	'age': [11, 23, 23, 21, 21, 21, 23, 21, numpy.nan]
})

# count all values in name column including NA
print(data['name'].value_counts(dropna=False))

# count all values in subjects column including NA
print(data['subjects'].value_counts(dropna=False))

# count all values in marks column excluding NA
print(data['marks'].value_counts(dropna=False))

# count all values in age column excluding NA
print(data['age'].value_counts(dropna=True))
