financial_data = {
    'Year': [2021, 2021, 2022, 2022],
    'Quarter': ['Q1', 'Q2', 'Q1', 'Q2'],
    'Revenue': [1000, 1500, 2000, 2500],
    'Profit': [200, 300, 400, 500]
}

df = pd.DataFrame(financial_data)
pivot_df = df.pivot_table(values=['Revenue', 'Profit'], index=['Year', 'Quarter'], aggfunc='sum')
print(pivot_df)
