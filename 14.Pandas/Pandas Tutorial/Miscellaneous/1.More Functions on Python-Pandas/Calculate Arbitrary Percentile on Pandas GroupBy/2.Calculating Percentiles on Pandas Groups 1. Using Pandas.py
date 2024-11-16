# import pandas module
import pandas as pd

# Sample dataset
data = {
    'Category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60, 70, 80, 90]
}

# create dataframe
df = pd.DataFrame(data)

# calculate percentile on grouped data
percentiles = df.groupby('Category')['Value'].quantile(0.25)

print(percentiles)
