# import pandas library
import pandas as pd

# load data
df1 = pd.read_csv("super.csv")

# drop rows which have same order_id
# and customer_id and keep latest entry
newdf = df1.drop_duplicates(
subset = ['order_id', 'customer_id'],
keep = 'last').reset_index(drop = True)

# print latest dataframe
display(newdf)
