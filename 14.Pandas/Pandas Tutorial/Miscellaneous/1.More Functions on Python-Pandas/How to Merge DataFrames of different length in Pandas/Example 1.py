# importing pandas module

import pandas as pd

# create a list that contains
# student id of subject 1
list1 = [7058, 7059, 7075, 7076]

# create a list that contains
# student id of subject 2
list2 = [7058, 7059, 7012, 7075, 7076]

# create a list that contains
# student names of subject 1
list11 = ["Sravan", "Jyothika", "Deepika",
		"Kyathi"]

# create a list that contains
# student names of subject 2
list22 = ["Sravan", "Jyothika", "Salma",
		"Deepika", "Kyathi"]


# pass list1 and list11 to the
# dataframe1
dataframe1 = pd.DataFrame(
{"Student ID": list1, "Student Name": list11})
print('First data frame:')
display(dataframe1)

# pass list2 and list22 to the
# dataframe1
dataframe2 = pd.DataFrame(
{"Student ID": list2, "Student Name": list22})
print('Second data frame:')
display(dataframe2)

# apply merge function to merge the
# two dataframes
mergedf = dataframe2.merge(dataframe1, how='left')
print('Merged data frame:')
display(mergedf)
