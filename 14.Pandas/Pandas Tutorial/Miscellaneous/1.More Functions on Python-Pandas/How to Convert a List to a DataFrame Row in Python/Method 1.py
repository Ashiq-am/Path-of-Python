# import pandas module
import pandas as pd

# conside a list
list1 = ["durga", "ramya", "meghana", "mansa"]

# convert the list into dataframe row
data = pd.DataFrame(list1).T

# add columns
data.columns = ['student1', 'student2',
				'student3', 'student4']

# display
data
