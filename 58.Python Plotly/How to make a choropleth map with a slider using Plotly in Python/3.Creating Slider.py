steps = []

for i in range(len(data)):
	step = dict(method='restyle',
				args=['visible', [False] * len(data)],
				label='Year {}'.format(i + 1980))
	step['args'][1][i] = True
	steps.append(step)

sliders = [dict(active=0, pad={"t": 1}, steps=steps)]
