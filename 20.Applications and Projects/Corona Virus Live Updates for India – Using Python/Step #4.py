plt.barh(y_pos, performance, align='center', alpha=0.5,
				color=(234/256.0, 128/256.0, 252/256.0),
				edgecolor=(106/256.0, 27/256.0, 154/256.0))

plt.yticks(y_pos, objects)
plt.xlim(1,performance[-1]+1000)
plt.xlabel('Number of Cases')
plt.title('Corona Virus Cases')
plt.show()
