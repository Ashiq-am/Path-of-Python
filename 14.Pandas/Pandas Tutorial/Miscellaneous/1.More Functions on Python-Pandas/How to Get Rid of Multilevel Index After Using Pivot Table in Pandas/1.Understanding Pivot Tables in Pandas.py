import pandas as pd

data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'Category': ['A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40]
}

df = pd.DataFrame(data)
pivot_df = df.pivot_table(values='Value', index='Date', columns='Category', aggfunc='sum')
print(pivot_df)
