import pandas as pd
from io import StringIO

# Sample bytes data
bytes_data = b'Name,Age,Occupation\nJohn,25,Engineer\nAlice,30,Doctor\nBob,28,Artist'

# Convert bytes to string and then to DataFrame
data_str = bytes_data.decode('utf-8')
df_method1 = pd.read_csv(StringIO(data_str))

# Display the DataFrame
print(df_method1)
