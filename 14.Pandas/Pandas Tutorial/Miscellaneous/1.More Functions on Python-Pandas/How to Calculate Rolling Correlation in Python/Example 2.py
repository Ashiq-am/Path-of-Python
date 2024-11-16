data['Product A'].rolling(6).corr(data['Product B'])

# formating the output
k = 1
for i, j in enumerate(data['Product A'].rolling(6).corr(data['Product B'])):
	if (i >= 5 and i < 12):
		print(f'The correlation in sales during months\
		{k} through {i+1} is {j}')
		i = 0
		k += 1
