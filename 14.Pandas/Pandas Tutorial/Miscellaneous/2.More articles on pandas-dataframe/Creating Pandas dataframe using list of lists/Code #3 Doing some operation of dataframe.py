# Import pandas library
import pandas as pd

# initialize list of lists
data = [[1, 5, 10], [2, 6, 9], [3, 7, 8]]

# Create the pandas DataFrame
df = pd.DataFrame(data)

# specifying cloumn names
df.columns = ['Col_1', 'Col_2', 'Col_3']

# print dataframe.
print(df, "\n")

# transpose of dataframe
df = df.transpose()
print("Transpose of above dataframe is-\n", df)
