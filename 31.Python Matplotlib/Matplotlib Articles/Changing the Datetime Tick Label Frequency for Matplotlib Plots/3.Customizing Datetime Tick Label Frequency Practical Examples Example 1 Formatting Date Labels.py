from matplotlib.dates import DateFormatter

fig, ax = plt.subplots()
ax.plot(df.index, df["Value"])

# Define the date format
date_format = DateFormatter("%b %d, %Y")
ax.xaxis.set_major_formatter(date_format)

plt.show()
