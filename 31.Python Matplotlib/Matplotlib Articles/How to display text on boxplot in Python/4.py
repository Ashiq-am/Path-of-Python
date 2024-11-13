# add text
plt.figure(figsize=(10, 6))
sns.boxplot(data['Height (in cm)'])

plt.text(3, 0.07,
		'Points beyond 25% value',
		bbox=dict(facecolor='red',
				alpha=0.5),
		fontsize=12)

plt.text(95, 0.07,
		'Points beyond beyond 75% value',
		bbox=dict(facecolor='pink',
				alpha=0.5),
		horizontalalignment='right',
		fontsize=12)

plt.show()
