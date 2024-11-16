# Resample by day and count
daily_counts = df.set_index('date').groupby('value').resample('D').size().unstack(fill_value=0)

print(daily_counts)
