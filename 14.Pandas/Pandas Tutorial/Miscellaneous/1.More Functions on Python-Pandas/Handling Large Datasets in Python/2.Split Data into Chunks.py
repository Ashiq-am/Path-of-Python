import pandas as pd

# Create sample DataFrame
data = {'A': range(10000),
        'B': range(10000)}

# Process data in chunks
chunk_size = 1000
for chunk in pd.DataFrame(data).groupby(pd.DataFrame(data).index // chunk_size):
    print(chunk)
