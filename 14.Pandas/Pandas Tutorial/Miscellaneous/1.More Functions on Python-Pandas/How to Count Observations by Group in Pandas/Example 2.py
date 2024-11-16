# import libraries
import pandas as pd

# create pandas DataFrame
df = pd.DataFrame({'Name': ['Arun', 'Arun', 'Bhuvi', 'Bhuvi',
                            'Bhuvi', 'Chandan', 'Chandan'],

                   'Department': ['CSE', 'IT', 'CSE', 'CSE',
                                  'IT', 'IT', 'CSE'],

                   'Funds': [1100, 800, 700, 600, 600, 500, 1200]})

# create a group using groupby
group = df.groupby(['Name', 'Department'])

# size of group to count observations
group = group.size()

# make a column name
group.reset_index(name='Observation')
