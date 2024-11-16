# import pandas library
import pandas as pd

# dictionary
Data = {'Algorithm': ['Graph', 'Dynamic Programming',
                      'Number Theory',
                      ' Sorting And Searching'],

        'Problems': ['62', '110', '40', '55']}

# create a dataframe object
df = pd.DataFrame(Data)

# convert strint to an integer
df['Problems'] = pd.to_numeric(df['Problems'])

# show the dataframw
print(df)
print("-" * 30)

# show the data type
# of each column
print(df.dtypes)
