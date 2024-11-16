ax = df.plot()
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series Plot with Vertical Line')

# Add a vertical line at a specific date with a specified range
plt.vlines(x=pd.to_datetime('2023-02-15'), ymin=df['Value'].min(), ymax=df['Value'].max(), color='g', linestyle='-', label='Event')
plt.legend()
plt.show()
