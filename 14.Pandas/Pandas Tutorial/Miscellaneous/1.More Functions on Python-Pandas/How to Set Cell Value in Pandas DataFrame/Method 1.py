# import pandas module
import pandas as pd

# create a dataframe
# with 3 rows amd 3 columns
data = pd.DataFrame({
	'name': ['sireesha', 'ravi', 'rohith', 'pinkey', 'gnanesh'],
	'subjects': ['java', 'php', 'html/css', 'python', 'R'],
	'marks': [98, 90, 78, 91, 87]
})

# set value at 6 th location for name column
data.at[5, 'name'] = 'sri devi'

# set value at 6 th location for subjects column
data.at[5, 'subjects'] = 'jsp'


# set value at 6 th location for marks column
data.at[5, 'marks'] = 100

# set value at 4 th location for name column
data.at[4, 'name'] = 'siva nagulu'

# set value at 4 th location for subjects column
data.at[4, 'subjects'] = 'react-js'


# set value at 4 th location for marks column
data.at[4, 'marks'] = 80

# display
data
