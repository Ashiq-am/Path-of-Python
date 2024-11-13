# import Pandas library
import pandas as pd

# Read our file. Here sheet_name=1
# means we are reading the 2nd sheet or Sheet2
df = pd.read_excel('Sample1.xlsx', sheet_name = 1)
df.head()
