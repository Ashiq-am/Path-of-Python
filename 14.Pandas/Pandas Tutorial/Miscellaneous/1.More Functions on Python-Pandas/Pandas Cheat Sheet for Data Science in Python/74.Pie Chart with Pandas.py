grouped = df.groupby(['Origin'])
grouped.sum().plot.pie(y='Paid_Price', subplots=True)
