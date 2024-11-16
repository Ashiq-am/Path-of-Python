pivot_table = df.groupby(['date', 'value']).size().unstack(fill_value=0)
print(pivot_table)
