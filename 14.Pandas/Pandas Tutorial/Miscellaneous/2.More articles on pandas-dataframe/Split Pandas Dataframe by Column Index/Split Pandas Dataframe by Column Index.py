import pandas as pd

dataset = {'toothed': [1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
		'hair': [1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
		'breathes': [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
		'legs': [1, 1, 0, 1, 1, 1, 0, 0, 1, 1],
		'species': [1, 1, 0, 1, 1, 1, 0, 0, 1, 0]
		}

df = pd.DataFrame(dataset)

df.head()
