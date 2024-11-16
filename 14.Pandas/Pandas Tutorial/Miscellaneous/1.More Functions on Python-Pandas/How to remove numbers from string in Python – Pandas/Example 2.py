# code
import pandas as pd

# creating dataframe
df = pd.DataFrame.from_dict({'Name': ['rohan21', 'Jelly',
                                      'Alok22', 'Hey65',
                                      'boy92'],

                             'Age': [24, 25, 10, 73, 92],

                             'Income': [28421, 14611, 28200,
                                        45454, 66565]})

# removing numbers from strings of speciafied
# column, here 'Name'
df['Name'] = df['Name'].str.replace('\d+', '')

# display output with numbers removed from
# required strings
print(df)
