# Subplots as having two types of quality
fig, ax = plt.subplots()

for key, group in df.groupby('quality'):
	group.plot('insert', 'mean', yerr='std',
			label=key, ax=ax)

plt.show()
