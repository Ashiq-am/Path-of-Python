# Autocorrelation Plot
plt.figure(figsize=(7,5))
plot_acf(data['Sunspots'], lags=50)
plt.xlabel('Lags')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot')
plt.grid(True)
plt.show()
