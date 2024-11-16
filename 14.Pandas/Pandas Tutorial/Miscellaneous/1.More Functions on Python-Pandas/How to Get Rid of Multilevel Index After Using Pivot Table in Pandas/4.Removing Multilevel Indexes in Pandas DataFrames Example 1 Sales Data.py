sales_data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'Store': ['A', 'B', 'A', 'B'],
    'Product': ['X', 'Y', 'X', 'Y'],
    'Sales': [100, 200, 150, 250]
}

df = pd.DataFrame(sales_data)
pivot_df = df.pivot_table(values='Sales', index=['Date', 'Store'], columns='Product', aggfunc='sum')
print(pivot_df)
