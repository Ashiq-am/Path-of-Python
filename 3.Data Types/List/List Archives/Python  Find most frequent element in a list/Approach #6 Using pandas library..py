import pandas as pd
List = [2, 1, 2, 2, 1, 3, 1]

# Create a panda DataFrame using the list
df=pd.DataFrame({'Number': List})

# Creating a new dataframe to store the values
# with appropriate column name
# value_counts() returns the count based on
# the grouped column values
df1 = pd.DataFrame(data=df['Number'].value_counts(), columns=[['Number','Count']])

# The values in the List become the index of the new dataframe.
# Setting these index as a column
df1['Count']=df1['Number'].index

# Fetch the list of frequently repeated columns
list(df1[df1['Number']==df1.Number.max()]['Count'])
