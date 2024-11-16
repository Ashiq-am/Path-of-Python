# importing pandas as pd
import pandas as pd

# Create the dataframe
df = pd.DataFrame({'Date': ['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'],
                   'Event': ['Music', 'Poetry', 'Theatre', 'Comedy'],
                   'Cost': [10000, 5000, 15000, 2000]})

# Create an empty list
Row_list = []

# Iterate over each row
for i in range((df.shape[0])):
    # Create a list to store the data
    # of the current row
    cur_row = []

    # iterate over all the columns
    for j in range(df.shape[1]):
        # append the data of each
        # column to the list
        cur_row.append(df.iat[i, j])

    # append the current row to the list
    Row_list.append(cur_row)

# Print the first 3 elements
print(Row_list[:3])
