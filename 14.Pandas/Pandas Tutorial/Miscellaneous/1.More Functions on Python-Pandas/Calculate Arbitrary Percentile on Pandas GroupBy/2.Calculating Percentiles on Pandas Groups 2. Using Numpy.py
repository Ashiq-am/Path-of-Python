# import modules
import pandas as pd
import numpy as np

# Sample dataset
data = {
    'Category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60, 70, 80, 90]
}

# create dataframe
df = pd.DataFrame(data)

# create groups of data based on category
grouped = df.groupby('Category')

def calculate_percentile(group, percentile):
    return np.percentile(group, percentile)

# Calculate the 25th, 50th, and 90th percentiles
percentiles = grouped['Value'].agg(
    percentile_25=lambda x: calculate_percentile(x, 25),
    percentile_50=lambda x: calculate_percentile(x, 50),  # Median
    percentile_90=lambda x: calculate_percentile(x, 90)
)

print(percentiles)
