# import pandas
import pandas as pd

# create data frame
Data = {'Name#': ['Mukul', 'Rohan', 'Mayank',
                  'Shubham', 'Aakash'],

        'Location@': ['Saharanpur', 'Meerut', 'Agra',
                      'Saharanpur', 'Meerut'],

        'Pay&': [25000, 30000, 35000, 40000, 45000]}

df = pd.DataFrame(Data)

# print original data frame
print(df)

# remove special character
df.columns = df.columns.str.replace('[#,@,&]', '')

# print file after removing special character
print("\n\n", df)
