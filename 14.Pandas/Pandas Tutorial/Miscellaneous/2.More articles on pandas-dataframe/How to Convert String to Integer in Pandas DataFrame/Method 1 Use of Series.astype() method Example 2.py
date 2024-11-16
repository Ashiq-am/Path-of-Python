# import pandas library
import pandas as pd

# dictionary
Data = {'Algorithm': ['Graph', 'Dynamic Programming',
                      'Number Theory',
                      ' Sorting And Searching'],

        'Problems': ['62', '110', '40', '55']}

# create a dataframe object
df = pd.DataFrame(Data)

# convert string to integer
df['Problems'] = df['Problems'].astype(int)

# show the dataframe
print(df)
print("-" * 25)

# show the data type
# of each columns
print(df.dtypes)
