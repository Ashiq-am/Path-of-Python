# depict time series
fig, ax = plt.subplots(figsize=(5,5))
ymin, ymax = plt. ylim()
ax.plot(year,GDP)
plt.ylim(ymin * 50, ymax * 50)

# adjust label
ax.set_ylabel("GDP")

# assign title
ax.set_title("GDP of country over years" ,size=15)
plt.show()
