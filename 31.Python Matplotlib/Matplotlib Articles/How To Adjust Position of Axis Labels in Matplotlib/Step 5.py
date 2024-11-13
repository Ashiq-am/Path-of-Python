fig, ax = plt.subplots()
ax.hist( data, bins = 100, alpha = 0.6)
ax.set_xlabel("X-Label",
			fontsize = 16, loc = "right")

ax.set_ylabel("Y-Label",
			fontsize = 16, loc = "top")
