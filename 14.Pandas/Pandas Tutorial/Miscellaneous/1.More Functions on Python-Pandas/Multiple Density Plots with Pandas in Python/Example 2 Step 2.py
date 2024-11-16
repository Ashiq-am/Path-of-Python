# Converting to wide dataframe
data_wide = df.pivot(columns = 'day',
					values = 'total_bill')

# plotting multiple density plot
data_wide.plot.kde(figsize = (8, 6),
				linewidth = 4)
