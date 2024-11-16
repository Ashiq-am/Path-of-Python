import pandas as pd

# Read space-delimited file using pd.read_csv()
df = pd.read_csv('space_delimited_file.txt', sep=' ')

# Display the DataFrame
print(df)
