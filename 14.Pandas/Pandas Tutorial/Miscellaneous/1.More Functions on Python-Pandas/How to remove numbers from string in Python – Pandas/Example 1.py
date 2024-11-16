# code
import pandas as pd

# creating dataframe
df = pd.DataFrame.from_dict({'Name': ['May21', 'James',
                                      'Adi22', 'Hello',
                                      'Girl90'],

                             'Age': [25, 15, 20, 33, 42],

                             'Income': [21321, 12311, 25000,
                                        32454, 65465]})

# removing numbers from strings of speciafied
# column, here 'Name'
df['Name'] = df['Name'].str.replace('\d+', '')

# display output with numbers removed from
# required strings
print(df)
