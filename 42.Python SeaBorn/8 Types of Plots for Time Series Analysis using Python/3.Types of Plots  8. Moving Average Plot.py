# Moving Average Plot
plt.figure(figsize=(7, 5))
values = data['Sunspots']

# 7-day moving average
rolling_mean = values.rolling(window=7).mean()
plt.plot(values, label='Original')
plt.plot(rolling_mean, label='7-day Moving Average', color='red')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Moving Average Plot')
plt.legend()
plt.grid(True)
plt.show()
