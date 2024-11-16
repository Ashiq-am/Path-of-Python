data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03'],
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Value': [10, 20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)
pivot_df = df.pivot_table(values='Value', index=['Date', 'Category'], columns='Subcategory', aggfunc='sum')
print(pivot_df)
