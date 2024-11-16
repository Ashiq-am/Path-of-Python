# import pandas module
import pandas as pd

# read the data
data = pd.read_csv('product_sales.csv')

# display top 10 rows
print(data.head(10))

# display column names
print(data.columns)
