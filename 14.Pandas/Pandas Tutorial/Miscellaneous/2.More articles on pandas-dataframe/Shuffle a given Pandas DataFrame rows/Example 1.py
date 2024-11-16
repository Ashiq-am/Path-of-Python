# import the module
import pandas as pd

# create a DataFrame
data = {'Name': ['Mukul', 'Rohan', 'Mayank',
                 'Shubham', 'Aakash'],
        'Class': ['BCA', 'BBA', 'BCA', 'MBA', 'BBA'],
        'Location': ['Saharanpur', 'Meerut', 'Agra',
                     'Saharanpur', 'Meerut']}
df1 = pd.DataFrame(data)

# print the original DataFrame
print("Original DataFrame :")
display(df1)

# shuffle the DataFrame rows
df2 = df1.sample(frac=1)

# print the shuffled DataFrame
print("\nAfter Shuffle:")
display(df2)
