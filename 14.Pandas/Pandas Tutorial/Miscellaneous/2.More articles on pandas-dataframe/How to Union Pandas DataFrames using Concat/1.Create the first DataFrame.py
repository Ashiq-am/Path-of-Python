import pandas as pd

students1 = {'Class': ['10','10','10'],
			'Name': ['Hari','Ravi','Aditi'],
			'Marks': [80,85,93]
		}

df1 = pd.DataFrame(students1, columns= ['Class','Name','Marks'])

df1
