import matplotlib.dates as mdates

fig, ax = plt.subplots()
ax.plot(df.index, df["Value"])

# Set major ticks to monthly
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.show()
