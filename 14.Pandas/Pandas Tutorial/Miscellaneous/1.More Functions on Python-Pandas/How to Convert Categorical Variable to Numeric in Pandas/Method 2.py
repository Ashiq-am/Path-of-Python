#import pandas
import pandas as pd

# read csv
df = pd.read_csv('salary.csv')

# get the dummies and store it in a variable
dummies = pd.get_dummies(df.Education)

# Concatenate the dummies to original dataframe
merged = pd.concat([df, dummies], axis='columns')

# drop the values
merged.drop(['Education', 'Under-Graduate'], axis='columns')

# print the dataframe
print(merged)
