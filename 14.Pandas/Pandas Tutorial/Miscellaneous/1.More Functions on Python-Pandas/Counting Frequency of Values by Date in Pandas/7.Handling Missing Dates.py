# Create a complete date range
all_dates = pd.date_range(start=df['date'].min(), end=df['date'].max())

# Reindex the pivot table to include all dates
pivot_table = pivot_table.reindex(all_dates, fill_value=0)
pivot_table.index.name = 'date'  # Name the index as 'date'
print(pivot_table)
