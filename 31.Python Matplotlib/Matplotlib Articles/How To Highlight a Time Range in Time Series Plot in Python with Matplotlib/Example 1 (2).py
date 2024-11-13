# depict illustration
fig, ax = plt.subplots(figsize=(5, 5))
ymin, ymax = plt. ylim()
ax.plot(year, GDP)
plt.ylim(ymin * 50, ymax * 50)

# adjust lables
ax.set_ylabel("GDP")

# assign title
ax.set_title("GDP of country over years", size=15)

# highlight a time range
ax.axvspan(1990, 2010, color="blue", alpha=0.3)
plt.show()
