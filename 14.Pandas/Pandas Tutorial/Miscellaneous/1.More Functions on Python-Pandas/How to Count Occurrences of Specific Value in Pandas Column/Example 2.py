# import pandas module
import pandas as pd

# create a dataframe
# with 5 rows and 4 columns
data = pd.DataFrame({
	'name': ['sravan', 'ojsawi', 'bobby', 'rohith',
			'gnanesh', 'sravan', 'sravan', 'ojaswi'],
	'subjects': ['java', 'php', 'java', 'php', 'java',
				'html/css', 'python', 'R'],
	'marks': [98, 90, 78, 91, 87, 78, 89, 90],
	'age': [11, 23, 23, 21, 21, 21, 23, 21]
})

# count all values in name column
print(data['name'].value_counts())

# count all values in subjects column
print(data['subjects'].value_counts())

# count all values in marks column
print(data['marks'].value_counts())

# count all values in age column
print(data['age'].value_counts())
