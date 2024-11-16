# Python program to demonstrate creating
# pandas Datadaframe from lists using zip.

import pandas as pd

# List1
Name = ['tom', 'krish', 'nick', 'juli']

# List2
Age = [25, 30, 26, 22]

# get the list of tuples from two lists.
# and merge them by using zip().
list_of_tuples = list(zip(Name, Age))

# Assign data to tuples.
list_of_tuples

# Converting lists of tuples into
# pandas Dataframe.
df = pd.DataFrame(list_of_tuples, columns=['Name', 'Age'])

# Print data.
df
