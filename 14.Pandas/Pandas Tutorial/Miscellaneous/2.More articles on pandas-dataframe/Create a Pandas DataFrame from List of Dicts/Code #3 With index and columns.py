# Python code demonstrate how to create
# Pandas DataFrame by lists of dicts.
import pandas as pd

# Initialise data to lists.
data = [{'Geeks': 'dataframe', 'For': 'using', 'geeks': 'list'},
        {'Geeks': 10, 'For': 20, 'geeks': 30}]

# With two column indices, values same
# as dictionary keys
df1 = pd.DataFrame(data, index=['ind1', 'ind2'],
                   columns=['Geeks', 'For'])

# With two column indices with
# one index with other name
df2 = pd.DataFrame(data, index=['indx', 'indy'])

# print for first data frame
print(df1, "\n")

# Print for second DataFrame.
print(df2)
