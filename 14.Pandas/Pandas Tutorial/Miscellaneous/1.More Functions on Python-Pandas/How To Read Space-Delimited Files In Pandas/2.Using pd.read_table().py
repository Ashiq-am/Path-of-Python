import pandas as pd

# Read space-delimited file using pd.read_table()
df = pd.read_table('space_delimited_file.txt', sep=' ')

# display the data frame
print(df)
