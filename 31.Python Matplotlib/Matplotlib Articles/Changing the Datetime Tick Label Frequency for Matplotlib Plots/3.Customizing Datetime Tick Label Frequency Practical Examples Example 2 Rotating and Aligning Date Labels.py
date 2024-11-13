fig, ax = plt.subplots()
ax.plot(df.index, df["Value"])

# Rotate and align date labels
fig.autofmt_xdate()

plt.show()
