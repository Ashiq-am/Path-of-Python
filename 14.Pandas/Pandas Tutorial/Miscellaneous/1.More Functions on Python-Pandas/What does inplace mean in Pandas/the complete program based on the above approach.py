# importing pandas
import pandas as pd

# creating dataframe
dataframe = pd.DataFrame({'Name': ['Shobhit', 'Vaibhav',
                                   'Vimal', 'Sourabh'],

                          'Class': [11, 12, 10, 9],
                          'Age': [18, 20, 21, 17]})

# Checking created dataframe
# copied dataframe
display(dataframe)

# without using inplace renaming the column
new_data = dataframe.rename(columns={'Name': 'FirstName'})

# Copied dataframe
display(new_data)

# checking whether dataframe is modified or not
# Original dataframe
display(dataframe)

# putting inplace=False
new_data_2 = dataframe.rename(columns={'Name': 'FirstName'},
                              inplace=False)

# Copied dataframe
display(new_data_2)

# checking whether dataframe is modified or not
# Original dataframe
display(dataframe)

# Putting Inplace=True
dataframe.rename(columns={'Name': 'FirstName'},
                 inplace=True)

# checking whether dataframe is modified or not
# Original dataframe
display(dataframe)
