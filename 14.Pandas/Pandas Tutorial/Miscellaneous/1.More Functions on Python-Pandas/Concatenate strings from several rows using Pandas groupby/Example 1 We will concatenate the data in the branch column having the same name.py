# import pandas library
import pandas as pd

# read csv file
df = pd.read_csv("Book2.csv")

# concatenate the string
df['branch'] = df.groupby(['Name'])['branch'].transform(lambda x : ' '.join(x))

# drop duplicate data
df = df.drop_duplicates()

# show the dataframe
print(df)
