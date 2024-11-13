objects = []
for row in stats :
	objects.append(row[1])

y_pos = np.arange(len(objects))

performance = []
for row in stats[:len(stats)-1] :
	performance.append(int(row[2]))

performance.append(int(stats[-1][2][:len(stats[-1][2])-1]))

table = tabulate(stats, headers=SHORT_HEADERS)
print(table)
