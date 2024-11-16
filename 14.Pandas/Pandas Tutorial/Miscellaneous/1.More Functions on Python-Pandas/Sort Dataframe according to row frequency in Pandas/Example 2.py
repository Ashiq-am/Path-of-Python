# import pandas
import pandas as pd

# create dataframe
df = pd.DataFrame({'Name': ['Mukul', 'Rohan', 'Mukul', 'Manoj',
                            'Kamal', 'Rohan', 'Robin'],

                   'age': [22, 22, 21, 20, 21, 24, 20]})

# print dataframe
print(df)

# use count() and sort()
df = df.groupby(['Name'])['age'].count().reset_index(
    name='Count').sort_values(['Count'], ascending=True)

# print dataframe
print(df)
