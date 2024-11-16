# Resampling the time series data based on months
# we apply it on stock close price
# 'M' indicates month
monthly_resampled_data = df.close.resample('M').mean()

# the above command will find the mean closing price
# of each month for a duration of 12 months.
monthly_resampled_data
