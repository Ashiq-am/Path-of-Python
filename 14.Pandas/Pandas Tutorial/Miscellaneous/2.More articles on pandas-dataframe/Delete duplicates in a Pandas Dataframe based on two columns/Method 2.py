# import pandas library
import pandas as pd

# read data
df1 = pd.read_csv("super.csv")

# group data over columns 'order_id'
# and 'customer_id' and keep first entry only
newdf1 = df1.groupby(['order_id', 'customer_id']).first()

# print new dataframe
print(newdf1)
