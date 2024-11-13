# compute percenatage of each format
percentage = []

for i in range(data.shape[0]):
	pct = (data.Runs[i] / total_runs) * 100
	percentage.append(round(pct, 2))

# display percentage
print(percentage)

# display data
data['Percentage'] = percentage
display(data)
