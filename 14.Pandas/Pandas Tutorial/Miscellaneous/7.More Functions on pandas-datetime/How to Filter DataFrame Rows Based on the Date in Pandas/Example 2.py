# import pandas library
import pandas as pd

# load csv file
df = pd.read_csv("C:\\Users\\Rohan\\OneDrive\\Desktop\\GFG\\netflix_titles.csv")

# convert date column into date format
df['date_added'] = pd.to_datetime(df['date_added'])

# filter rows on the basis of date
newdf = (df['date_added'] > '01-01-2019') & (df['date_added'] <= '31-12-2019')

# locate rows and access them using .loc() function
newdf = df.loc[newdf]

# print dataframe
print(newdf)
