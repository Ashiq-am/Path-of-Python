# Import all the required libraries
import pandas as pd

# Generation of sample data
data = {
    'A': range(1, 1000001),
    'B': range(1000000, 0, -1),
    'C': ['Category1', 'Category2'] * 500000
}

# Creation of dataframe
df = pd.DataFrame(data)

# Converting columns to more efficient data types
def optimize_data_types(df):
    for col in df.select_dtypes(include='object').columns:
        num_unique_values = len(df[col].unique())
        num_total_values = len(df[col])
        if num_unique_values / num_total_values < 0.5:
            df[col] = df[col].astype('category')
    return df


# Optimizing data types
df = optimize_data_types(df)
print(df.dtypes)
