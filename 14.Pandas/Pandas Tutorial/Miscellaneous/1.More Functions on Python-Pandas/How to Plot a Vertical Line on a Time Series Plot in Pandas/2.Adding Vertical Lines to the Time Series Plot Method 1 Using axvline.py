ax = df.plot()
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series Plot with Vertical Line')

# Add a vertical line at a specific date
plt.axvline(x=pd.to_datetime('2023-02-15'), color='r', linestyle='--', label='Important Date')
plt.legend()
plt.show()
