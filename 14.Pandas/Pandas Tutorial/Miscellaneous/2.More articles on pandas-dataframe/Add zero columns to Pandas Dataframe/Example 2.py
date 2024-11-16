# import pandas library
import pandas as pd

# create data
data = [["geeks", 1], ["for", 2], ["best", 3]]

# creating a dataframe
df = pd.DataFrame(data, columns=['col1', 'col2'])

print("data frame before adding the column:")
display(df)

# creating a new column with all zero entries
df['col3'] = 0

# showing the dataframe
print("data frame after adding the column:")
display(df)
