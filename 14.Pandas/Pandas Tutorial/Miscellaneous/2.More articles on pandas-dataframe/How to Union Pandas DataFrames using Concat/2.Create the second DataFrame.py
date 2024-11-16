import pandas as pd

students2 = {'Class': ['10','10','10'],
			'Name': ['Tanmay','Akshita','Rashi'],
			'Marks': [89,91,87]
		}

df2 = pd.DataFrame(students2,
				columns= ['Class','Name','Marks'])

df2
