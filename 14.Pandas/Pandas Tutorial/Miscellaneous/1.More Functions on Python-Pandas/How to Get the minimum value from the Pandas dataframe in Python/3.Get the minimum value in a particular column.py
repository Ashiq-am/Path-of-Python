# import pandas module
import pandas as pd

# create a dataframe
# with 5 rows and 4 columns
data = pd.DataFrame({
	'name': ['sravan', 'ojsawi', 'bobby', 'rohith', 'gnanesh'],
	'subjects': ['java', 'php', 'html/css', 'python', 'R'],
	'marks': [98, 90, 78, 91, 87],
	'age': [11, 23, 23, 21, 21]
})

# display dataframe
print(data)

# get the miniumum in name column
print(data['name'].min())

# get the miniumum in subjects column
print(data['subjects'].min())

# get the miniumum in age column
print(data['age'].min())

# get the miniumum in marks column
print(data['marks'].min())
