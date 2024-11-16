import pandas as pd

# Read file with inconsistent/multiple spaces using regex separator
df = pd.read_csv('multiple_space_delimited_file.txt', sep='\s+')

# Display the DataFrame
print(df)
