import pandas as pd


data = pd.DataFrame({'Name': {0: 'Samrat', 1: 'Tomar', 2: 'Verma'},
					'Score': {0: '99', 1: '98', 2: '97'},
					'Age': {0: 22, 1: 31, 2: 33}})

pd.melt(data, id_vars=['Name'], value_vars=['Score'])

display(pd.melt(data, id_vars=['Name'], value_vars=['Score']))
