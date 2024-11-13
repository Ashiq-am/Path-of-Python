import pandas as pd
import pyarrow as pa

# Create a Pandas DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
		'Age': [25, 30, 22]}
df = pd.DataFrame(data)

# Convert Pandas DataFrame to Arrow Table
arrow_table = pa.Table.from_pandas(df)

# Display the Arrow Table
print(arrow_table)
