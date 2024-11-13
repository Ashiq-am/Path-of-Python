fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df.index, df["Value"])

# Set tick frequency for the entire figure
plt.xticks(pd.date_range(start="2023-01-01", end="2023-12-31", freq="M"))
plt.yticks(np.arange(-3, 4, 1))

plt.show()
