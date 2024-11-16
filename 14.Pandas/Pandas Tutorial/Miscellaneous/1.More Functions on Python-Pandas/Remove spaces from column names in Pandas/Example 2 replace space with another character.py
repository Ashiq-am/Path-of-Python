# import pandas
import pandas as pd

# create data frame
Data = {'Employee Name': ['Mukul', 'Rohan', 'Mayank',
                          'Shubham', 'Aakash'],

        'Location': ['Saharanpur', 'Meerut', 'Agra',
                     'Saharanpur', 'Meerut'],

        'Sales Code': ['muk123', 'roh232', 'may989',
                       'shu564', 'aka343']}

df = pd.DataFrame(Data)

# print original data frame
print(df)

# replace space with another character
df.columns = df.columns.str.replace(' ', '_')

# print file after removing special character
print("\n\n", df)
