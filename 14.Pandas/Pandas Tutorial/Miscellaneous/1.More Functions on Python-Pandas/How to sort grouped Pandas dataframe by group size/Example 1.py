# importing pandas module for dataframe
import pandas as pd

# creating a dataframe with student
# name and subject

dataframe1 = pd.DataFrame({'student_name': ['bobby', 'ojaswi', 'gnanesh',
                                            'rohith', 'karthik', 'sudheer',
                                            'vani'],

                           'subjects': ['dbms', 'python', 'dbms', 'oops',
                                        'oops', 'oops', 'dbms']})

# display dataframe
print(dataframe1)

# group the data on subjects column based on
# size and sort in descending order
a = dataframe1.groupby('subjects').size().sort_values(ascending=False)

# group the data on subjects column based on
# size and sort in ascending order
b = dataframe1.groupby('subjects').size().sort_values(ascending=True)

print(a, b)
