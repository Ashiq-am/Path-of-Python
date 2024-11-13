# PACF plot
plt.figure(figsize=(7, 5))
plot_pacf(data['Sunspots'], lags=50)
plt.xlabel('Lags')
plt.ylabel('Partial Autocorrelation')
plt.title('Partial Autocorrelation Function (PACF) Plot')
plt.grid(True)
plt.show()
