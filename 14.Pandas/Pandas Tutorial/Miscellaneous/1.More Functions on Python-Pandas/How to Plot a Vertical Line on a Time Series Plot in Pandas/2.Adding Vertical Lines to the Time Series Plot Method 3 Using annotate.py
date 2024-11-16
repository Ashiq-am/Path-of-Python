# Plot the time series data
ax = df.plot()
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series Plot with Annotation')

# Add a vertical line and annotation
plt.axvline(x=pd.to_datetime('2023-02-15'), color='b', linestyle=':', label='Annotation Date')
plt.annotate('Event', xy=(pd.to_datetime('2023-02-15'), df['Value'].mean()), xytext=(pd.to_datetime('2023-02-15'), df['Value'].max()),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.legend()
plt.show()
